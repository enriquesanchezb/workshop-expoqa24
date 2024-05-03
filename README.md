# Branch: 2-SpongeBob-LLM

Welcome to the 2-spongebob-llm branch of our AI Testing workshop! In this branch, you will learn how to install and run AI models using Ollama, and you will even create your own model inspired by SpongeBob.

## Installation

Follow these steps to set up your environment:

1. Install [Python 3.11](https://www.python.org/downloads/release/python-3119/)
2. Install [Poetry](https://python-poetry.org/) for Python using `pip3 install poetry` 
3. Install [Ollama](https://ollama.com/download) in your computer.
4. Download a [model](https://ollama.com/library) (Mistral, Llama2, Gemma...) using `ollama run <model>`

## How to use a model

To run a model with Ollama, use the following command:

```bash
ollama run <model>
```
Replace `<model_name>` with the name of the model you installed. Upon executing the command, a prompt will appear, allowing you to interact with the model. Initial loading might take some time depending on your computer's performance.

Example interaction:

```bash
ollama run mistral
>>> tell me a joke
 Of course! Here's a classic one for you:

Why don't scientists trust atoms?

Because they make up everything!

I hope that brought a smile to your face. Do you have any other questions or topics you'd like me to help with?

>>> 
```

Of course you can do it programmatically. Take a look to [`/basic_chat.py`](/basic_chat.py)

## How to create a simple new model

Ollama allows you to extend existing models using a Modelfile. Check the details here: `Modelfile`: https://github.com/ollama/ollama/blob/main/docs/modelfile.md.

Take a look to [`/Modelfile`](/Modelfile) and after that simply run:

```bash
ollama create spongebob -f Modelfile
ollama run spongebob
```

## Exercises

**Exercise1:**
Create and customize your own fun model. Start by modifying the Modelfile.

**Exercise 2:**
The script `/basic_chat.py` is not accurately mimicking SpongeBob's unique speaking style. Can you adjust it to better represent SpongeBob?

---

Enjoy creating and experimenting with your AI models!

---