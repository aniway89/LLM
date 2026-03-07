# LLM

### Building a Small but Functional 10M Parameter LLM

This repository documents the journey of building a **small but functional Large Language Model (LLM)** from scratch.

The goal of this project is to gradually develop a language model capable of understanding and generating text in:

* 🇺🇸 **English**
* 🇯🇵 **Japanese**

Instead of jumping directly to large-scale architectures, this project focuses on **learning the core mechanics of LLMs step by step**, starting from the most fundamental models and progressively improving them.

---

# 🎯 Project Goals

The long-term objective is to build and experiment with a **10M parameter transformer-based language model** while documenting the entire learning and engineering process.

This repository will track:

* 📚 **Learning progress**
* 🧪 **Experiments**
* 🧠 **Model training**
* ⚙️ **Engineering challenges**
* 🛠 **Solutions and optimizations**
* 📈 **Model improvements over time**

The project is structured as a **learning log + engineering notebook**, where each stage of development is recorded.

---

# 📖 Background

Before starting this repository, I spent **about one month studying the fundamentals of Large Language Models**.

Although I already had general familiarity with **AI and LLMs**, I wanted to understand their **internal mechanics more deeply**, including how they are actually built and trained.

During this study phase, I explored several key concepts:

* Transformers architecture
* Tokenization strategies
* Language model training pipelines
* Dataset preparation
* Small-scale language models
* Core LLM architecture principles
* **BLM (Bigram Language Model)** as the first experimental model

This preparation phase helped build the theoretical foundation required before attempting to build a real system.

This repository marks the **start of the practical implementation journey**.

---

# 🚧 Project Progress

The project started with extremely small experiments and gradually evolved toward a working transformer model.

### Early Stage

The first working experiment was a **Bigram Language Model (BLM)** used to understand:

* token prediction
* probability distributions
* training loops
* dataset preparation

This stage helped establish a minimal but working language model pipeline.

---

### Current Stage

The project has now progressed to training a **~5 million parameter transformer model** using **character-level tokenization**.

Key characteristics of the current model:

* ~5M parameters
* Transformer-based architecture
* Character-level tokenizer
* Designed to run within **Google Colab resource limits**

---

# ⚠️ Engineering Challenges

One of the biggest challenges in this project has been **hardware limitations**.

Since the training environment is based on **Google Colab Free Tier**, the available resources are limited.

Typical environment constraints include:

### RAM

Approximately **12GB system RAM**

This memory must handle:

* Model weights
* Optimizer states
* Dataset batches
* Python runtime

Efficient memory management is therefore critical.

---

### CPU

Colab typically provides **2 virtual CPUs**, which affects:

* Data loading speed
* preprocessing
* training throughput

Because of this, the codebase has been optimized to remain **CPU-friendly and memory efficient**.

---

### GPU Availability

GPU access on the free tier is **not guaranteed**.

Possible GPUs include:

* NVIDIA T4
* NVIDIA P100
* Sometimes no GPU

This means the training system must remain **robust even without GPU acceleration**.

---

# ⏱ The Biggest Limitation: Session Timeout

The most significant constraint encountered was **Colab's session time limit**.

Free sessions typically run for **a maximum of ~12 hours** before automatically shutting down.

For machine learning training workloads, this is a major obstacle because:

* long training jobs get interrupted
* progress can be lost
* restarting training becomes necessary

Early experiments frequently failed because the training session terminated before completion.

---

# 🧠 Solution: Chunk-Based Training

To overcome the 12-hour runtime limit, the training pipeline was redesigned using a **chunk-based training strategy**.

Instead of one long training session, the training process is divided into **independent segments (chunks)**.

Each chunk performs the following steps:

1. Load the latest checkpoint
2. Train for a defined number of steps
3. Save progress
4. Exit safely before the session timeout

This approach allows the training to **continue across multiple Colab sessions** without losing progress.

---

# ⚙️ Code Optimization

To ensure the model runs within Colab's constraints, the code was optimized for:

### Memory Efficiency

* Reduced batch sizes
* Controlled tensor allocation
* Frequent checkpointing

### CPU Efficiency

* Lightweight preprocessing
* Efficient training loops
* Minimal overhead in the data pipeline

These optimizations allow the model to train reliably within:

* **12GB RAM**
* **limited CPU resources**

---

# 📊 Current Model Status

The current model being trained in this repository:

**Model size:** ~5 Million Parameters
**Tokenization:** Character-level
**Architecture:** Transformer-based
**Training environment:** Google Colab (free tier)

The training system is now stable enough to **resume training across sessions**.

---

# 🚀 Future Goals

Next development steps include:

* Scaling toward **10M+ parameter models**
* Improving dataset quality
* experimenting with **subword tokenization**
* optimizing training stability
* improving generation quality

Each stage will be documented as the project evolves.

---

# 📷 Screenshots

![App Screenshot](https://github.com/aniway89/LLM/blob/main/LOG.png?raw=true)

---

# 👨‍💻 Author

Hi! I'm **Ayan**.

This repository is part of my personal journey to understand how **Large Language Models actually work under the hood** by building them from scratch.

GitHub:
https://github.com/aniway89

---

⭐ If you find this project interesting, feel free to follow the progress.
