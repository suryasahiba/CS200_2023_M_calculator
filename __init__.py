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

<<<<<<< HEAD
    a = int(jsonObj["N1"])
    b = int(jsonObj["N2"])
    sum = a + b
    response = str(sum)  # "sum = " + str(sum)
    return response


# add your functions below


@app.route("/multiplication", methods=["POST"])
def multiplication(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)

    a = int(jsonObj["N1"])
    b = int(jsonObj["N2"])
    # write code for your_function
    c = a * b
    c = str(c)
    response = c
    return response

@app.route("/bitwise-nor", methods=["POST"])
def BitwiseNor(): 
=======
@app.route("/Exponentiation", methods=["POST"])
def Exponentiation(): 
>>>>>>> 11e0342b41a85369ad80fb087ef77281dc9db939
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
<<<<<<< HEAD
    c=~(a| b)
    c=str(c)
    response = c
=======
    left= a << b
    response = str(left)                                #"sum = " + str(sum)
>>>>>>> 11e0342b41a85369ad80fb087ef77281dc9db939
    return response

@app.route("/LOGICALAND", methods=["POST"])
def LOGICALAND(): 

    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    ans= a and b
    response = "Logical AND is = " + str(ans)
    return response
    
@app.route("/isDiff", methods=["POST"])
def isDiff(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    # write code for your_function
    if a == b:
    	ans=0
    else:
    	ans=1
    response = str(ans)
    return response

@app.route("/modulus", methods=["POST"])
def MODULUS(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    mod=a%b
    response = str(mod)                                #"sum = " + str(sum)
    return response
if __name__ == "__main__":
    app.run()
