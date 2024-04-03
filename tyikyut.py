spisok = ["#","#","#","#","#","#","*","#","#","#","#","#","#"]
x = ""
c = 6

while x != "стоп":
    print()
    
    x = input("вправо или влево ")
    if x == "вправо":
        c += 1
        if c > 12:
            print("!!!!!!!!!!!так нельзя иди влево")
        else:
            spisok[c] = "*"
            spisok[c-1] = "#"
            #print(spisok)
            for i in spisok:
                print(i, end = "")
        
    if x  == "влево":
        c -= 1
        if c < 0:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!так нельзя иди вправо")
        else:
            spisok[c] = "*"
            spisok[c+1] = "#"
            #print(spisok)
            for i in spisok:
                print(i, end = "")
    




