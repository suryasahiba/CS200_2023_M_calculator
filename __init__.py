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


@app.route("/div", methods=["POST"])
def div(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    
    if b != 0:
        div_result = a / b
        response = str(div_result)
    else:
        response = "Division by zero is not allowed."

    return response
    
    
#TechnoSync Is Equal   
@app.route("/is_equal", methods=["POST"])
def IS_EQUAL(): 

	jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])

    
    
    if a == b:
    	response = "Equal"
    else:
    	response = "Not Equal"
          
    return response


@app.route("/LOGICALAND", methods=["POST"])
def LOGICALAND(): 



    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])

    
    
    if a == b:
    	response = "Equal"
    else:
    	response = "Not Equal"
          
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

    return response

    ans= a and b
    response = "Logical AND is = " + str(ans)
    return response
    
    
 
#Breaking branches rocks
@app.route("/bnand", methods=["POST"])
def bnand():
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)

    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    # write code for your_function

    #logical=a|b
    #response=str(logical)
    response=str(not(a and b))

    return response


@app.route("/xor", methods=["POST"])
def xor(): 

    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    value=a^b
    response = str(value) 
    return response
    
    
@app.route("/left_dec", methods=["POST"])
def left_dec(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    left=a/(10**b)
    response = str(left)                                #NightConquerors
    return response









 
 
 
 
 
 
 
 
 
 
 
 
 @app.route("/bnand", methods=["POST"])
def BNAND():
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    a = int(jsonObj["N1"])
    b = int(jsonObj["N2"])
    bnand=~(a&b)
    response = str(bnand)  # "sum = " + str(sum)
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
    
@app.route("/MAX", methods=["POST"])
def MAX(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    # write code for your_function
    if a > b:
        MAX = a
    else:
        MAX = b
    response = str(MAX)
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
@app.route("/leftshift", methods=["POST"])
def leftshift(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    leftshift = a<<b
    # write code for your_function
    response = str(leftshift)
    return response




if __name__ == "__main__":
    app.run()
