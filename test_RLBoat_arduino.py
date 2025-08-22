import time
import serial
import math

loopcount = 0
test_speed = 0
test_steer = 5

ser = serial.Serial("COM3", 115200, timeout = 1)
while (loopcount <1000):
    op = str(106+int(3*math.sin(loopcount*0.1)))+"," + "10"+",b,0,testmsg,"+str(106+int(3*math.sin(loopcount*0.1)))+", &"
    print(op)
    #op = "105,28,b,0,RLBoat,108, &"
    ser.write(op.encode())
    print("R: ", loopcount)

    if (test_speed<255):
        test_speed = test_speed + 0.1

    time.sleep(0.05)
    loopcount = loopcount +1

ser.close()



