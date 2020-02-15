import paramiko
import os
import sys


selection = int(input("The way you choose: "))

url = (input("The url you want download: "))

filename = url.split("/")[-1]

if selection == 1:
    cmd = 'git clone ' + url 
    filename_without_git = filename.split(".")[0]
    filename_plus_tar = filename_without_git + ".tar"
    print("服务器正在下载")
    
elif selection == 2:
    cmd = 'wget ' + url
    print("服务器正在下载")
else:
    print("wrong option!")



jssh = paramiko.SSHClient()

jssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

jssh.connect('149.248.3.160','22','root','G{x3oJmo[%RM)GGZ')



if selection == 1:
    stdin,stdout,stderr = jssh.exec_command(cmd)
    stdin,stdout,stderr = jssh.exec_command("tar -cvf " + filename_plus_tar + "  " +filename_without_git)
    stdin,stdout,stderr = jssh.exec_command("ffsend upload " + filename_plus_tar)
    
elif selection == 2:
    stdin,stdout,stderr = jssh.exec_command(cmd)
    stdin,stdout,stderr = jssh.exec_command("ffsend upload " + filename)


print(stdout.read())



