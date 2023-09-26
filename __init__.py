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
@app.route("/antilog", methods=["POST"])
def antilog(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    antilog=math.pow(10,a)
    response = str(antilog)                                
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


if __name__== "__main__":
    app.run()
