from flask import Flask, request, jsonify
from customagents.HeuristicCheckAgent import HeuristicCheckAgent
from customagents.HeuristicReflectionAgent import HeuristicReflectionAgent
from customagents.HeuristicComparatorAgent import HeuristicComparatorAgent

app = Flask(__name__)

heuristic_check_agent = HeuristicCheckAgent()
heuristic_reflect_agent = HeuristicReflectionAgent()
heuristic_compare_agent = HeuristicComparatorAgent()

@app.route('/heuristic_check', methods=['POST'])
def heuristic_check():
    data = request.get_json()
    text = data.get('candidate_text')
    result = heuristic_check_agent.run(candidate_text=text)  # Replace with appropriate method call
    return jsonify(result=result)

@app.route('/heuristic_reflect', methods=['POST'])
def heuristic_reflect():
    data = request.get_json()
    text = data.get('candidate_text')
    result = heuristic_reflect_agent.run(candidate_text=text)  # Replace with appropriate method call
    return jsonify(result=result)

@app.route('/heuristic_compare', methods=['POST'])
def heuristic_compare():
    data = request.get_json()
    text = data.get('candidate_text')
    text2 = data.get('comparative_text')
    result = heuristic_compare_agent.run(candidate_text=text, comparative_text=text2)  # Replace with appropriate method call
    return jsonify(result=result)


if __name__ == '__main__':
    app.run()