import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login("bhardwaj73700@gmail.com", "sonbhardwaj2!@#maamila")



# message 
message = "finally got more than 80% accuracy"


# to send  mail
server.sendmail('bhardwaj73700@gmail.com', 'bhardwajnbhardwaj2015@gmail.com', message)


# to terminate the session
server.quit()
