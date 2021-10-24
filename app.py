from flask import Flask, render_template
from flask import Flask, render_template, url_for, flash, redirect
from keras.models import load_model
from flask import request
import numpy as np
from sklearn.preprocessing import MinMaxScaler,StandardScaler
import pickle
app = Flask(__name__,template_folder='templates')

@app.route("/")
def main():
    return render_template("index.html")
@app.route("/heart")
def heart():
    return render_template("heart.html")
@app.route("/kidney")
def kidney():
    return render_template("kidney.html")
@app.route("/diabetes")
def diabetes():
    return render_template("diabetes.html")
@app.route("/liver")
def liver():
    return render_template("liver.html")
@app.route("/cancer")
def cancer():
    return render_template("cancer.html")

@app.route("/predict_diabetes",methods=["POST"])
def predict_diabetes():
    print("HELLO PREDICT DIABETES")  
    if request.method == "POST":
        model=pickle.load(open("C:/Users/prera/Desktop/FINALPROJECT/models/diabetes_model.pkl","rb"))
        float_features = [x for x in request.form.values()]
        float_features = float_features[:-1]
        float_features=np.array(float_features)
        # print("before",float_features)
        sc = MinMaxScaler()
        float_features = sc.fit_transform(float_features[:, np.newaxis]) 
        # print("after",float_features)
        float_features=float_features.reshape(1,-1)
        per = float(request.form["Percentage"])
        per=per/100
        print(per)
        result=model.predict_proba(float_features)[0][1]
        print(result)
        
    if(result>=per):
        result = result*100
        prediction_neg = f"Sorry you have {result:.2f}% chances of getting the disease. You need to consult the doctor immediately."
        return(render_template("diabetes.html", prediction_text_neg=prediction_neg))
    else:
        result = result*100
        prediction_pos = f"No need to fear. You have no dangerous symptoms of the disease. You only have {result:.2f}% chances of getting disease."
        return(render_template("diabetes.html", prediction_text_pos=prediction_pos))       


@app.route("/predict_liver",methods=["POST"])
def predict_liver():
    print("HELLO PREDICT LIVER")  
    if request.method == "POST":
        model=pickle.load(open("C:/Users/prera/Desktop/FINALPROJECT/models/liver_model.pkl","rb"))
        float_features = [x for x in request.form.values()]
        float_features = float_features[:-1]
        float_features=np.array(float_features)
        sc = MinMaxScaler()
        float_features = sc.fit_transform(float_features[:, np.newaxis]) 
        float_features=float_features.reshape(1,-1)
        per = float(request.form["Percentage"])
        per=per/100
        # features = [np.array(float_features)]
        print(float_features)
        print(per)
        result=model.predict_proba(float_features)[0][1]
        print(result)
    if(result>=per):
        result = result*100
        prediction_neg = f"Sorry you have {result:.2f}% chances of getting the disease. You need to consult the doctor immediately."
        return(render_template("liver.html", prediction_text_neg=prediction_neg))
    else:
        result = result*100
        prediction_pos = f"No need to fear. You have no dangerous symptoms of the disease. You only have {result:.2f}% chances of getting disease."
        return(render_template("liver.html", prediction_text_pos=prediction_pos))
         


@app.route("/predict_heart",methods=["POST"])
def predict_heart():
    print("HELLO PREDICT HEART")  
    if request.method == "POST":
        model=pickle.load(open("C:/Users/prera/Desktop/FinalProject/models/heart_model.pkl","rb"))
        float_features = [x for x in request.form.values()]
        print(float_features)
        float_features = float_features[:-1]
        float_features=np.array(float_features)
        print("before",float_features)
        sc = MinMaxScaler()
        float_features = sc.fit_transform(float_features[:, np.newaxis]) 
        print("after",float_features)
        float_features=float_features.reshape(1,-1)
        per = float(request.form["Percentage"])
        per=per/100
        # features = [np.array(float_features)]
        # print(float_features)
        print(per)
        result=model.predict_proba(float_features)[0][1]
        print(result)
    if(result>=per):
        result = result*100
        prediction_neg = f"Sorry you have {result:.2f}% chances of getting the disease. You need to consult the doctor immediately."
        return(render_template("heart.html", prediction_text_neg=prediction_neg))
    else:
        result = result*100
        prediction_pos = f"No need to fear. You have no dangerous symptoms of the disease. You only have {result:.2f}% chances of getting disease."
        return(render_template("heart.html", prediction_text_pos=prediction_pos))
               

@app.route("/predict_kidney",methods=["POST"])
def predict_kidney():
    print("HELLO PREDICT KIDNEY")  
    if request.method == "POST":
        model=pickle.load(open("C:/Users/prera/Desktop/FINALPROJECT/models/kidney_model.pkl","rb"))
        float_features = [x for x in request.form.values()]
        float_features = float_features[:-1]
        float_features=np.array(float_features)
        print("before",float_features)
        sc = MinMaxScaler()
        float_features = sc.fit_transform(float_features[:, np.newaxis]) 
        print("after",float_features)
        float_features=float_features.reshape(1,-1)
        per = float(request.form["Percentage"])
        per=per/100
        # features = [np.array(float_features)]
        # print(float_features)
        print(per)
        result=model.predict_proba(float_features)[0][1]
        print(result)
        if(result>=per):
            result = result*100
            prediction_neg = f"Sorry you have {result:.2f}% chances of getting the disease. You need to consult the doctor immediately."
            return(render_template("kidney.html", prediction_text_neg=prediction_neg))
        else:
            result = result*100
            prediction_pos = f"No need to fear. You have no dangerous symptoms of the disease. You only have {result:.2f}% chances of getting disease."
            return(render_template("kidney.html", prediction_text_pos=prediction_pos))
     

@app.route("/predict_cancer",methods=["POST"])
def predict_cancer():
    print("HELLO PREDICT CANCER")  
    if request.method == "POST":
        model=pickle.load(open("C:/Users/prera/Desktop/FINALPROJECT/models/cancer_model.pkl","rb"))
        # model = load_model('C:/Users/prera/Desktop/WEB APPLICATION/MAchinelearning/diabetes.h5')
        float_features = [x for x in request.form.values()]
        float_features = float_features[:-1]
        float_features=np.array(float_features)
        # print("before",float_features)
        sc = StandardScaler()
        float_features = sc.fit_transform(float_features[:, np.newaxis]) 
        # print("after",float_features)
        float_features=float_features.reshape(1,-1)
        per = float(request.form["Percentage"])
        per=per/100
        # features = [np.array(float_features)]
        # print(float_features)
        print(per)
        result=model.predict_proba(float_features)[0][1]
        print(result)

        if(result>=per):
            result = result*100
            prediction_neg = f"Sorry you have {result:.2f}% chances of getting the disease. You need to consult the doctor immediately."
            return(render_template("cancer.html", prediction_text_neg=prediction_neg))
        else:
            result = result*100
            prediction_pos = f"No need to fear. You have no dangerous symptoms of the disease. You only have {result:.2f}% chances of getting disease."
            return(render_template("cancer.html", prediction_text_pos=prediction_pos))


if __name__=="__main__":
    app.run(port=5000, debug=True)