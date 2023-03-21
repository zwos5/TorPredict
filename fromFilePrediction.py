import sys
import time

def fromFile():
    ef0 = 0
    ef1 = 0
    ef2 = 0
    ef3 = 0
    ef4 = 0
    ef5 = 0
    efu = 0
    
    file1 = open("tornadosurvey.txt", "r+")
    windspeed = list()
    num = file1.readline()

    print("Getting the windspeeds...")
    time.sleep(1)
    
    i = 0
    for i in range(int(num)):
        x = int(next(file1))
        windspeed.append(x)
    i = i + 1
    
    
    i = 0
    print("Calculating EF Levels...")
    time.sleep(1)
    for i in range(int(num)):
        if(windspeed[i] > 200):
            print("Tornado likely an EF5")
            ef5 = ef5 + 1
        elif(windspeed[i] >= 166 and windspeed[i] <= 200):
            print("Tornado likely an EF4")
            ef4 = ef4 + 1
        elif(windspeed[i] >= 136 and windspeed[i] <= 165):
            print("Tornado likely an EF3")
            ef3 = ef3 + 1
        elif(windspeed[i] >= 111 and windspeed[i] <= 135):
            print("Tornado likely an EF2")
            ef2 = ef2 + 1
        elif(windspeed[i] >= 86 and windspeed[i] <= 110):
            print("Tornado likely an EF1")
            ef1 = ef1 + 1
        elif(windspeed[i] >= 65 and windspeed[i] <= 85):
            print("Tornado likely an EF0")
            ef0 = ef0 + 1
        elif(windspeed[i] < 65):
            print("Tornado not strong enough to register on the EF Scale")
            efu = efu + 1
    i = i + 1
    file1.close()
    
    print("\n============ Total Tornadoes ============")
    print('EFU Tornadoes: ', efu, '\n')
    print('EF0 Tornadoes: ', ef0, '\n')
    print('EF1 Tornadoes: ', ef1, '\n')
    print('EF2 Tornadoes: ', ef2, '\n')
    print('EF3 Tornadoes: ', ef3, '\n')
    print('EF4 Tornadoes: ', ef4, '\n')
    print('EF5 Tornadoes: ', ef5, '\n')
