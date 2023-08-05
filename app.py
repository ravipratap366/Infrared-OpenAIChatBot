from flask import Flask, render_template, request, jsonify
import os
import pickle
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQAWithSourcesChain
from langchain import OpenAI
import requests
import config

app = Flask(__name__)

# Load Langchain model and vector store
# this is for git check


os.environ["OPENAI_API_KEY"] = config.OPENAI_API_KEY

urls = [
    "https://64c88d1e986e8d39abdf0ffc--merry-choux-c76385.netlify.app/",
    'https://machinelearningmastery.com/blog/',
    'https://www.bmc.com/blogs/machine-learning-anomaly-detection/'
]

loaders = UnstructuredURLLoader(urls=urls)
data = loaders.load()

text_splitter = CharacterTextSplitter(separator='\n', chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(data)

with open("final_openai.pkl", "rb") as f:
    vectorStore = pickle.load(f)

llm = OpenAI(temperature=0, model_name='text-davinci-003')
chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorStore.as_retriever())

@app.route('/static/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()  # Use request.get_json() to parse JSON data
    if data and 'input' in data:
        input_question = data['input']
        response = chain({"question": input_question}, return_only_outputs=True)
        answer = response['answer']
        sources = response['sources']
        return jsonify({'answer': answer, 'sources': sources})
    else:
        return jsonify({'error': 'Invalid input format'}), 400

if __name__ == '__main__':
    app.run(debug=True)
