from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.base_url = os.getenv("OPENAI_API_BASE")


@app.route("/", methods=["GET"])
def main():
    return "Hello World"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message")
    response = openai.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是個有幫助的助手"},
            {"role": "user", "content": message}
        ]
    )
    return jsonify({"reply": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(debug = True)

