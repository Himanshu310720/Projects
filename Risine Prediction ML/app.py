from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('Gradient_Boost.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('index1.html')


@app.route('/predict', methods=['POST','GET'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    arr = np.array([[data1, data2 ,data3, data4 , data5, data6, data7]])
    pred = model.predict(arr)
    if pred == 0 :
        return render_template('home1.html',pred="Kecimen")
    else :
        return render_template('home1.html',pred="Besni")


if __name__ == "__main__":
    app.run(debug = True)















