import time
import winsound

cont = 10
while cont > 0:
    print(cont)
    cont -= 1
    time.sleep(0.4)
    
print ('a')   
winsound.Beep(2500, 10000)
    