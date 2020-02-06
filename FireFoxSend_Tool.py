import paramiko
import os
import sys

print("""
______ _         ______        
|  ___(_)        |  ___|       
| |_   _ _ __ ___| |_ _____  __
|  _| | | '__/ _ \  _/ _ \ \/ /
| |   | | | |  __/ || (_) >  < 
\_|   |_|_|  \___\_| \___/_/\_\\
 _____                _        
/  ___|              | |       
\ `--.  ___ _ __   __| |       
 `--. \/ _ \ '_ \ / _` |       
/\__/ /  __/ | | | (_| |       
\____/ \___|_| |_|\__,_|       
                               
                               
>>>>>> press 1  git clone
>>>>>> press 2  wget
""")

selection = int(input("The way you choose: "))

url = (input("The url you want download: "))

filename = url.split("/")[-1]

if selection == 1:
    cmd = 'git clone ' + url 
    filename_without_git = filename.split(".")[0]

    print("服务器正在下载")
    
elif selection == 2:
    cmd = 'wget ' + url
    print("服务器正在下载")
else:
    print("wrong option!")


filename_plus_tar = filename_without_git + ".tar"

jssh = paramiko.SSHClient()

jssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

jssh.connect('IP','22','username','password')



if selection == 1:
    stdin,stdout,stderr = jssh.exec_command(cmd)
    stdin,stdout,stderr = jssh.exec_command("tar -cvf " + filename_plus_tar + "filename")
    stdin,stdout,stderr = jssh.exec_command("ffsend upload " + filename_plus_tar)
    
elif selection == 2:
    stdin,stdout,stderr = jssh.exec_command(cmd)
    stdin,stdout,stderr = jssh.exec_command("ffsend upload " + filename)


print(stdout.read())
