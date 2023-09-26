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


@app.route("/mutiplication", methods=["POST"])
def multiplication():
=======


@app.route("/is_equal", methods=["POST"])
def IS_EQUAL(): 

    a = int(jsonObj["N1"])
    b = int(jsonObj["N2"])
    sum = a + b
    response = str(sum)  # "sum = " + str(sum)
    return response


# add your functions below


@app.route("/multiplication", methods=["POST"])
def multiplication(): 
>>>>>>> f895cb6ed3a2aa76e2648fcc34e20b09e4e7a80a
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
<<<<<<< HEAD
=======

>>>>>>> f895cb6ed3a2aa76e2648fcc34e20b09e4e7a80a
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
    if a == b:
    	response = "Equal"
    else:
    	response = "Not Equal"
    
    #response = "your_function"

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

>>>>>>> f895cb6ed3a2aa76e2648fcc34e20b09e4e7a80a
    return response

@app.route("/LOGICALAND", methods=["POST"])
def LOGICALAND(): 

<<<<<<< HEAD
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


=======
>>>>>>> f895cb6ed3a2aa76e2648fcc34e20b09e4e7a80a
if __name__ == "__main__":
    app.run()
