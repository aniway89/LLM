# Building My First Conversational LLM From Scratch

### A Journey Through Datasets, Tokenization, and Hardware Limits

---

## Introduction

For a long time I’ve been fascinated by how modern AI systems like large language models work. Instead of only *using* them, I wanted to understand how they are actually built — from the raw data all the way to the trained model.

So I started a small but exciting experiment:

> **Build a tiny conversational LLM from scratch.**

Not something huge like GPT-4.
Not something trained on trillions of tokens.

Just a **small model capable of answering simple conversational questions**.

Questions like:

* *How are you?*
* *What is your name?*
* *What do you call “wall” in Japanese?*
* *Where are you from?*

Simple responses, simple conversations — but powered by a **real transformer model that I trained myself**.

This blog documents the entire process: the datasets, the mistakes, the tokenization problems, the hardware limits, and how I adapted everything to make it work.

---

# The Original Idea

Initially, my plan was to train the model primarily on **Japanese conversational datasets**.

The idea was interesting: a small model that could answer **simple English questions and provide Japanese translations** for certain words.

But after collecting several Japanese datasets, I discovered a major problem.

The **datasets were too small**.

Training a language model requires a reasonable amount of data. With only a few thousand conversations, the model would not generalize well and would likely overfit.

So I had to rethink the plan.

---

# Switching to English Conversation Data

To solve the dataset problem, I switched the training data to **English conversational datasets**.

This allowed me to train the model on:

* everyday conversations
* question-answer interactions
* dialogue exchanges
* natural language responses

The goal was to let the model learn **how conversations flow**.

Once that foundation works, additional languages like Japanese can be added later.

---

# The Datasets I Used

Instead of relying on a single dataset, I decided to combine **multiple conversational sources**.

Each dataset teaches the model something slightly different.

---

## 1. DailyDialog Dataset

One of the most useful datasets I found was **DailyDialog**.

It contains thousands of natural conversations between people discussing topics like:

* school
* daily life
* hobbies
* relationships
* emotions

Example conversation:

```
How was your education going on in Australia?
I'm going to graduate this summer.
Where are you going to work then?
I'm planning to return to China after graduation.
```

This dataset helps the model learn **natural dialogue structure**.

---

## 2. Simple Conversation Dataset

Another dataset contains **very basic dialogue pairs**.

Example:

```
hi, how are you doing? -> i'm fine. how about yourself?
i'm fine. how about yourself? -> i'm pretty good. thanks for asking.
```

These patterns teach the model things like:

* greetings
* polite responses
* short conversational replies

This is perfect for a **small conversational LLM**.

---

## 3. Dialogue Dataset with Conversation Markers

Some datasets use a special separator:

```
__eou__
```

This means:

```
End Of Utterance
```

Example:

```
The kitchen stinks. __eou__
I'll throw out the garbage. __eou__
```

This format is useful because it clearly tells the model **where one speaker stops and another begins**.

---

## 4. SQuAD Dataset

I also added part of the **SQuAD dataset**, which contains question-answer pairs.

Example:

```
Question: When did Beyonce start becoming popular?
Answer: In the late 1990s
```

This teaches the model to handle **direct questions with factual answers**.

---

# Combining the Datasets

Because every dataset had a **different format**, they needed to be merged into a single training file.

I created a simple script that combined everything into one dataset.

```python
files = ["train.txt", "train1.txt", "train2.txt", "train3.txt"]

with open("final_train.txt", "w", encoding="utf-8") as outfile:
    for fname in files:
        with open(fname, "r", encoding="utf-8") as infile:
            outfile.write(infile.read() + "\n")
```

After this step, I had a **single unified training corpus**.

---

# Tokenization: The First Major Challenge

Next came tokenization.

Tokenization converts text into **numerical tokens** that the neural network can process.

At first, I used the **GPT tokenizer library**.

But almost immediately I encountered a serious problem.

---

## The Giant Sequence Error

While preparing the dataset, the tokenizer produced this error:

```
Token indices sequence length is longer than the specified maximum sequence length for this model
(2847532 > 1024)
```

The issue was simple but important.

I had accidentally tried to tokenize **the entire dataset as one giant sequence**.

That created a token sequence of **2.8 million tokens**, which obviously exceeds the **1024 token limit** of the model.

---

# The Solution: Chunking the Dataset

The fix was to break the dataset into **smaller blocks**.

Instead of processing everything at once, the text is split into chunks of **1024 tokens**.

This ensures:

* stable training
* manageable memory usage
* compatibility with the transformer architecture

Chunking the data was one of the **key steps that allowed training to proceed**.

---

# Model Architecture

For this experiment I built a **Tiny GPT-style transformer model**.

The model contains:

* token embedding layer
* transformer encoder blocks
* language modeling head

The architecture is intentionally small so it can train within limited resources.

Example structure:

```
Embedding Layer
↓
Transformer Blocks
↓
Language Modeling Head
```

Even though the model is small, the structure is similar to real LLMs.

---

# Hardware Limitations

One of the biggest constraints in this project is **hardware**.

Training language models requires large GPUs, but my system cannot handle heavy workloads.

Because of this, I rely on:

**Google Colab Notebooks**

This allows me to:

* access free GPUs
* run training sessions
* experiment with model parameters

However, Colab sessions have **time limits**, so training must be carefully managed.

---

# Optimizing the Training Process

To make the model train successfully on limited hardware, I adjusted several parameters.

Examples include:

* increasing block size carefully
* adjusting training steps
* modifying batch sizes
* reducing model size

These tweaks ensure the model stays **within hardware limits**.

---

# The Current Training Setup

My training pipeline currently looks like this:

1. Collect datasets
2. Convert them into text format
3. Merge them into one dataset
4. Tokenize the text
5. Split tokens into blocks
6. Train a transformer model
7. Monitor training loss

Everything is being trained through **Google Colab**.

---

# Future Improvements

This project is still in its early stages.

Some improvements I plan to explore include:

* adding Japanese datasets again
* increasing dataset size
* improving tokenizer efficiency
* experimenting with larger models
* implementing better dialogue formatting

Eventually I want to create a **more capable conversational AI system**.

---

# Final Thoughts

This project is not about creating the biggest or smartest AI.

It is about **learning the foundations of language models**.

By building everything step by step — from datasets to training loops — I gained a much deeper understanding of:

* how LLMs process text
* how tokenization works
* how transformers operate
* how hardware limitations shape model design

This is only the beginning of the journey.

The next steps will involve **improving the architecture, expanding the datasets, and refining the training pipeline**.

---

# Author

**Ayan Khan**





```
hope this will work :)
```
