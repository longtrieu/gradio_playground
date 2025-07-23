# IBM RAG and Agentic AI Professional Certificate - Course Materials

This GitHub repository contains the lab exercises, experiments, and assignments for the [IBM RAG and Agentic AI Professional Certificate](https://www.coursera.org/professional-certificates/ibm-rag-and-agentic-ai) course.

### Setting up your development environment

Set up a Python virtual environment

```  bash
pip install virtualenv
virtualenv my_env
source my_env/bin/activate
```

Install necessary libraries
- `gradio` allows you to build interactive web applications quickly, making your AI models accessible to users with ease.
- `ibm-watsonx-ai` for using LLMs from IBM's watsonx.ai.
- `langchain`, `langchain-ibm`, `langchain-community` for using relevant features from LangChain.
- `chromadb` for using the chroma database as a vector database.
- `pypdf` is required for loading PDF documents.

``` bash
# Installing necessary packages in my_env
python3.11 -m pip install \
gradio==4.44.0 \
ibm-watsonx-ai==1.1.2  \
langchain==0.2.11 \
langchain-community==0.2.10 \
langchain-ibm==0.1.11 \
chromadb==0.4.24 \
pypdf==4.3.1 \
pydantic==2.9.1
```

Deactivate virtual environment

``` bash
deactivate
```

Run the Gradio app:

``` bash
# QA Bot
python3.11 qabot.py

# Gradio demo
python3.11 gradio_demo.py

# Simple LLM
python3.11 simple_llm.py

# Common input types
python3.11 common_input_types.py
```