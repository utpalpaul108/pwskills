from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return "Welcome to ABC Corporation"


@app.route('/')
def company_details():
    return '''
    <h1>Company Details</h1>
    <p><b>Company Name:</b> ABC Corporation</p>
    <p><b>Location:</b> India</p>
    <p><b>Contact Detail:</b> 999-999-9999</p>
    '''


if __name__ == '__main__':
    app.run(debug=True)
