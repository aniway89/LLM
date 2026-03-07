import json

with open("SQAD.json", "r", encoding="utf-8") as f:
    data = json.load(f)

pairs = []

for article in data["data"]:
    for paragraph in article["paragraphs"]:
        for qa in paragraph["qas"]:
            question = qa["question"]

            if qa["answers"]:
                answer = qa["answers"][0]["text"]

                pairs.append(f"<user> {question}\n<bot> {answer}\n")

with open("train3.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(pairs))

print("done")