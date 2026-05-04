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

def get_ai_reply(user_message):
    msg = user_message.lower().strip()

    # Greeting
    if msg in ["hi", "hello", "hey", "start", "hii", "helo"]:
        return "Hi! Welcome to SkillEdge Academy 👋\n\nHow can I help you today?"

    # Enroll
    if any(word in msg for word in ["enroll", "register", "join", "admission", "yes"]):
        return "Great! Let's get you enrolled 🎉\n\nPlease share your full name first."

    # Want to learn
    if any(word in msg for word in ["learn", "skill", "study", "interested", "want to"]):
        return "That's great! 🌟 We have courses in:\n• Python Programming\n• Data Science\n• Web Development\n\nType any course name to know more!"

    # Course list
    if any(word in msg for word in ["course", "courses", "list", "available", "options", "offer"]):
        return "Our courses:\n• Python Programming — 5000 rupees, 2 months\n• Data Science — 8000 rupees, 3 months\n• Web Development — 7500 rupees, 3 months\n\nAll with placement assistance!\n\nWhich one interests you?"
    # Web development
    if "web" in msg:
        return "📚 Web Development — 7500 rupees, 3 months, placement available\n\nWould you like to enroll in this course?"
    # Data science
    if "data" in msg:
        return "📚 Data Science — 8000 rupees, 3 months, placement available\n\nWould you like to enroll in this course?"

    # Specific course
    for course, details in COURSES.items():
        if course in msg:
            return f"📚 {details}\n\nWould you like to enroll in this course?"

    # Consultant or call
    if any(word in msg for word in ["consultant", "call", "talk", "contact", "speak"]):
        return "Please share your phone number and our team will call you within 24 hours 📞"

    # Address
    if any(word in msg for word in ["address", "office", "location", "visit", "where"]):
        return "📍 Visit us at MG Road, Thrissur\n📞 Call us at 9876543210"

    # Placement
    if any(word in msg for word in ["placement", "job", "career", "hired"]):
        return "Yes! All our courses come with placement assistance. 85% of students get placed within 3 months ✅"

    # Fees
    if any(word in msg for word in ["fee", "cost", "price", "rupees", "how much"]):
        return "Our fees:\n• Python — 5000 rupees\n• Data Science — 8000 rupees\n• Web Development — 7500 rupees\n\nEMI options available!"

    # Off-topic
    off_topic = ["what is", "who is", "why is", "how is", "when is", "weather",
                 "cricket", "football", "movie", "politics", "news", "sport",
                 "game", "food", "recipe", "wather"]
    if any(word in msg for word in off_topic):
        return "I can only help with course enquiries 😊\n\nType 'courses' to see what we offer or 'enroll' to register."

    # Qualification detection
    qualifications = ["btech", "bsc", "mtech", "msc", "mba", "diploma",
                      "12th", "10th", "12", "10", "plus two", "degree", 
                      "graduate", "engineering", "plustwo", "hse", "sslc"]
    if any(word in msg for word in qualifications):
        return "Got it! ✅ Our team will follow up with you shortly.\n\nAnything else? "
    ignore = ["nothing", "ok", "okay", "thanks", "thank you", "bye", "no","no thanks", "nope"]
    if msg in ignore:
        return "Thank you for contacting SkillEdge Academy! 😊\n\nFeel free to reach out anytime. "
    # Name detection
    if len(msg.split()) <= 4 and msg.replace(" ", "").isalpha():
        return "Nice to meet you! 😊\n\nPlease share your phone number so we can contact you."

    # Phone number detection
    if any(char.isdigit() for char in msg) and len(msg.replace(" ", "")) >= 8:
        return "Got it! 📞\n\nLastly, please share your highest qualification (e.g. 12th, Diploma, B.Tech)"

    # Default
    return "Got it! ✅ Our team will follow up with you shortly.\n\nAnything else? Type 'courses' to explore or 'enroll' to register."