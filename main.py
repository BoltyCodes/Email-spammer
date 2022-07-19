import smtplib

while True:
    recipient_email = 'dhruvan.biz@gmail.com'
    my_email = "dhruva.happiest@gmail.com"
    password = "mnlulmslwlbscrma"

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)

    connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg="get_spammed!")
    connection.close()
