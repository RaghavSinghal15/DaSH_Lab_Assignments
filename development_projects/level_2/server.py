from flask import Flask, request
import time 
from groq import Groq

API_KEY = "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"
client = Groq( api_key = API_KEY)
app = Flask(__name__) 

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

@app.route("/")
def base():
    p = request.args.get("prompt")
    return "hello" + p 

@app.route("/Llm")
def prompt():
    p = request.args.get("prompt")
    return getResp(p)

    



app.run(debug = True)


