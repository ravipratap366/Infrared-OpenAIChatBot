import random
import pyttsx3
import time
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)

def read_responses_from_file(filename):
    responses = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if "::" in line:
                question, answer = line.split("::", 1)
                responses[question.lower()] = answer
    return responses

def get_response(user_input, responses, conversations, confidence_level=0.95):
    user_input = user_input.lower()

    # Add the user input to the conversations dictionary
    conversations[user_input] = None

    response = responses.get(user_input)
    if not response:
        # Calculate cosine similarity between user input and all known questions
        vectorizer = CountVectorizer().fit_transform([user_input] + list(responses.keys()))
        vectors = vectorizer.toarray()
        similarity_scores = cosine_similarity(vectors)

        # Filter out similarity scores below the confidence level
        similar_questions_indices = np.argwhere(similarity_scores[0, 1:] > confidence_level).flatten()

        # If there are similar questions above the confidence level, choose one randomly
        if len(similar_questions_indices) > 0:
            most_similar_index = random.choice(similar_questions_indices)
            print(most_similar_index)
            most_similar_question = list(responses.keys())[most_similar_index]
            response = responses.get(most_similar_question)
            conversations[user_input] = most_similar_question  # Store the most similar question in the conversations dictionary
        else:
            response = "Sorry, I don't have information regarding that....😢"

    return response

def speak(message, voice="default"):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if voice == "male":
        engine.setProperty('voice', voices[0].id)
    elif voice == "female":
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)  # Default to male voice

    engine.say(message)
    engine.runAndWait()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["user_input"]
    voice = request.form.get("voice", "male")  # Get the voice parameter from the form
    if user_input.lower() in ["exit", "bye", "quit"]:
        response = "Goodbye! Have a great day!"
        speak(response, voice)
    else:
        response = "Chatbot is processing your request. Please wait..."
        # time.sleep(1.1)  # Add a 2-second delay for demonstration purposes
        response = get_response(user_input, responses, conversations)
        speak(response, voice)

    return {"response": response}

if __name__ == "__main__":
    responses = read_responses_from_file("qa_data.txt")
    conversations = {}
    print("Chatbot: Hello! How can I assist you?")
    app.run()