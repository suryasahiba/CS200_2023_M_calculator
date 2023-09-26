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
@app.route("/reporiots", methods=["POST"])
def Reporiots(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    number = float(jsonObj['N1'])
    n = float(jsonObj['N2'])

    print(number)
    print(n)
    
    result = math.pow(number, 1/n)  # Calculate the nth root using math.pow
    print(result)
    response = str(result)
    return response
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



if __name__== "__main__":
    app.run()
