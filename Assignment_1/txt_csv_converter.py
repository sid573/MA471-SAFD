def convert():
    f = open("data.txt","r")
    fl = 0
    s = ""
    for i in f.read():
        if i != " " and i != "\n":
            s = s+i
            fl = 1
        elif i == " " and fl==1:
            s = s+","
            fl = 0
        elif i == "\n":
            s = s+"\n"
    return s
    
f = open("mod_data.csv", "w")
f.write(convert())
f.close()