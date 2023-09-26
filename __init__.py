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


#Three Musketeers
@app.route("/bitwise_or", methods=["POST"])
def Bitwise_OR(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    bit_or=a|b
    response = str(bit_or)                            
    return response
	

@app.route("/mutiplication", methods=["POST"])
def multiplication(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    # write code for your_function
    c=a*b
    c=str(c)
    response = c
    return response

#function for finding the minimum of two number
@app.route("/Min", methods=["POST"])
def Min(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    
    if a < b:
        return str(a)
    else:
        return str(b)



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

@app.route("/modulus", methods=["POST"])
def MODULUS(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    mod=a%b
    response = str(mod)                                #"sum = " + str(sum)
    return response

if __name__== "__main__":
    app.run()
