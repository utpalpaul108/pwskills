from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return "Home Page"


@app.route('/pass/<int:score>')
def success(score):
    return f"You successfully PASSED. Your score is <b>{score}</b>"


@app.route('/fail/<int:score>')
def fail(score):
    return f"You FAILED to PASS the Exam. Your score is {score}"


@app.route('/result/<int:score>')
def result(score):

    if score >= 50:
        result = 'success'
    else:
        result = 'fail'

    return redirect(url_for(result,score=score))


if __name__ == '__main__':
    app.run(debug=True)
