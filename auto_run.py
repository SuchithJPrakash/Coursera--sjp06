import paramiko
import sys
import time
import pywinauto 
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from datetime import datetime
import argparse

f=open(r"C:\Users\1000295835\Downloads\Oakgate_as_is.txt")
g=open(r"C:\Users\1000295835\Downloads\controller_features_testcases.txt")

fr=f.readlines()
gr=g.readlines()

for i in range(len(fr)):
    fr[i]=fr[i].strip("\n").strip()

for i in range(len(gr)):
    gr[i]=gr[i].strip("\n").strip()

print(fr)

f.close()
g.close()
l=[]

for script in gr:
    l.append("python startTest.py -targetname OGT-WD-INDIA-3UG4-72 -chassis 1 -slot 1 -script '"+script+"' -test_blocksize 512  -dt\n")
    l.append("sleep 1m\n")


s=open(r"C:\Users\1000295835\Documents\controller_features_logs\sample.sh","w")
s.writelines(l)
s.close()
    
'''
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
host_name="10.207.193.161"
download_path="C:/Users/1000295835/Downloads/" #Change path according to your downloads location

try:
    client.connect(hostname=host_name, username="root", password="!Nvm@WD$")
    sftp = client.open_sftp()
    print("Connection:Success",host_name)
except:
    print("Connection timeout")
    sys.exit()

ogt_name="OGT-WD-INDIA-3UG4-72"
chassis="1"
slot="0"

conn = client.invoke_shell() 
conn.send("cd ..\n") 
conn.send("cd star\n") 
conn.send("cd fwqa_framework\n") 
time.sleep(5)
f=open("controller_features_testcases.txt","r")
l=f.readlines()
for i in range(len(l)):
    l[i]=l[i].strip("\n").strip("\t")
print(l)

block_list=["4096","4096"]
for block_size in block_list:
    print("Block size",block_size)
    for script in l:

        print("Executing ",script)
        conn.send("python startTest.py -targetname "+ogt_name+" -chassis "+chassis+" -slot "+slot+" -script "+script+" -test_blocksize "+block_size+" -dt\n")
        time.sleep(60)
        tf=conn.recv(9999).decode("ascii")
        print(tf)
        if "Could not rescan slot with UID" in tf:
            conn.send("python startTest.py -targetname "+ogt_name+" -chassis "+chassis+" -slot "+slot+" -script "+script+" -test_blocksize "+block_size+" -dt\n")

        file_name=""
        count=0
        wait_count=240
        flag=False

        while count<wait_count:

            if(conn.recv_ready()): 
                file=conn.recv(9999).decode("ascii")
                print(file)

                if "Sending results STAR for" in file:
                    break

            time.sleep(5)
            count+=1

        time.sleep(10)'''