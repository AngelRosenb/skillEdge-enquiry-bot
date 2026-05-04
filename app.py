from flask import Flask, request, jsonify, render_template
from ai_brain import get_ai_reply
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    
    reply = get_ai_reply(user_message)
    
    return jsonify({"reply": reply})

@app.route("/enroll", methods=["POST"])
def enroll():
    data = request.get_json()
    
    lead = {
        "name": data.get("name"),
        "phone": data.get("phone"),
        "qualification": data.get("qualification"),
        "course": data.get("course")
    }
    
    with open("leads.json", "r") as f:
        leads = json.load(f)
    
    leads.append(lead)
    
    with open("leads.json", "w") as f:
        json.dump(leads, f, indent=2)
    
    return jsonify({"status": "saved"})

if __name__ == "__main__":
    print("Starting SkillEdge Enquiry Bot...")
    app.run(debug=True)