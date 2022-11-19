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

file = open("model.pkl","rb")
gbc = pickle.load(file)
file.close()

@app.route("/result", methods=["POST"])
def result():
    if request.method == "POST":

        url = request.form["url"]
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1,30) 

        y_pred =gbc.predict(x)[0]
        #1 is safe       
        #-1 is unsafe
        y_pro_phishing = gbc.predict_proba(x)[0,0]
        y_pro_non_phishing = gbc.predict_proba(x)[0,1]
        # if(y_pred ==1 ):
        xx =round(y_pro_non_phishing)

        if(y_pred==0):
            msg="All is not lost all is never lost. Have a safe day exploring!!"
            flag=1
            
        else:
            msg="It's ok to lost sometimes. Find other sites to explore!!"
            flag=-1
        return render_template('result.html',msg=msg,url=url ,val=flag)

if __name__ == "__main__":
    app.run(debug=True,port=2002)
