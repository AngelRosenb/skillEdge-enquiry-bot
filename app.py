from flask import Flask, request, jsonify, render_template
from ai_brain import get_ai_reply
import json
import os

app = Flask(__name__)

# temporary memory (single user demo)
user_data = {}


# -----------------------------
# SAVE FUNCTION
# -----------------------------
def save_to_json(data):
    # create file if not exists
    if not os.path.exists("leads.json"):
        with open("leads.json", "w") as f:
            json.dump([], f)

    # read existing data safely
    try:
        with open("leads.json", "r") as f:
            leads = json.load(f)
    except:
        leads = []

    # append new lead
    leads.append(data)

    # write back
    with open("leads.json", "w") as f:
        json.dump(leads, f, indent=4)


# -----------------------------
# ROUTES
# -----------------------------
@app.route("/")
def home():
    return render_template("chat.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    reply = get_ai_reply(user_message, user_data)

    # ✅ SAVE DATA WHEN FLOW COMPLETES
    if user_data.get("state") == "done":
        save_to_json({
            "name": user_data.get("name"),
            "phone": user_data.get("phone"),
            "qualification": user_data.get("qualification")
        })

        # reset for next user
        user_data.clear()

    return jsonify({"reply": reply})


# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    print("Starting SkillEdge Enquiry Bot...")
    app.run(debug=True)
