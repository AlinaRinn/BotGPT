import g4f
from time import sleep
from threading import Thread
STATE = False


def awaiting():
    global STATE
    time = int(0)
    while(STATE == False):
        print("Waiting for " + str(time) + "s\r", sep = "", end = "")
        time+=1
        sleep(1)



while(True):
    question = str(input("Enter message: "))
    new_thread = Thread(target=awaiting)
    STATE = False
    new_thread.start()
    response = g4f.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "Nika", "content": question}])
    STATE = True
    print(response)




