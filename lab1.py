import sys
#Handling the case where we have to EXIT the program
for line in sys.stdin:
    i = line.strip()
    if i.upper() == "EXIT":
        break
    try:
    #Taking marks as an Input to Calculate Grades 
        s = float(i)
        if 0 <= s <= 100:
            if 90 <= s <= 100:
                print("A")
            elif 75 <= s < 90:
                print("B")
            elif 60 <= s < 75:
                print("C")
            elif 40 <= s < 60:
                print("D")
            else:
                print("F")
        else:
         # Handling the case of Invalid Input 
            print("Invalid Input")
    except:
        print("Invalid Input")
