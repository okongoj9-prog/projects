try:
    file = open("file.txt" , "w")
    file.write("Hello From Python")
    file.close()
    print("file Created Successfully")
except:
    print("error creating")
    