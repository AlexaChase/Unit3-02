lengthA = float(input("Please enter length A of the trapezoid:"))
lengthB = float(input("Please enter length B of the trapezoid:"))
lengthH = float(input("Please enter the height of the trapezoid:"))
AreaTrapezoid= lengthH * (lengthA + lengthB) /2
if lengthA <= 0:
    print("Error, number must be positive")
if lengthB <= 0:
    print("Error, number must be positive")
if lengthH <= 0:
    print("Error, number must be positive")
else:
    print("The area of the trapezoid:")
    print(AreaTrapezoid)
