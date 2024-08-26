import os
import time
import json
from groq import Groq

API_KEY = "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"
client = Groq( api_key = API_KEY)


def getResp(prompt: str):
    timesent = time.time()

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    timerecv = time.time()

    output = {
        "Prompt": prompt, 
        "Message": chat_completion.choices[0].message.content, 
        "TimeSent": timesent, 
        "TimeRecvd": timerecv, 
        "Source": "Groq"
    }

    return output

f = open("./input.txt", "r")
prompts = f.readlines()
outputs = []

for prompt in prompts: 
    output = getResp(prompt)
    outputs.append(output)

f = open("./output.json","w")
json.dump(outputs,f,indent = 4)
f.close()   