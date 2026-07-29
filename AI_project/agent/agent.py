

from openai import OpenAI
from pathlib import Path
import subprocess
from datetime import date, datetime
import json



ROOT = Path(__file__).resolve().parent
SOUL = ROOT / "SOUL.md"
MEMORY = ROOT / "MEMORY.md"
SKILLS = ROOT / "skills"
MAX_STEPS = 20 # agent loop  


BASE_URL = "http://localhost:1234/v1"
API_KEY = "lm-studio"
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)
MODEL = "qwen3-0.6b"
MODEL = "qwen/qwen3.6-35b-a3b"

def run_shell(command):
    print(f"\n  [tool] run_bash: {command}")
    if input("  execute? [y/N] ").strip().lower() != "y":
        return "User declined to run this command."
    result = subprocess.run(command, shell=True, capture_output=True,
                            text=True, timeout=60)
    return (result.stdout + result.stderr)[-4000:] or "(no output)"


def read_file(path: str) -> str:
    return Path(path).expanduser().read_text()[:8000]


def write_file(path: str, content: str) -> str:
    p = Path(path).expanduser()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)
    return f"Wrote {len(content)} chars to {p}"


def save_memory(fact: str) -> str:
    with MEMORY.open("a") as f:
        f.write(f"- {date.today()}: {fact}\n")
    return "Saved."


def read_skill(name: str) -> str:
    path = SKILLS / f"{name}.md"
    if not path.exists():
        return f"No skill named '{name}'. Available: " + ", ".join(
            p.stem for p in SKILLS.glob("*.md"))
    return path.read_text()



TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "run_shell",
            "description": "Run a shell command and return stdout+stderr. "
                           "The user must confirm every command.",
            "parameters": {
                "type": "object",
                "properties": {"command": {"type": "string"}},
                "required": ["command"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a text file and return its content.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write text to a file (overwrites).",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "content": {"type": "string"},
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "save_memory",
            "description": "Append one durable fact about the user or the ongoing "
                           "work to MEMORY.md. Use for things worth remembering "
                           "across sessions, not for conversation details.",
            "parameters": {
                "type": "object",
                "properties": {"fact": {"type": "string"}},
                "required": ["fact"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_skill",
            "description": "Load the full instructions of a skill by name "
                           "(see the skill list in the system prompt).",
            "parameters": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
                "required": ["name"],
            },
        },
    },
]


available_tools = {
    "run_shell" : run_shell,
    "read_file": read_file,
    "write_file": write_file,
    "save_memory": save_memory,
    "read_skill": read_skill,
}

def system_prompt():
    soul = SOUL.read_text() if SOUL.exists() else "You are helpful agent."
    memory = MEMORY.read_text() if MEMORY.exists() else "(none)"

    return soul + "\n\n" + "## Memory " + memory

def run(messages):
    for i in range(MAX_STEPS):
        response = client.chat.completions.create(
            model=MODEL, messages=messages, tools=TOOLS
        )

        msg = response.choices[0].message
        if not msg.tool_calls:
            print(msg.content)
            return # escape the function

        messages.append(msg)

        # call the tools
        for call in msg.tool_calls:
            arguments = json.loads(call.function.arguments)
            result = available_tools[call.function.name](**arguments)
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": str(result)
                }
            )

def main():
    messages = [{"role": "system", "content": system_prompt()}] 
    while True:
        try:
            user = input("you> ").strip()
        except (KeyboardInterrupt):
            print()
            break

        if not user:
            continue

        messages.append({"role": "user", "content": user})
        run(messages)
        # Update memory 
        messages[0] = {"role": "system", "content": system_prompt()}


main()