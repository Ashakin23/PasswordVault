def varify():

    import emailto
    import random
    from cryptography.fernet import Fernet
    import pyzipper
    import os
    import pyAesCrypt as pac
    
    #generate the key
    key = Fernet.generate_key()
    #string the key into a file
    with open('unlock.key', 'wb') as unlock:
        unlock.write(key)
        
    
    
    otp=""
    for i in range(6):
        otp+=str(random.randrange(0,10))
        
    
    inpfile = open("mp.txt")
    inpfile = inpfile.read()
    
    
    
    if len(inpfile)==0:
        set_master_email = input("Set Master Email: ")
       # emailto.rec= set_master_email
        #emailto.otp = otp
        emailto.em(set_master_email,otp)
        
        
        
        
        
        
        print("An OTP is being sent to your email to varify. Please enter the OTP.")
        check = input("Enter the OTP: ")
    
        if otp == check:
            print("Account Varified")
        
        
        else:
            print("Wrong OTP! App is terminating!!!")
            exit()
            
        while True:
            set_master_password = input("Set a NEW Master Password: ")
            con = input("Confirm NEW Master Password: ")
            if set_master_password == con:
                break;
            else:
                continue;
        outfile = open("mp.txt","w")
        outfile2 = open("me.txt",'w')
        outfile3 = open('ps.txt','w')
        outfile2.write(set_master_email);
        outfile.write(set_master_password)
        outfile.close()
        outfile2.close()
        outfile3.write("This is the saved password file.\n")
        outfile3.close()
        
        sep = str.encode(set_master_password)
        
        
        with pyzipper.AESZipFile('uk.zip', 'a', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
            zf.setpassword(sep)
            zf.write('unlock.key')
        

        key = key.decode('utf-8')
        pac.encryptFile("mp.txt", "mp.txt.aes", key)
        pac.encryptFile("ps.txt", "ps.txt.aes", key)
        
        os.remove('unlock.key')
        os.remove('ps.txt')
        os.remove('mp.txt')
        
        
        


def varify2():

    import emailto
    import random
    import sys
    
    otp=""
    for i in range(6):
        otp+=str(random.randrange(0,10))
    
    inpfile = open("me.txt")
    inpfile = inpfile.read()
    
    
    while True:
        asking_master_email = input("Enter Master Email: ")
        if asking_master_email == inpfile:
            otp=""
            for i in range(6):
                otp+=str(random.randrange(0,10))
            emailto.em(asking_master_email,otp)
            print("An OTP is being sent to your email to varify. Please enter the OTP.")
            check = input("Enter the OTP: ")
        
            if otp == check:
                print("Account Varified")
            
            
            else:
                print("Wrong OTP! App is terminating!!!")
                sys.exit()
                
            print("You may set a new master password. ")
            outfile = open("mp.txt","w")
            outfile.write(asking_master_email);
            outfile.write("\n");
            while True:
                set_master_password = input("Set a NEW Master Password: ")
                con = input("Confirm NEW Master Password: ")
                if set_master_password == con:
                    break;
                else:
                    print("Wrong password input!!")
                    continue;
            outfile.write(set_master_password);
            outfile.close()
        else:
            print("Master email is wrong!")
            print("Want to quit?(y/n)");c=input();
            if c=='y' or c=='Y':
                break;
            else:
                continue;
        break;