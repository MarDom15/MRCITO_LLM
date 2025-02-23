# LLM Project for MRC and its President - Cameroon 2025 Elections

## Description

This project offers a language model (LLM) capable of answering questions about the MRC (Movement for the Renaissance of Cameroon) and its president, particularly in the context of the upcoming elections in October 2025. The application uses the `LangChain` library to query a pre-created FAISS index and provide relevant answers to voters, supporters, and citizens about the MRC's information.

The goal of this project is to facilitate access to information for voters, providing instant and relevant answers to common questions about the MRC, its history, vision, and actions ahead of the elections.

## Features

- **Answers to questions**: The application answers all questions about the MRC and its president. This includes information on the party's history, recent actions, political positions, and more.
  
- **Based on an LLM model**: Uses a powerful language model based on OpenAI GPT-4 to understand and respond to complex questions.

- **Indexing and fast search**: Information is indexed with FAISS to allow for efficient and fast search within large volumes of textual data.

- **API with FastAPI**: The application exposes a REST API, enabling users to easily ask questions.

- **Android Application Deployment**: A lightweight Android application will be developed to allow users to interact easily with the LLM, providing a mobile-friendly interface for accessing information.

## Technologies

- **FastAPI**: Web framework for creating the REST API.
- **LangChain**: Python library for building question-answering chains using language models.
- **HuggingFace Embeddings**: Used to transform textual data into embeddings to facilitate search.
- **FAISS**: Library for indexing and fast searching of embeddings.
- **OpenAI GPT-4**: Language model used to generate precise and contextual answers.
- **Android (Kotlin/Flutter)**: The mobile application will be built using either Kotlin (native) or Flutter for cross-platform compatibility.

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
   ```

2. **Install dependencies**:
   Make sure you have `python` and `pip` installed, then install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the FAISS index**:
   - If you don't have a FAISS index yet, you need to create one by loading the relevant MRC data. This involves using `embeddings` to transform texts into vectors.
   - If you already have an index, place it in the appropriate directory.

4. **Run the FastAPI application**:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be accessible at `http://127.0.0.1:8000`.

## API Usage

The API exposes a single `GET` route to ask questions:

### Endpoint

```
GET /ask/?question=<your_question>
```

### Examples

#### Example 1:
Ask a question about the MRC:

```
GET http://127.0.0.1:8000/ask/?question=Who is the president of the MRC?
```

Response:
```json
{
  "response": "The president of the MRC is Maurice Kamto."
}
```

#### Example 2:
Ask a question about the 2025 elections:

```
GET http://127.0.0.1:8000/ask/?question=What are the MRC's positions for the 2025 elections?
```

Response:
```json
{
  "response": "The MRC advocates for free and transparent elections, and fights for social justice and democracy..."
}
```

## Android Application Deployment

A mobile application will be developed to ensure easy access to the LLM-based service. This app will:

- Provide a simple and intuitive user interface.
- Connect to the FastAPI backend via REST API.
- Enable users to input questions and receive responses instantly.
- Be lightweight and optimized for low-bandwidth environments.

## Contribution

If you'd like to contribute to this project, feel free to open issues or pull requests. All contributions are welcome!

## License

This project is ...........................................

