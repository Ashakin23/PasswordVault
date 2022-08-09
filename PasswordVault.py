import pyzipper
import time
import varify
import pyAesCrypt as pac
import os


inpfile = open("me.txt")
inpfile = inpfile.read()
if len(inpfile)==0:
    varify.varify()
    
    


         
while True:
    while True:
        
        inpfilee =open('me.txt','r')
        inpfilee = inpfilee.read()
        a = input("Enter Master email: ")
        b = input("Enter Master Password: ")
        
        with pyzipper.AESZipFile('uk.zip') as zf:
            try:
                zf.setpassword(str.encode(b))
            except RuntimeError:
                print("Incorrect Username or Password. You may re-enter or change password or quit the app. (r/c/q)")
                x = input()
                if x=='r' or x=='R':
                    continue;
                elif x=='c' or x=='C':
                    varify.varify2()
                    continue;
                else:
                    print('App is quitting...')
                    time.sleep(2)
                    exit();
            if a==inpfilee:
                print("You Have successfully Logged in!")
            else:
                print("Incorrect Username or Password. You may re-enter or change password or quit the app. (r/c/q)")
                x = input()
                if x=='r' or x=='R':
                    continue;
                elif x=='c' or x=='C':
                    varify.varify2()
                    continue;
                else:
                    print('App is quitting...')
                    time.sleep(2)
                    exit();
                
            key = zf.read('unlock.key')
            key = key.decode('utf-8')
            print(key)
            break;
        break;
    break;
        
    
"""Decrypt"""
pac.decryptFile("ps.txt.aes", "ps.txt", key)
inp = open("ps.txt",'r')
inp = inp.read()
fd = inp.split("\n") 

    
print("\n\n")
print ("{:<20} {:<35} ".format('Website/App','Password'))
for i in range(1,len(fd)-1):
    fds = fd[i].split(' ')
    website,psw = fds
    print ("{:<20} {:<35} ".format(website,psw))
print("\n\n")
    

while True:
    print("Want to add another password?(y/n)");e = input();
    if e=='y' or e=="Y":
        oup = open("ps.txt",'a')
        oup.write(input("Enter Website/App name: "))
        oup.write(' ')
        oup.write(input("Enter the password: "))
        oup.write("\n")
        oup.close()
        
        inp = open("ps.txt",'r')
        inp = inp.read()
        fd = inp.split("\n")
        print("\n\n")
        print ("{:<20} {:<35} ".format('Website/App','Password'))
        for i in range(1,len(fd)-1):
            fds = fd[i].split(' ')
            website,psw = fds
            print ("{:<20} {:<35} ".format(website,psw))
        print("\n\n")

    else:
        pac.encryptFile("ps.txt", "ps.txt.aes", key)
        os.remove('ps.txt')
        print("Want to quit?(y/n)");c = input();
        if c=='y' or c=="Y":
            exit()
        else:
            while True:
                pac.decryptFile("ps.txt.aes", "ps.txt", key)
                inp = open("ps.txt",'r')
                inp = inp.read()
                fd = inp.split("\n")
                print("\n\n")
                print ("{:<20} {:<35} ".format('Website/App','Password'))
                for i in range(1,len(fd)-1):
                    fds = fd[i].split(' ')
                    website,psw = fds
                    print ("{:<20} {:<35} ".format(website,psw))
                print("\n\n")
                print("Want to quit?(y/n)");c = input();
                if c=='y' or c=="Y":
                    pac.encryptFile("ps.txt", "ps.txt.aes", key)
                    os.remove('ps.txt')
                    exit()
                    
                else:
                    continue;