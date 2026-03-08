# BLOG 3 — Day Three of Training

## Training Progress Update

Today marks **Day Three** of the training process for our small transformer-based language model.

Since yesterday, the model has continued training steadily and has now reached **12,500 training steps**. This progress has taken **more than 24 hours of cumulative runtime**, spread across multiple sessions due to the **Google Colab session limitations** discussed earlier.

Despite these constraints, the chunk-based training system we implemented earlier is working reliably. The model can resume training from saved checkpoints without losing progress.

If everything continues running smoothly, the training process should **finish around 1:00 AM tomorrow**.

---

# Current Model Configuration

At this stage, the model being trained has approximately:

**~5 Million Parameters**

It uses:

* **Character-level ionization**
* **Transformer-based architecture**
* **English training data**

Because the model is trained only on **English text** and has a relatively small parameter count, it is important to set realistic expectations.

This model will **not be capable of solving complex reasoning problems** or performing advanced tasks like large commercial models.

However, it should still be able to:

* Generate simple text
* Continue sentences
* Answer small queries
* Demonstrate the behavior of a working language model

The primary goal here is **understanding and building the system**, not competing with large-scale models.

---

# Next Step: Building an Interface

Once the training process completes, the next step will be to design a **simple interface** to interact with the model.

This interface will allow us to:

* Input text prompts
* Generate model responses
* Observe how the character-level model behaves

The goal is to make the LLM **interactive**, allowing us to test its capabilities directly.

---

# Reflections on Model Size

While working on this project, I came across some fascinating research related to **efficient reasoning models**, particularly:

* **HRM**
* **TRM**

These approaches are extremely interesting because they challenge the traditional assumption that **bigger models are always better**.

Some of these systems use only around **27 million parameters**, yet they can outperform much larger models such as:

* Tiny GPT-2
* Some models with **125M – 300M parameters**

What makes them especially interesting is that they achieve this through **architectural innovations rather than simply scaling parameters**.

Even more surprising is that:

**TRM is roughly 3× smaller than HRM**, yet still achieves competitive performance.

This suggests that **model architecture and reasoning mechanisms may be just as important as model size**.

---

# Why This Matters for This Project

Although the model we are building right now is relatively small (~5M parameters), it serves as a **foundation for future experimentation**.

Understanding how to build, train, and interact with a language model from scratch opens the door to experimenting with more advanced architectures later.

Projects like HRM and TRM demonstrate that **innovation does not always require massive models**.

Sometimes the most interesting ideas come from **smarter architectures rather than larger parameter counts**.

---

# Looking Ahead

Once this training run completes, the next milestones will be:

1. Building an **interactive interface** for the model
2. Testing text generation quality
3. Analyzing model behavior
4. Exploring more efficient architectures

This project continues to evolve step by step, with each stage bringing new insights into how language models actually work.

---

*More updates will follow as soon as the training finishes.*
