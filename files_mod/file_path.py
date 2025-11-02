# relative
with open('files_folder/relative.txt', mode="r") as my_file:
    print(my_file.readlines())
    
# absolute
with open('C:/Users/gushi/OneDrive/Documentos/projects/100daysOfPython/files/roadmap.md', mode="r", encoding="utf-8") as my_f:
    print(my_f.readlines())