import os
accuracy = os.system("cat /code/accuracy.txt")
x = 'model.add(Dense(units=32, activation=\"relu\"))'
if accuracy < 80:
    os.system("sed -i '/sigmoid/ i {}' /code/mycode.py".format(x))
else:
    print("accuracy is more than 80%:)")
    exit()
