# BLOG 2 — Building Our First 5M Parameter LLM Under Extreme Constraints

## Introduction

After several experiments and many failed attempts, we finally reached an important milestone in our project: **training a 5 million parameter language model** using **character-level tokenization**.

This stage of the project was not just about training a model. It was about **engineering around severe computational limitations**, particularly those imposed by **Google Colab's free tier**.

Our biggest challenge was not the architecture itself — it was **making the training survive long enough to finish**.

This blog documents the technical journey, the limitations we faced, and the engineering decisions we made to overcome them.

---

# The Biggest Bottleneck: Google Colab Session Limits

The free version of Google Colab is an amazing tool for experimentation, but it comes with strict limitations.

The most difficult constraint for our project was:

**A maximum runtime of approximately 12 hours per session.**

For training neural networks — especially transformers — this is a major obstacle.

Our early training runs repeatedly failed because:

* The session expired before training finished
* The runtime disconnected
* Memory was exhausted
* Checkpoints were not saved frequently enough

This meant **hours of training progress were lost** multiple times.

At one point we attempted to run the model continuously for **48 hours**, but the Colab session would terminate long before reaching that point.

This forced us to rethink the entire training approach.

---

# Hardware Constraints (Colab Free Tier)

Understanding the hardware limits was critical.

### RAM

Google Colab provides approximately:

**12 GB of system RAM**

This RAM is shared between:

* Python runtime
* Dataset loading
* Model weights
* Training batches
* Optimizer states

Without careful optimization, the model easily exceeds this limit.

---

### CPU

Colab free tier typically provides:

* 2 virtual CPUs

This limits:

* Data loading speed
* preprocessing throughput
* training efficiency when running without GPU

Because of this, we had to **design the data pipeline carefully** to avoid CPU bottlenecks.

---

### GPU Availability

GPU access in Colab free tier is **not guaranteed**.

Possible GPUs include:

* T4
* P100
* Sometimes none

This unpredictability forced us to make the training pipeline **CPU compatible** and **memory efficient**.

---

# The Solution: Chunk-Based Training

To overcome the 12-hour runtime limitation, we redesigned our training pipeline.

Instead of attempting one long training run, we implemented a **chunk-based training strategy**.

The idea is simple:

Training is divided into **independent segments (chunks)**.

Each chunk:

1. Loads the last checkpoint
2. Trains for a fixed number of steps
3. Saves progress
4. Stops safely before the session limit

This allows training to **resume seamlessly** in the next Colab session.

### Advantages

This approach gives us several benefits:

* Training can continue across multiple sessions
* No progress is lost when Colab disconnects
* Hyperparameters can be adjusted between runs
* Model scaling becomes easier

This design effectively **removes the 12-hour barrier**.

---

# Model Architecture

Our current model is a **5M parameter transformer** trained using **character-level tokenization**.

Character tokenization keeps the system simple and allows the model to learn structure directly from raw text.

### Key Characteristics

* ~5,000,000 parameters
* Character-level tokenizer
* Transformer-based architecture
* Designed for low-memory environments

---

# Flexible Scaling

One of the major goals of this architecture is **flexibility**.

Because the training system is chunk-based, we can now safely experiment with larger model configurations such as:

* Increasing **filter size**
* Increasing **embedding dimension (`n_embed`)**
* Increasing **context block size**
* Increasing **training steps**

These changes no longer risk losing hours of progress due to session timeouts.

---

# Memory Optimization Strategy

To operate within the **12 GB RAM limit**, we optimized several aspects of the training pipeline.

### Techniques Used

**Small batch sizes**

Reducing batch size significantly lowers memory usage.

---

**Efficient tensor allocation**

Avoid unnecessary tensor copies and intermediate allocations.

---

**Checkpoint saving**

Model state is saved periodically to prevent progress loss.

Example logic:

```
if iter % checkpoint_interval == 0:
    save_checkpoint()
```

---

**Chunk-based dataset loading**

The dataset is processed in manageable segments to avoid loading the entire dataset into memory.

---

# Lessons Learned

This phase of the project taught us several important lessons.

### 1. Infrastructure matters as much as algorithms

A well-designed training system can be more important than the model itself.

---

### 2. Long training runs are fragile

Without checkpointing and restart mechanisms, training can fail easily.

---

### 3. Resource-aware engineering is essential

Designing models for **limited hardware** is a valuable engineering skill.

---

# Current Status

At this stage:

The model is successfully training with:

**~5 million parameters**

Using:

**character-level tokenization**

And a **robust chunk-based training pipeline** designed to work within the limitations of Google Colab.

---

# Next Steps

Our future goals include:

* Increasing model size beyond 5M parameters
* Improving training stability
* Expanding dataset size
* Implementing better evaluation metrics
* Exploring subword tokenization methods

---

# Final Thoughts

This milestone represents more than just a trained model.

It represents a **system that can continue to evolve**, even under strict hardware constraints.

Building machine learning systems under limitations forces creative engineering solutions.

And sometimes, those solutions become the most valuable part of the project.

---

*Thank you for following the journey.*
