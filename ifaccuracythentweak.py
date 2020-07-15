import os
accuracy = os.system("cat /dlcode/accuracy.txt")
x = 'model.add(Dense(units=32, activation=\"relu\"))'
if accuracy < 80:
    os.system("sed -i '/sigmoid/ i {}' /dlcode/mycode.py".format(x))
else:
    print("You Achieved wnated accuracy :)")
    exit()
