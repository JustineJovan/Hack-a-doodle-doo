from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

app = Flask(__name__)
CORS(app)

with open("content.json", "r") as f:
  info = json.load(f)

@app.route("/ask", methods=["POST"])

def ask_bot():
  user_input = request.json.get("question","")

  info.append(user_input)
  vector = TfidfVectorizer()
  Matrix = vector.fit_transform(info)
  Similar_Matrix = cosine_similarity(Matrix[-1], Matrix)

  Similar_Matrix = Similar_Matrix.flatten()
  index = Similar_Matrix.argsort()[-2]
  answer = info[index] if Similar_Matrix[index] > 0.2 else "Sorry, I couldn't find an answer"

  info.pop()
  return jsonify({"answer": answer})

if __name__ == "__main__":
  app.run(port=5000)

