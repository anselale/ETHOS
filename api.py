from flask import Flask, request, jsonify
from customagents.HeuristicCheckAgent import HeuristicCheckAgent

app = Flask(__name__)

heuristic_check_agent = HeuristicCheckAgent()


@app.route('/heuristic_check', methods=['POST'])
def heuristic_check():
    data = request.get_json()
    text = data.get('txt')
    result = heuristic_check_agent.run(txt=text)  # Replace with appropriate method call
    return jsonify(result=result)


if __name__ == '__main__':
    app.run()