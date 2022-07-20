import smtplib

while True:
    try:
     recipient_email = 'person.spam@gmail.com'
     my_email = ""
        #enable 2FA on your email and search for app passwods, put your app password. It should looke like something like the below line.
     password = "mnlulmslwlbscrma" 

     connection = smtplib.SMTP("smtp.gmail.com", 587)
     connection.starttls()
     connection.login(user=my_email, password=password)

     connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg="get_spammed!")
     connection.close()
     
    except:
        ValueError 
