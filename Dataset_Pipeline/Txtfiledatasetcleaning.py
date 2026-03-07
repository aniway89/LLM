pairs = []

with open("dialogues_text.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.split("__eou__")

        if len(parts) >= 2:
            user = parts[0].strip()
            bot = parts[1].strip()

            pairs.append(f"<user> {user}\n<bot> {bot}\n")

with open("train2.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(pairs))