import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login("bhardwaj73700@gmail.com", "sonbhardwaj2!@#maamila")

#sender
from = 'bhardwaj73700@gmail.com'

#receiver
to = 'bhardwajnbhardwaj2015@gmail.com'

# message 
message_success = "finally got more than 80% accuracy"


# to send  mail
server.sendmail(from, to, message_success)


# to terminate the session
server.quit()
