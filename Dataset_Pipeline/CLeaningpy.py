import json

with open("data.json","r") as f:
    data = json.load(f)

lines = []

for item in data["rows"]:
    conv = item["row"]["utterances"]
    
    for i in range(len(conv)-1):
        inp = conv[i]
        out = conv[i+1]

        lines.append(f"User: {inp}\nBot: {out}\n")

with open("train.txt","w") as f:
    f.write("\n".join(lines))