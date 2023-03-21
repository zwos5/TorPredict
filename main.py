import sys
import time
import efPrediction as efp
import fromFilePrediction as ffp

print("Hello and welcome to TorPredict")
time.sleep(2)
print("An Application for predicting unofficial EF Scale values of tornadoes based on windspeed")
time.sleep(1)
   
cont = input("Would you like to run a prediction? ")
if(cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y"):
    x = input("Do you have a file to load? ")
    if (x == "Yes" or x == "yes" or x == "Y" or x == "y"):
        ffp.fromFile()    
    else:
        efp.runPrediction()
else:
    efp.goodbyeMessage()
