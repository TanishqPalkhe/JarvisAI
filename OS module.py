import os
def soldier(path,file_dict,extension):
    os.chdir(path)
    i=1
    with open(file_dict,'r') as f:
        file1=f.read().split("\n")
        for contents in file1:
            da = contents.capitalize()
            if file_dict in path:
                with open(file_dict, 'a') as f:
                    f.write(da)

            if  os.path.splitext(file_dict)[1]==extension:
                os.rename(file_dict,f"{i}.{extension}")
                i+=1
soldier(r"C:\Users\hp\PycharmProjects\pythonProject",r"C:\Users\hp\PycharmProjects\pythonProject\this\barry.txt",".jpg")



