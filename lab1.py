while True:
    i = input()
    if i.upper() == "EXIT":
        break
    try:
        s = float(i)
        if 90 <= s <= 100: print("A")
        elif 75 <= s < 90: print("B")
        elif 60 <= s < 75: print("C")
        elif 40 <= s < 60: print("D")
        elif 0 <= s < 40: print("F")
    except: pass
