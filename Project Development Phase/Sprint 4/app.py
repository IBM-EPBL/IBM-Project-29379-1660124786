from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
warnings.filterwarnings('ignore')
from features import FeatureExtraction
import inputScript
import os
from os.path import join, dirname


import numpy as np
from flask import Flask, request, render_template,session, url_for,redirect,flash
import pickle

model = pickle.load(open('model.pkl','rb'))




app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/result", methods=["POST"])
def result():
    if request.method == "POST":

        url = request.form['url']
        checkprediction = inputScript.main(url)
        prediction = model.predict(checkprediction)
        print(prediction)
        output=prediction[0]
        if(output==1):
            msg="All is not lost all is never lost. Have a safe day exploring!!"
            flag=1
        else:
            msg="It's ok to lost sometimes. Find other sites to explore!!"
            flag=-1
        return render_template('result.html',msg=msg,url=url ,val=flag)
    


if __name__ == "__main__":
    app.run(debug=True,port=2002)
