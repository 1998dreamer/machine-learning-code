import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login("sender@gmail.com", "**password**")



# message 
message = "finally got more than 80% accuracy"


# to send  mail
server.sendmail('sender@gmail.com', 'receiver@gmail.com', message)


# to terminate the session
server.quit()
