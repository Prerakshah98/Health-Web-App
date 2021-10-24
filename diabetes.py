from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np
# from pandas.io.formats.format import float_format_type
from sklearn.preprocessing import MinMaxScaler
import pickle

app = Flask(__name__, template_folder='templates')
model=pickle.load(open("C:/Users/prera/Desktop/Project/Diabetes_API/diabetes_model.pkl","rb"))
@app.route("/")

@app.route("/diabetes")
def diabetes():
    return render_template("diabetes.html")

@app.route("/predict",methods=["POST"])
def predict():
    print("HELLO")
    # float_features = [float(x) for x in request.form.values()]
    # features = [np.array(float_features)]
    # prediction = model.predict(features)

    # if(int(prediction)==1):
    #     prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    # else:
    #     prediction = "No need to fear. You have no dangerous symptoms of the disease"
    # return(render_template("result.html", prediction_text=prediction))       
    if request.method == "POST":
        # to_predict_list = request.form
        # to_predict_list = list(to_predict_list.values())
        # to_predict_list = list(map(float, to_predict_list))
        float_features = [float(x) for x in request.form.values()]
        print(request.form.values())
        features = [np.array(float_features)]
        # sc = MinMaxScaler()
        # to_predict_list = sc.fit_transform(features)
        result = model.predict(features)
        print(result)
    
    if(result==1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return(render_template("result.html", prediction_text=prediction))       


# @app.route('/predict', methods = ["POST"])
# def predict():


if __name__ == "__main__":
    app.run(port=5000, debug=True)
