import random

with open("final_train.txt") as f:
    lines = f.readlines()

random.shuffle(lines)

with open("final_train_shuffled.txt","w") as f:
    f.writelines(lines)