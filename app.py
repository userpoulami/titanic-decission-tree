from flask import Flask, render_template, request
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__)#initializing a flask app

@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/report.html',methods=['GET'])  # route to display the home page
@cross_origin()
def report():
    return render_template("report.html")


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():

    if request.method == 'POST':
        try:
            is_Pclass = request.form['Pclass']
            if(is_Pclass=="1"):
                pclass=1
            elif (is_Pclass=="2"):
                pclass=2
            else:
                pclass=3
            Age = float(request.form['Age'])
            SibSp=int(request.form["SibSp"])
            Parch=int(request.form["Parch"])
            Fare=float(request.form["Fare"])
            is_sex=request.form["Sex"]
            if(is_sex=="1"):
                sex=1
            else :
                sex=0
            filename="model.pickle"
            loaded_model = pickle.load(open(filename, 'rb'))
            prediction=loaded_model.predict([[pclass,Age,SibSp,Parch,Fare,sex]])
            print('prediction is', prediction)   
            return render_template('result.html',prediction=prediction) 
        except Exception as e:
            print('The Exception message is: ',e)

                
        
    else:
        return render_template('index.html')   
    
        
if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # 