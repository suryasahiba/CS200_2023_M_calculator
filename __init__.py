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
    a = int(jsonObj["N1"])
    b = int(jsonObj["N2"])
    sum = a + b
    response = str(sum)  # "sum = " + str(sum)
    return response


# add your functions below


@app.route("/mutiplication", methods=["POST"])
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
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    # write code for your_function

    c=~(a| b)
    c=str(c)
    response = c
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
    
    
 












 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 @app.route("/HCF", methods=["POST"])
def HCF():
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)

    a = int(jsonObj["N1"])
    b = int(jsonObj["N2"])
    # write code for your_function
   while b:
        a, b = b, a % b
  
    response = str(a)
    return response  


if __name__ == "__main__":
    app.run()
