from wget import download
from os import system,popen,chdir,listdir,getcwd
from requests import post
from pyautogui import typewrite
from time import sleep
from zipfile import ZipFile
#wget to download programs
#os to execute few internal commands
#requests to post the data to server
#pyautogui is send a key stroke
#zipfile to extract zip file

#below is the code to change the dir
sourcepath=popen("echo %temp%").read().replace("\n","")
chdir(sourcepath)

#below is the code to create a temp bat file
batch1=open("mainfile.bat","w")
batch1.writelines("est.exe>vulns.txt\n")
batch1.writelines("exit\n")
batch2=open("mainexecute.bat","w")
batch2.writelines("start mainfile.bat\n")
batch1.close()
batch2.close()
#below code download the zip file from target url 'change the url'
download("http://localhost/est.zip")

#below code maps zip file downloaded above and unzip it
uzip=ZipFile('est.zip')
uzip.extractall()

#below code collect info of machine hostname,ip address,usernames
hostname=popen("hostname").read().replace("\n","")
chdir(r'C:\Users')
un=''
for i in listdir(getcwd()):
    un=un+"_"+i

un=un[1:]
chdir(sourcepath)
ip=popen('''ipconfig|findstr /i "ipv4"''').read().replace("\n","-").replace("   ","").replace(". . . . . . . . . . .","")
os=popen('''wmic os get Caption,CSDVersion /value|findstr /i "Caption"''').read().replace("Caption=","").replace("\r\n","")
#below code to run the batches
system("mainexecute.bat")
sleep(2)
typewrite("m")
sleep(2)
typewrite("m")

f=open("vulns.txt","r")
st=f.readlines()
f.close()
if "Your computer is safe, Microsoft security update is already installed.\n" in st:
    status="safe"
elif "Your computer is vulnerable !!!\n" in st:
    status="NOT safe"
else:
    status="pending"

#below code to post data to server
post("http://localhost/status.php",data={'hostname':hostname,'uname':un,'ip':ip,'os':os,'status':status})
