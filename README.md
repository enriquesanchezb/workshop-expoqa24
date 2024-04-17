# Workshop instructions

## Installation

1. Install [Python 3.11](https://www.python.org/downloads/release/python-3119/)
2. Install [Poetry](https://python-poetry.org/) for Python using `pip3 install poetry` 
3. Install [Ollama](https://ollama.com/download) in your computer.
4. Download a [model](https://ollama.com/library) (Mistral, Llama2, Gemma...) using `ollama run <model>`

## How to use a model

To run a model using Ollama simply has to use this command

```bash
ollama run <model>
```

where `<model>` is what you installed in the step 4. Once you execute the command a new prompt has to appear and you can use it, don't worry if it takes some time, is your computer.

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

One of the funny things about Ollama is you can extend a model using `Modelfile`: https://github.com/ollama/ollama/blob/main/docs/modelfile.md.

Take a look to [`/Modelfile`](/Modelfile) and after that simply run:

```bash
ollama create spongebob -f Modelfile
ollama run spongebob
```

## Exercise 1

Have fun!! Change the Modelfile and create a funny model for you

## Exercise 2

`/basic_chat.py` is not acting as SpongeBob!!! Could you fix it?
