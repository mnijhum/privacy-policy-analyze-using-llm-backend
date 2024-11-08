from flask import Flask, request, jsonify
from model.analyzeWithLlama import send_url_to_llama

app = Flask(__name__)


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    policy_url = data['policyText']
    result = send_url_to_llama(policy_url)
    return jsonify({"analysis": result})


if __name__ == '__main__':
    app.run(port=5000)
