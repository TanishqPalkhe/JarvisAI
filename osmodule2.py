import os
# os.makedirs("yoo/opbhai")
with open("yoo/op.txt",'w') as f:
    f.write("hi")
with open("yoo/op1.txt",'w') as f:
    f.write("hi")
with open("yoo/op3.txt", 'w') as f:
    f.write("hi")
with open("yoo/op4.txt", 'w') as f:
    f.write("hi")


# def exe(path,file,extension):
#     os.chdir(path)
#     i=1
#     if file in path:
#         if os.path.splitext(file)[1] == extension:
#             os.rename(file,f"{i}.{extension}")
#             i+=1
# exe(r"C:\Users\hp\PycharmProjects\pythonProject\yoo",r"C:\Users\hp\PycharmProjects\pythonProject\yoo\op.txt",".txt")
# change the name of files in folder using os module
def exe(extension):
    i=1
    d=os.listdir("C:\\Users\\hp\\PycharmProjects\\pythonProject\\yoo")
    for items in d:
        d=os.path.join("yoo",items)
        y=os.path.join("yoo",f"R{i}.{extension}")
        os.rename(d,y)
        i+=1
exe("png")



# os.rename("yoo/op1.txt","yoo/tp6.txt")











