# LLM

### Building a Small Transformer Language Model From Scratch

This repository documents the journey of building a **small but functional Transformer-based Language Model (LLM)** from scratch.

The goal of this project was not to create a production-level AI system, but to **deeply understand how modern language models work internally** by implementing one step by step.

Instead of relying on existing frameworks or pretrained models, the entire system was built and trained manually using **PyTorch**, focusing on understanding the core mechanics behind LLMs.

---

# 🎯 Project Goals

The main objective of this project was to **learn how language models actually work under the hood** by building one from scratch.

This repository documents the entire process including:

* 📚 Learning and research
* 🧪 Small experiments
* 🧠 Model training
* ⚙️ Engineering challenges
* 🛠 Solutions and optimizations
* 📈 Model development progress

Rather than being just a code repository, this project also serves as a **learning log and engineering journal** that tracks the process of building a language model step by step.

---

# 📖 Background

Before starting this project, I spent **about one month studying the fundamentals of Large Language Models**.

Although I already had general familiarity with AI and LLMs, I wanted to understand **how these systems are actually built and trained**.

During the research phase I explored topics such as:

* Transformer architecture
* Attention mechanisms
* Tokenization strategies
* Language model training pipelines
* Dataset preparation
* Sampling strategies
* Small-scale language models

The first experimental model implemented was a **Bigram Language Model (BLM)** which helped build intuition about:

* token prediction
* probability distributions
* training loops
* text generation

After understanding these basics, the project progressed toward implementing a **full transformer-based model**.

---

# 🚧 Project Progress

The project evolved through several stages.

### Early Stage

The first working experiment was a **Bigram Language Model**, which was used to understand the simplest possible language model architecture.

This stage focused on understanding:

* how tokens predict the next token
* probability distributions
* training loops
* dataset handling

It served as a minimal but functional starting point.

---

### Transformer Implementation

After the bigram model experiment, the project moved toward building a **Transformer-based architecture**.

The transformer model includes:

* Multi-head self-attention
* Feed-forward neural networks
* Layer normalization
* Positional embeddings
* Autoregressive text generation

This architecture forms the foundation used by modern LLM systems.

---

# 📊 Current Model Status

The final model trained in this repository has approximately:

**~5 Million Parameters**

Model characteristics:

* Transformer-based architecture
* Character-level tokenization
* Context length: 256
* Multi-head attention
* Implemented using PyTorch

The model is capable of generating simple text and continuing prompts.

Example prompt:
```
User: Hello
Bot:


Example generated output:


Bot: We are the Macs preservatives at the Mac...
```


Because this is a **very small experimental model**, the responses are sometimes unusual or grammatically imperfect. However, the system successfully demonstrates how language generation works.

---

# ⚠️ Engineering Challenges

One of the biggest challenges during this project was **hardware limitations**.

The entire training process was done using **Google Colab Free Tier**, which comes with several restrictions.

---

### RAM Limitations

The environment typically provides around:

**~12GB System RAM**

This memory must handle:

* model weights
* optimizer states
* dataset batches
* runtime memory

Efficient memory management was therefore important for stable training.

---

### CPU Constraints

Colab generally provides only **2 virtual CPUs**, which affects:

* preprocessing speed
* dataset loading
* training throughput

Because of this, the codebase was written to remain **CPU-friendly and lightweight**.

---

### GPU Availability

GPU access on the free tier is **not always guaranteed**.

Possible hardware includes:

* NVIDIA T4
* NVIDIA P100
* sometimes no GPU at all

Because of this uncertainty, the training system had to remain **robust even when GPU was unavailable**.

---

# ⏱ The Biggest Limitation: Session Timeout

One of the biggest obstacles encountered was **Google Colab's session time limit**.

Free sessions usually run for **a maximum of around 12 hours** before automatically shutting down.

For machine learning training workloads this is problematic because:

* long training jobs get interrupted
* progress can be lost
* training must restart

This became a major issue during early training experiments.

---

# 🧠 Solution: Checkpoint-Based Training

To solve the session timeout problem, the training system was redesigned using **checkpoint-based training**.

The process works as follows:

1. Save model checkpoints during training
2. Reload checkpoints when the session restarts
3. Continue training from the last saved step

This allowed training to continue across **multiple Colab sessions** without losing progress.

This approach made it possible to complete the full training process despite the environment limitations.

---

# ⚙️ Code Optimization

To ensure the model runs reliably within Colab constraints, the code was optimized for:

### Memory Efficiency

* controlled batch sizes
* careful tensor allocation
* regular checkpointing

### Training Stability

* gradient management
* stable training loops
* periodic loss evaluation

These optimizations allowed the model to train successfully within limited resources.

---

# 🧠 Project Limitations

Although the project successfully produced a working language model, several limitations exist:

* Small model size (~5M parameters)
* Character-level tokenization
* Limited training dataset
* Limited compute resources
* Relatively short training duration

Because of these limitations, the model cannot perform complex reasoning or advanced language tasks.

However, for a small research experiment, the result is still meaningful.

---

# 🚀 Future Improvements

If better resources become available in the future, several improvements could be explored:

* Scaling the model toward **10M+ parameters**
* Switching to **subword tokenization**
* training on larger datasets
* experimenting with improved transformer architectures
* longer training runs

These improvements could significantly increase model capability.

For now, the project achieved its primary goal: **understanding how language models are built and trained**.

---

# 💭 Personal Reflection

This project took **about a month of learning, experimenting, debugging, and training**.

During this time I learned a lot about:

* transformers
* attention mechanisms
* language model training
* PyTorch implementation
* handling real engineering constraints

For the level of research and resources available to me right now, this project is **more than enough**, and I am genuinely satisfied with the result.

Building even a small language model from scratch was a valuable experience.

In the future, I may return to this project and improve it further when I have access to **better hardware and more training resources**.

---

# 📷 Screenshots

![Training Log](https://github.com/aniway89/LLM/blob/main/LOG.png?raw=true)

---

# 👨‍💻 Author

Hi! I'm **Ayan**.

This repository is part of my personal journey to understand **how Large Language Models actually work** by building them from scratch.

GitHub:  
https://github.com/aniway89

---

⭐ If you find this project interesting, feel free to follow the progress.
