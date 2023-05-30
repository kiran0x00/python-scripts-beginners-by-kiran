from threading import*
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hellooooooooooooo(Thread):
    def run(self):
        for i in range(5):
            print("Helloooooooooooooooooooooo")
            sleep(1)

t1 = Hello()
t2 = Hellooooooooooooo()
t1.start()
sleep(0.5)
t2.start()
t1.join()
t2.join()
print("End of the code")
