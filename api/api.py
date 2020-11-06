import logging


from flask import Flask, request, jsonify
from flask_cors import CORS

from answers import AnswerScoring
from question_generator import QuestionGenerator

app = Flask(__name__)
CORS(app)


@app.route("/questions", methods=['POST'])
def predict():
    data = []
    try:
        for doc in request.json["document"]:
            q = QuestionGenerator()
            question_list = q.generate_question(doc, "Wh")
            data.append({"answer": doc, "questions": question_list})
        return jsonify(data)
    except Exception as e:
        return jsonify({"result": "Model Failed"})


@app.route("/answers", methods=["POST"])
def compare():
    marking_answer = request.json["marking_answer"]
    logging.info(request.json)
    student_answer = request.json["student_answer"]
    scorer = AnswerScoring(marking_answer, student_answer)
    return jsonify({"score": scorer.score})


if __name__ == "__main__":
    app.run('0.0.0.0', port=8001)
