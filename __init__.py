import json
from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")        

@app.route("/add", methods=["POST"])
def ADD(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    sum=a+b
    response = str(sum)                                #"sum = " + str(sum)
    return response
#add your functions below


@app.route("/Exponentiation", methods=["POST"])
def Exponentiation(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    value=a**b
    response = str(value) 
    return response
    
@app.route("/left_shift", methods=["POST"])
def left_shift(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    
    # write code for your_function
    left= a << b
    response = str(left)                                #"sum = " + str(sum)
    return response


#HashGuild- Logical OR

@app.route("/LOGICAL_OR", methods=["POST"])
def LOGICAL_OR():
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)

    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    # write code for your_function

    #logical=a|b
    #response=str(logical)
    response=str(a or b)

#Team BMS - Logarithmic
@app.route("/log", methods=["POST"])
def LOG(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=float(jsonObj['N1'])
    b=float(jsonObj['N2'])
    if b <= 0 or a <= 0:
            return "Invalid Input"
    logi = math.log(a, b)
    
    # write code for your_function
    response = str(logi)
    return response


if __name__== "__main__":
    app.run()
    
    
        
      
