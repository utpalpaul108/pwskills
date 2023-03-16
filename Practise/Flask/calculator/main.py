from flask import Flask, render_template, request, jsonify
import operator

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == "POST":
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

        result = ops[operation](num1, num2)

        return render_template('result.html', result=result)

    else:
        return render_template('index.html')


# For API
@app.route('/result-api', methods=['POST'])
def result_api():
    if request.method == "POST":
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

        result = ops[operation](num1, num2)

        return jsonify(f"Your result is :{result}")

    else:
        return jsonify('Something went wrong')


if __name__ == '__main__':
    app.run(debug=True)
