with open('test.txt', mode="r") as my_file:
    print(my_file.readlines())
    
with open('smile.txt', mode="w") as my_file:
    text = my_file.write(":)") # sustituye todo

with open('smile.txt', mode="r+") as my_file:
    print(my_file.readlines())
    
with open('smile.txt', mode="a") as my_file:
    text = my_file.write("testing")
    