# EternalBlue_SMB_check
Using this source you can find the EternalBlue_SMB vulnerable windows machines

Setup steps

1.Need to have a windows or ubuntu(any flavor of linux distro but i prefer ubuntu)

1.1. If windows just install wampp server or xampp server 

link:http://www.wampserver.com/en/

link:https://www.apachefriends.org/download.html

1.2 If you are using linux you need to install apache2,php,phpmyadmin and mysql

these below link can help you to install the above mentioned application in linux

https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-debian

https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu

https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-phpmyadmin-on-ubuntu-14-04

2.Now you need to import the database structure in server(windows/linux) which you can do using phpmyadmin (http://localhost/phpmyadmin) 

2.1.After login in to phpmyadmin web console click import and browse this project file and select ebs.sql and click GO.

3.If you are using windows xampp or wamp copy status.php and est.zip into web directory (C:\wamp64\www or C:\xampp\htdocs)
If you are using linux you need to place est.zip and status.php in /var/www/html.

4.Now choose a windows 7 32bit operation system to generate a agent file using report.py(single windows binary .exe).

4.1.https://www.python.org/downloads/ download python from here and install with full features which it will manage setting environment variables and etc.

4.2.open command prompt and type below commands

pip install pillow

pip install requests

pip install pyautogui

pip install wget

pip install pyinstaller

are you lazy like me use requirements.bat

4.3.goto https://www.microsoft.com/en-us/download/confirmation.aspx?id=44266 and download and install it

5.Open report.py and change "localhost" with server (windows/linux) IP at lines 26,61

6.Now goto windows 7 32bit machine and open command prompt and navigate to report.py directory

6.1.Pyinstaller report.py -w -F

6.2. After executing the above command you can see new directories,goto dist and you can see report.exe agent there and its ready now


7.Now in server open status.php(/var/www/html) and at line 6 please change the password(mysql password that you have given during the installation) for windows you can leave as it is but remember default configuration is most vulnerable and I recommend to set a password and change it as linux users do.

8.Now you are do with setup

9. Now ask you AD administrator to push the agent (6.2) via group policy to execute it while logon or lock time state.

If you organization has tool like symantec altiris or any other agent executors you can use it. 

10.Result are at phpmyadmin ebs database export it and see the results.
