from flask import Flask, request, jsonify
from flask_cors import CORS
from farmer_agent import ask_farmer_agent
from disease_detector import detect_disease
from database import save_conversation, get_conversations

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "AI Farmer Assistant is running!",
        "usage": "POST /ask with {question, city} or POST /detect-disease with image file"
    })

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')
    city = data.get('city', 'Tirupati')

    if not question:
        return jsonify({"error": "Please provide a question!"}), 400

    answer = ask_farmer_agent(question, city)
    
    # Save to database
    save_conversation(city, question, answer)
    
    return jsonify({
        "answer": answer,
        "city": city
    })

@app.route('/detect-disease', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({"error": "Please upload an image!"}), 400

    image_file = request.files['image']
    image_bytes = image_file.read()

    diagnosis = detect_disease(image_bytes)
    return jsonify({
        "diagnosis": diagnosis
    })

@app.route('/history', methods=['GET'])
def history():
    conversations = get_conversations(limit=20)
    return jsonify({
        "conversations": conversations
    })

if __name__ == '__main__':
    app.run(debug=True)