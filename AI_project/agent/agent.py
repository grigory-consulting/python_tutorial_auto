

from openai import OpenAI

BASE_URL = "http://localhost:1234/v1"

API_KEY = "lm-studio"

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

MODEL = "qwen3-0.6b"

def run_shell(command):
    pass

def read_file(file):
    pass

def write_file(file):
    pass

def save_memory(fact):
    pass

def read_skill(name):
    pass

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

