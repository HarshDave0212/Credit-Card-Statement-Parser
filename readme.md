## Credit Card Statement Parser:
This project allows users to chat with their credit card statements using Natural Language Processing (NLP).
It extracts text from uploaded PDF statements (from any bank), processes them using embeddings and a local language model, and enables users to query the data conversationally through a Streamlit interface.
________________________________________
## Overview:
This application reads your credit card statement PDFs, understands the transactions, and answers your questions such as:
•	“What was my highest transaction in July?”
•	“How much did I spend on Amazon?”
•	“What’s my total bill amount?”
•	“Show me my dining expenses.”
It’s a fully local setup — no API keys or external dependencies needed for LLM processing.
________________________________________
## How It Works:
1.	PDF Extraction:
The app reads uploaded PDFs using PyPDF2 and extracts all transaction text.
2.	Text Splitting:
The extracted text is split into manageable chunks using LangChain’s CharacterTextSplitter.
3.	Vector Embeddings:
Each chunk is converted into embeddings using HuggingFace Instruct Embeddings (hkunlp/instructor-base), enabling semantic understanding.
4.	FAISS Vector Store:
The embeddings are stored locally in a FAISS index, allowing fast similarity searches.
5.	Conversational Retrieval:
The app uses a Retrieval-Augmented Generation (RAG) pipeline powered by a local FLAN-T5 model to retrieve and respond to user questions.
6.	Interactive UI:
Streamlit provides a clean, chat-like interface styled via custom HTML templates (htmlTemplates.py).
________________________________________
## Github Link:
https://github.com/HarshDave0212/Credit-Card-Statement-Parser
________________________________________


## Tech Stack:

| Component                | Library / Tool                  | Purpose                                    |
| ------------------------ | ------------------------------- | ------------------------------------------ |
| **Frontend UI**          | `Streamlit`                     | Web app interface                          |
| **PDF Processing**       | `PyPDF2`                        | Extract text from PDF pages                |
| **Text Management**      | `LangChain`                     | Splitting, memory, and conversational flow |
| **Embeddings**           | `HuggingFaceInstructEmbeddings` | Semantic vectorization                     |
| **Vector Store**         | `FAISS`                         | Fast text similarity search                |
| **LLM (Local)**          | `google/flan-t5-small`          | Local text generation and reasoning        |
| **Transformers + Torch** | `transformers`, `torch`         | Model and pipeline execution               |

