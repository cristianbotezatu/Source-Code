#this line asks for a number in a new line showing "Input your first number" 
firstNumber = int(input("Input your first number\n"))

#this line asks for a number in a new line showing "Input your second number" 
secondNumber = int(input("Input your second number\n"))

#this line stores the sum of firstNumber and secondNumber variables in summationResult
summationResult = firstNumber + secondNumber

#this line prints the two inputted number along with the summation of these two numbers
print("The sum of {0} and {1} is {2}".format(firstNumber, secondNumber, summationResult))
