

from openai import OpenAI
import time


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
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Explain what a string in Python is."}
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
        

# main()
#demo_streaming()
demo_temperature()