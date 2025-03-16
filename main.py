from flask import Flask, request
import random
import requests

app = Flask(__name__)

# Flirty replies ka stock
flirty_replies = [
    "Aap hamesha itne cute lagte ho ya aaj kuch special hai? 😉",
    "Aapka naam Google hai kya? Kyunki mere saare answers aap hi ho! 😘",
    "Mujhe to laga tha angels sirf heaven me hote hain, par aap yahan kaise? 😍",
    "Aapki ek smile kaafi hai din banane ke liye! 🌟"
]

@app.route("/")
def home():
    return "Mohit Bot Active 😎"

# Bot ka main auto-reply setup
@app.route("/bot", methods=["POST"])
def bot_reply():
    data = request.get_json()
    user_message = data.get("message", "").lower()
    sender_name = data.get("name", "User")

    # Flirty reply ka magic ✨
    if "hi" in user_message or "hello" in user_message:
        return {"reply": f"Hello {sender_name}! Kya haal hai? 💖"}

    elif "kaise ho" in user_message:
        return {"reply": f"Main to full mast! Tum batao {sender_name}, aaj chand se zyada chamak rahe ho! 🌙"}

    else:
        return {"reply": random.choice(flirty_replies)}

if __name__ == "__main__":
    app.run(port=5000)
