import git
import os
import subprocess
import shutil 


# location 
#location = "D:\\MCC\\"
#dir = "hello-world"
# path 
#path = os.path.join(location, dir) 
    
# removing directory 
#shutil.rmtree(path) 


#Clone repo
git.Git("D:/MCC").clone("https://github.com/ChristianMedinaSusarrey/hello-world")

report = ''
for file in os.listdir("C:\\Users\\chris\\Desktop\\MCC\\Segundo Semestre\\Diseno\\Python\\hello-world"):
    if file.endswith(".py"):      
        print('*****************************************************************************************')  
        print('file to analyze: ' +  os.path.join("C:\\Users\\chris\\Desktop\\MCC\\Segundo Semestre\\Diseno\\Python\\hello-world", file))
        proc = subprocess.Popen('prospector ' + file, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = proc.communicate()        
        text = out.
        print(out)
        report = report + str(out)
        print('*****************************************************************************************')  
text_file = open("Output.txt", "w")
text_file.write(report)
text_file.close()
