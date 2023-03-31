import sys
import time

def runPrediction():
    
    ef0 = 0
    ef1 = 0
    ef2 = 0
    ef3 = 0
    ef4 = 0
    ef5 = 0
    efu = 0
    
    windspeed = list()
    num = input("How many tornadoes are you checking? ")

    print("Enter the windspeeds: ")
    i = 0

    for i in range(int(num)):
        x = int(input(""))
        windspeed.append(x)
    i = i + 1

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
    
    print("\n============ Total Tornadoes ============")
    print('EFU Tornadoes: ', efu, '\n')
    print('EF0 Tornadoes: ', ef0, '\n')
    print('EF1 Tornadoes: ', ef1, '\n')
    print('EF2 Tornadoes: ', ef2, '\n')
    print('EF3 Tornadoes: ', ef3, '\n')
    print('EF4 Tornadoes: ', ef4, '\n')
    print('EF5 Tornadoes: ', ef5, '\n')

    tornadototal = efu + ef0 + ef1 + ef2 + ef3 + ef4 + ef5
    print('Writing to a file...')
    time.sleep(2)
    
    outfile = open("tornadowebreport.html", "w")
    outfile.write('<link rel="stylesheet" type="text/css" href="webreportstyles.css">')
    outfile.write('<a href="tornadowebreport.html">Tornado Report</a>')
    outfile.write(' ')
    outfile.write('<a href="checkArea.html">Check Your Local Area</a>')
    outfile.write("<html>\n<head>\n<title> \nTornadics Tornado Report \
           </title>\n</head> <body><h1><u>Tornadics Tornado Report</u></h1>\
           \n<h2>Prediction Results:</h2>EFU Tornadoes: ")
    outfile.write(str(efu))  
    outfile.write("<br> EF0 Tornadoes: ")
    outfile.write(str(ef0)) 
    outfile.write("<br> EF1 Tornadoes: ") 
    outfile.write(str(ef1)) 
    outfile.write("<br> EF2 Tornadoes: ")
    outfile.write(str(ef2))
    outfile.write("<br> EF3 Tornadoes: ")
    outfile.write(str(ef3))
    outfile.write("<br> EF4 Tornadoes: ")
    outfile.write(str(ef4))
    outfile.write("<br> EF5 Tornadoes: ")
    outfile.write(str(ef5))
    outfile.write("<br><br><b> Percentage of Tornadoes of an estimated EF3 or greater: ")
    outfile.write(str(((ef3+ef4+ef5)/tornadototal) * 100))
    outfile.write("%")
    outfile.write("<br><b>Total Reported Tornadoes: ")
    outfile.write(str(tornadototal))
    outfile.write("</body></html>")
    
    print('View a web report at ', outfile)

def goodbyeMessage():
    print("Ok goodbye")