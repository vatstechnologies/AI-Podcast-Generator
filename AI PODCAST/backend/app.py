from flask import Flask, request, jsonify
from utils import generate_text, generate_audio, generate_summary

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to AI Podcast Generator API!"})

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    generated_text = generate_text(prompt)
    summary = generate_summary(generated_text)
    audio = generate_audio(summary)

    return jsonify({
        "generated_text": generated_text,
        "summary": summary,
        "audio_url": "Generated audio will be available here"
    })

if __name__ == "__main__":
    app.run(debug=True)

