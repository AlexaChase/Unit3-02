lengthA = float(input("Please enter length A of the trapezoid:"))
if lengthA <=0:
    print("Error, number must be positive")
elif lengthA> 0:
    lengthB = float(input("Please enter length B of the trapezoid:"))
    if lengthB <= 0:
        print("Error, number must be positive")
    elif lengthB> 0:
        lengthH = float(input("Please enter the height of the trapezoid:"))
        if lengthH <= 0:
            print("Error, number must be positive")
        elif lengthH> 0:
            AreaTrapezoid= lengthH * (lengthA + lengthB) /2
        if AreaTrapezoid> 0:
            print("The area of the trapezoid:")
            print(AreaTrapezoid)
