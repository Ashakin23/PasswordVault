import smtplib as sl



def em(rec,otp):
    sender = input("Sender Email: ")
    password = input("Password: ")

    x = "outlook.com"
    SUBJECT = "One Time Password"
    TEXT = "Your OTP for PasswordVault is {}".format(otp)
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    server = sl.SMTP("smtp-mail."+x,587)
    server.starttls()
    server.login(sender,password)
    server.sendmail(sender,rec,message)