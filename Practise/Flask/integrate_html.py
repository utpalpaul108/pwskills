from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/submit',methods=['GET','POST'])
def submit():
    total_score=0
    if request.method == "POST":
        bangla = float(request.form['bangla'])
        english = float(request.form['english'])
        total_score = bangla + english
    elif request.method == "GET":
        bangla = float(request.args.get('bangla'))
        english = float(request.args.get('english'))
        total_score = bangla + english

    return render_template('result.html',total_marks=total_score)



if __name__ == '__main__':
    app.run(debug=True)
