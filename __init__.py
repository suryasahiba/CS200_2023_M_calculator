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

@app.route("/Bitwise AND", methods=["POST"])
def BITWISE_AND(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    # write code for your_function
    c=a&b
    c=str(c)
    response = c
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
	
@app.route("/rightshift", methods=["POST"])
def rightshift(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    number=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    c= str(number >> b)
    return c
    
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

    left= a << b
    response = str(left)                                #"sum = " + str(sum)

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
def shiftright(): 

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




    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])

    ans= a and b
    response = "Logical AND is = " + str(ans)
    return response



    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    ans= a and b
    response = "Logical AND is = " + str(ans)
    return response




    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    ans= a and b
    response = "Logical AND is = " + str(ans)
    return response

    #response = "your_function"

    c=~(a| b)
    c=str(c)
    response = c
    return response

    
@app.route("/right_shift", methods=["POST"])
def right_shift(number, shift_amount):
    return number >> shift_amount
while True:
    print("Select operation:")
    print("1. Right Shift")

    choice = input("Enter choice (1): ")

    if choice == '1':
        try:
            number = int(input("Enter the number: "))
            shift_amount = int(input("Enter the number of bits to shift: "))
            result = right_shift(number, shift_amount)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    else:
        print("Invalid choice. Please enter '1' for right shift.")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != "yes":
        break


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

    if a == b:
    	ans=0
    else:
    	ans=1
    response = str(ans)


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

@app.route("/antilog", methods=["POST"])
def antilog(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    antilog=math.pow(10,a)
    response = str(antilog)   
                                 
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


if __name__ == "__main__":

    app.run()
