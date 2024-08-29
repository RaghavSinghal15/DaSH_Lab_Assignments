import requests
import sys
import json

rng = sys.argv[1]
idz = sys.argv[2] 
i = rng.split(":")[0]
j = rng.split(":")[1]

i = int(i)
j = int(j)


f = open("./input.txt", "r") 
prompts = f.readlines()
f.close()
outputs = []

for prompt in prompts[i-1:j]: 
    params = {
        "prompt": prompt
    }
    response = requests.get("http://127.0.0.1:5000/Llm", params=params)
    output = response.json()
    outputs.append(output)

f = open(f"./output{idz}.json","w")
json.dump(outputs,f,indent = 4)
f.close()   
