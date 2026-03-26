name = input("enter your name:")
file = open("names.csv","a")
file.write(f"{name}\n")
file.close()