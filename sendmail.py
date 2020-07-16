import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("bhardwaj73700@gmail.com", "sonbhardwaj2!@#maamila")


    # message 
message_success = "finally got more than 80% accuracy"


    # to send  mail
s.sendmail("bhardwaj73700@gmail.com", "bhardwajnbhardwaj2015@gmail.com", message_success)


    # to terminate the session
s.quit()
