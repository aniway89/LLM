# BLOG 4 — Final Day: Project Completion

## The End of This Experiment

After nearly a **month of learning, experimenting, debugging, and training**, I have finally completed this small language model project.

What started as curiosity about **how Large Language Models actually work** turned into a full learning journey where I implemented and trained a **Transformer-based language model from scratch using PyTorch**.

The model I trained contains **approximately 5 million parameters** and is trained using a **character-level transformer architecture**.

Even though it is a very small model compared to modern LLMs, completing this project feels like a **huge achievement for me**.

---

# The Result

After multiple training sessions and checkpoint recoveries, the model successfully finished training with the following configuration:

**Model Details**

* ~5M parameters
* Transformer architecture
* Character-level tokenization
* Context length: 256
* Multi-head attention
* Trained using PyTorch

The model is capable of:

* Generating simple text
* Continuing prompts
* Producing basic conversational patterns

While the responses are sometimes imperfect or unusual, the model **does generate language**, which proves that the system works.

For a small experiment like this, that is a very satisfying result.

---

# Limitations of This Model

This project also helped me understand **why modern LLMs are so large and complex**.

This model has several limitations:

### Small Parameter Size

With only **~5 million parameters**, the model is extremely small compared to real LLMs.

For comparison:

| Model      | Parameters |
| ---------- | ---------- |
| Tiny GPT-2 | 124M       |
| GPT-3      | 175B       |

This means the model cannot perform complex reasoning or advanced language understanding.

---

### Character-Level Tokenization

The model predicts **characters instead of words or tokens**, which makes learning language much harder and slower.

Modern LLMs use **subword tokenization**, which is far more efficient.

---

### Limited Dataset

The dataset used for training is relatively small and limited in scope, which affects the quality of generated responses.

---

### Training Compute

The model was trained using **Google Colab GPU sessions**, which come with time limits and resource constraints.

Because of this, training had to be done across **multiple sessions using checkpoints**.

---

# What Could Be Improved

If I revisit this project in the future with **better resources**, there are many improvements that could be made:

* Train a **larger model (20M – 100M parameters)**
* Use **token-level or BPE tokenization**
* Train on a **much larger dataset**
* Implement **better sampling methods**
* Improve the **transformer architecture**
* Train for **longer steps**

With more compute and data, the model could become significantly more capable.

---

# Personal Reflection

This project took **a lot of time, effort, and patience**.

For nearly a month, I spent time learning:

* how transformers work
* how attention mechanisms operate
* how training loops function
* how language models generate text

There were many errors, crashes, and unexpected problems along the way.

But reaching the end of this project and seeing the model **actually generate text** makes all that effort worth it.

For my current level of research and available resources, this project is **more than enough**.

I am genuinely satisfied with the result.

---

# What Comes Next

This is not the end of the journey.

I plan to continue learning more about:

* transformer optimization
* efficient architectures
* reasoning models
* new research papers

In the future, when I have **better hardware and resources**, I will likely return to this project and try to improve it further.

For now, I am proud of what I built and what I learned along the way.

---

# Final Thoughts

Building even a small language model from scratch gives a deep understanding of how these systems work.

This project might be small compared to real LLMs, but for me it represents **a major milestone in my learning journey**.

And this is only the beginning.

More experiments and improvements will come in the future.
