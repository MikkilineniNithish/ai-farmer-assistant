from flask import Flask, request, jsonify
from flask_cors import CORS
from farmer_agent import ask_farmer_agent

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "AI Farmer Assistant is running!",
        "usage": "POST /ask with {question, city}"
    })

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')
    city = data.get('city', 'Tirupati')

    if not question:
        return jsonify({"error": "Please provide a question!"}), 400

    answer = ask_farmer_agent(question, city)
    return jsonify({
        "answer": answer,
        "city": city
    })

if __name__ == '__main__':
    app.run(debug=True)