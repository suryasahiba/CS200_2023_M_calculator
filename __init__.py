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

@app.route("/shiftright", methods=["POST"])
def Shiftright(): 

    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=float(jsonObj['N1'])
    b=int(jsonObj['N2'])
    value=a/(10 ** b)

    # write code for your_function


    response =str(value)
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
