from flask import Flask, request, render_template
import pickle
application = Flask(__name__)
app = application

standard_scaler = pickle.load(open('model/standardScaler.pkl','rb'))
model = pickle.load(open('model/logisticRegression.pkl','rb'))

@app.route('/',methods=['GET','POST'])
def predict_datapoint():
   if request.method == 'POST':
      Pregnancies = int(request.form.get('Pregnancies'))
      Glucose = float(request.form.get('Glucose'))
      BloodPressure = float(request.form.get('BloodPressure'))
      SkinThickness = float(request.form.get('SkinThickness'))
      Insulin = float(request.form.get('Insulin'))
      BMI = float(request.form.get('BMI'))
      DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
      Age = float(request.form.get('Age'))

      scaled_data = standard_scaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
      predicted_result = model.predict(scaled_data)

      result = 'Non-Diabetic'
      if predicted_result[0] == 1:
         result = 'Diabetic'
      return render_template('home.html',title="Logistic Regression", result=result)
   else:
      return render_template('home.html', title="Logistic Regression")

if __name__ == '__main__':
   app.run()
