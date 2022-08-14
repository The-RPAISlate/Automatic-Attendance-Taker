
import os
import shutil

# def del_images():
folder_path = "TrainingImage"
dir_list = os.listdir(folder_path)
print(dir_list)

final_list=[]
for i in dir_list:
    final_list.append(i.split('_'))
    
# print(final_list)

delete_folder_name="TrainingImage/"

for i in final_list:
    if(i[0]=="6" and i[1]=="Sudhanwa"):
        delete_folder_name+=i[0] + "_" +i[1]

if(delete_folder_name=="6_Sudhanwa"):
    print("Hello")
print(delete_folder_name)
# shutil. rmtree(delete_folder_name) 

# def del_name_from_excel():
    

            
        