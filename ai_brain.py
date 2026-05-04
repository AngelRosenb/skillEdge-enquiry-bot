from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

COURSES = {
    "python": "Python Programming — 5000 rupees, 2 months, placement available",
    "data science": "Data Science — 8000 rupees, 3 months, placement available",
    "web development": "Web Development — 7500 rupees, 3 months, placement available"
}

def get_ai_reply(user_message, user_data):
    msg = user_message.lower().strip()
    state = user_data.get("state", "")

    # -------------------------
    # STATE FLOW
    # -------------------------

    if state == "ask_name":
        if len(msg.split()) >= 2 and msg.replace(" ", "").isalpha():
            user_data["name"] = user_message
            user_data["state"] = "ask_phone"
            return "Nice to meet you! 😊\n\nPlease share your phone number."
        return "Please enter your full name (e.g. Rahul Kumar)."

    if state == "ask_phone":
        if msg.isdigit() and len(msg) == 10:
            user_data["phone"] = user_message
            user_data["state"] = "ask_qualification"
            return "Got it! 📞\n\nNow share your highest qualification."
        return "Please enter a valid 10-digit phone number."

    if state == "ask_qualification":
        user_data["qualification"] = user_message
        user_data["state"] = "done"
        return "🎉 You have been successfully registered!\n\nOur team will contact you soon."

    # -------------------------
    # NORMAL FLOW
    # -------------------------

    if msg in ["hi", "hello", "hey", "start"]:
        return "Hi! Welcome to SkillEdge Academy 👋\n\nHow can I help you today?"

    if "course" in msg:
        return (
            "Our courses:\n"
            "• Python Programming — 5000 rupees, 2 months\n"
            "• Data Science — 8000 rupees, 3 months\n"
            "• Web Development — 7500 rupees, 3 months\n\n"
            "All with placement assistance!\n\nWhich one interests you?"
        )

    for course, details in COURSES.items():
        if course in msg:
            return f"📚 {details}\n\nWould you like to enroll in this course?"

    if any(word in msg for word in ["enroll", "register", "join", "yes"]):
        user_data["state"] = "ask_name"
        return "Great! Let's get you enrolled 🎉\n\nPlease share your full name first."

    if "fee" in msg or "cost" in msg:
        return "Fees:\n• Python — 5000\n• Data Science — 8000\n• Web Development — 7500"

    if "address" in msg or "location" in msg:
        return "📍 MG Road, Thrissur\n📞 9876543210"

    if msg in ["ok", "thanks", "bye", "no"]:
        return "Thank you for contacting SkillEdge Academy 😊"

    # -------------------------
    # GROQ (OFF-TOPIC)
    # -------------------------

    off_topic = ["what is", "who is", "why", "weather", "cricket", "movie", "news"]

    if any(word in msg for word in off_topic):
        try:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": user_message}],
                model="llama3-8b-8192"
            )
            return response.choices[0].message.content
        except:
            return "Sorry, I couldn't process that right now."

    return "Type 'courses' to explore or 'enroll' to register."
