import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("bhardwaj73700@gmail.com", "")


    # message
message_success = "Achieved the accuracy we wanted"


    # sending the mail
s.sendmail("bhardwaj73700@gmail.com", "bhardwajnbhardwaj2015@gmail.com", message_success)


    # terminating the session
s.quit()
