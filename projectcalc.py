def geta_number(number):
    while True:

        operand = input("Number "+str(number))
        try:
            vslue = float(operand)
            return vslue
        except:
            print("invalid")


operand = geta_number(1)
operand1 = geta_number(2)
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
