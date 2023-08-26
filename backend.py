from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

history = []
def calculate(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return "Error"
@app.route('/')
def home():
    return render_template('index.html', endpoints=[
        "/history",
        "Following are the examples of operations:",
        "/5/plus/3",
        "/3/minus/5",
        "/3/minus/5/plus/8",
        "/3/into/5/plus/8/into/6"
    ])
@app.route('/<path:expression>')
def math_operation(expression):
    if "favicon.ico" in expression:
        return "Favicon request"
    expression = expression.replace(
        '/', ' ').replace('plus', '+').replace('minus', '-').replace('into', '*')
    result = calculate(expression)
    history.append({"question": expression, "answer": result})
    if len(history) > 20:
        history.pop(0)
    return jsonify({"question": expression, "answer": result})
@app.route('/history')
def operation_history():
    return jsonify(history)
if __name__ == '__main__':
    app.run(host='localhost', port=3000)
