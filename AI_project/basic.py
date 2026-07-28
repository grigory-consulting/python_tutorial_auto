

from openai import OpenAI
import time
import json 


client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

def main():
    models = client.models.list()

    for m in models.data:
        print(m.id)

    # Chat completion 

    response = client.chat.completions.create(
        model = "qwen3-0.6b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Answer ONLY in datetime even if you dont know."},
            #{"role": "user", "content": "Explain what a string in Python is."}
            {"role": "user", "content": "What time is it? "}
        ]
    )
    print("Answer:")
    print(response.choices[0].message.content)

    # In-context learning -> give some examples and let LLM do its job

    response = client.chat.completions.create(
        model = "qwen3-0.6b",
        messages=[
            # Context
            {"role": "system", "content": "Follow the pattern shown in the examples"}, # 
            {"role": "user", "content": "I need two monitors by Friday."},
            {"role": "assistant", "content": '{"item": "monitor", "quantity": "2", "deadline": "Friday"}' },
            {"role": "user", "content": "Please send me one laptop, no rush."},
            {"role": "assistant", "content": '{"item": "laptop", "quantity": "1", "deadline": "undefined"}' },
            {"role": "user", "content": "Ship me three USB-C cables by Monday"},
            {"role": "assistant", "content": '{"item": "USB-C cable", "quantity": "3", "deadline": "Monday"}' },
            # ---

            # Query 
            {"role": "user", "content": "We require five docking stations by the end of September."}, 

        ]
    )

    print("In-context:")
    print(response.choices[0].message.content)


def demo_streaming():

    stream = client.chat.completions.create(
        model="qwen3-0.6b",
        messages=[
            {"role": "system", "content": "You are helpful assistant."},
            {"role": "user", "content": "Count from 1 to 100, one number per line."}
        ],
        stream=True,
    )

    #print(stream.choices[0].message.content)
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            #time.sleep(0.3) #
            print(delta,end="")

def demo_multiturn(): # idea how chatbots are working 
    messages=[
            {"role": "system", "content": "You are helpful assistant. Answer in plain text, no markdown."},]
    for question in ["What is the capital of India?", "And its population?"]:
        messages.append({"role":"user", "content": question}) 
        response = client.chat.completions.create(
            model="qwen3-0.6b",messages=messages
        )
        answer = response.choices[0].message.content
        messages.append({"role": "assistant", "content": answer})
        print(f"user> {question}")
        print(f"model> {answer}")


def demo_temperature(): # Temperature is a value for creativeness/fantasy 
    prompt = "Give a name for a coffee hop run by robots. Name only."
    for temp in [0.0, 0.0, 0.3, 0.3, 0.8,0.8, 1., 1.]:
        response= client.chat.completions.create(
            model="qwen3-0.6b",
            messages=[
                {"role": "system", "content": "You are helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=temp
        )
        print(f"temp={temp}: {response.choices[0].message.content}")
        

def demo_structured_output():
    schema = {
        "type": "object",
        "properties": {
            "item": {"type": "string"},
            "quantity": {"type": "integer"},
            "deadline": {"type": ["string", "null"]}
        },
        "required": ["item", "quantity", "deadline"]
    }

    response = client.chat.completions.create(
        model= "qwen3-0.6",
        messages=[
            {"role": "system","content":"Extract the order: item = product name (singular), quantity = number, deadline = due date or null"},
            {"role": "user", "content": "We require five docking stations by the end of September."}
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {"name": "order", "schema": schema}
        }, 
        temperature=0.0,
    )

    order = json.loads(response.choices[0].message.content) # Python Object: Dictionary 
    print(order)
    print(order["quantity"], type(order["quantity"]))

def demo_tool_calling():

    def get_current_time():
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M")

    available_tools = {"get_current_time": get_current_time}
    
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time", 
                "description": "Return the current local date and time",
                "parameters": {"type": "object", "properties": {}},
            }
        }
    ]

    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What time is it? "}
        ]

    response = client.chat.completions.create(
        model="qwen3-0.6b",
        messages=messages,
        tools=tools,
        temperature=0.0
    )

    msg = response.choices[0].message
    print(msg.tool_calls[0])
    result = available_tools[msg.tool_calls[0].function.name]() # () -> actual function call 

    messages.append(msg)
    messages.append({"role": "tool", "tool_call_id": msg.tool_calls[0].id, "content": result})

    response = client.chat.completions.create(
        model="qwen3-0.6b",
        messages=messages,
        tools=tools,
        temperature=0.0
    )
    print(response.choices[0].message.content) 

def demo_tool_calling_python():

    def run_python(code):
        import io, contextlib
        buffer = io.StringIO()
        try:
            with contextlib.redirect_stdout(buffer):
                exec(code, {})
        except Exception as e:
            return f"Error: {e}"
        return buffer.getvalue() or "(code produced no output — use print())"


    tools = [
        {
            "type": "function",
            "function": {
                "name": "run_python", 
                "description": "Execute Python code and return what it prints.",
                "parameters": {
                    "type": "object", 
                    "properties": {"code": {"type": "string", "description": "Python code, must print() the result."}},
                    "required": ["code"]
                    },
            }
        }
    ] 
    messages=[
            {"role": "system", "content": "You are a helpful assistant. To answer questions, write Python code."},
            {"role": "user", "content": "Which files are in the current directory?"}
        ]

    response = client.chat.completions.create(
        model = "qwen3-0.6b",
        messages=messages,
        tools=tools,
        temperature=0.0
    )

    msg = response.choices[0].message
    messages.append(msg)
    for tool_call in msg.tool_calls:
        args = json.loads(tool_call.function.arguments)
        print(args["code"])

        if input("execute this code? [y/N]").strip().lower() == "y":
            result = run_python(args["code"])
            print(result)
        else:
            print("skipped")


    

#main()
#demo_streaming()
#demo_temperature()
#demo_structured_output()
demo_tool_calling_python()