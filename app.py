import pickle
from flask import Flask,render_template,request,jsonify,app,url_for
import numpy as np
import pandas as pd

app=Flask(__name__)
#Load th model and scaling pickle files 
regmodel=pickle.load(open('regmodel.pkl','rb'))
scaling=pickle.load(open('scaling.pkl','rb'))

#Determining the root paths and their functions
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=["POST"])
def predict_api():
    data=request.json['data']   #this received data will be in the form of key:value pair
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))   #resized so that it can creates a single datapoint record 
    new_data=scaling.transform(np.array(list(data.values())).reshape(1,-1))
    print(new_data)
    output=regmodel.predict(new_data)
    print(output[0])  #since output will be a 2D array
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    #data=np.array(data).reshape(1,-1)
    final_input=scaling.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)[0] 
    return render_template("home.html",prediction_text="The House Price Prediction is {}".format(output))

if (__name__=="__main__"):
    app.run(debug=True)

