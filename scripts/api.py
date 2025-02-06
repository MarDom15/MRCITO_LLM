from fastapi import FastAPI, HTTPException
from langchain.chains import RetrievalQA
#from langchain.llms import OpenAI
#from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import OpenAI
from langchain_community.vectorstores import FAISS


app = FastAPI()

# Charger l'index FAISS avec gestion d'erreur
try:
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("faiss_index", embeddings)
    print("✅ Index FAISS chargé avec succès.")
except Exception as e:
    raise RuntimeError(f"❌ Erreur lors du chargement de FAISS : {str(e)}")

# Configurer le modèle et la chaîne de question-réponse
llm = OpenAI(model_name="gpt-4")  # Remplacer par un modèle open-source si nécessaire
qa_chain = RetrievalQA(llm=llm, retriever=db.as_retriever())

@app.get("/ask/")
def ask(question: str):
    if not question.strip():
        raise HTTPException(status_code=400, detail="La question ne peut pas être vide.")

    try:
        response = qa_chain.run(question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors du traitement de la requête : {str(e)}")
