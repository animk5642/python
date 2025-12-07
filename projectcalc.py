while True:
    operand = input('Number 1:')
    try:
        operand = float(operand)
        break
    except:
        print("invalid")
   
while True:

      operand1 = input('Number 2:')
      try:
              operand1 = float(operand1)
              break
      except:
              print("invalid")

sign = input("sign")

if sign == "+":
      result = operand+operand1

elif sign == "-":
      result = operand-operand1
elif sign == "/":
      result = operand/operand1
elif sign == "*":
      result = operand*operand1
else:
      print("no operation")

print(result)
