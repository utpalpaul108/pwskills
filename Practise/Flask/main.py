from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/submit", methods=["GET","POST"])
def submit():
    total_marks = 0
    marks = {}

    if request.method == 'POST':
        marks = {"math": int(request.form['math']), "english": int(request.form['english']),
                 "bangla": int(request.form['bangla'])}

        bangla = int(request.form['bangla'])
        english = int(request.form['english'])
        math = int(request.form['math'])

        total_marks = bangla + english + math

    if request.method == 'GET':
        marks = {"math": int(request.args.get('math')), "english": int(request.args.get('english')),
                 "bangla": int(request.args.get('bangla'))}

        bangla = int(request.args.get('bangla'))
        english = int(request.args.get('english'))
        math = int(request.args.get('math'))

        total_marks = bangla + english + math

    return render_template('about.html',title="About", total_marks=total_marks, marks=marks)


@app.route("/test-request")
def test_request():
    data = request.args.get('name')
    return f"<h2>Get From URL : {data}</h2>"


if __name__ == '__main__':
    app.run(debug=True)
