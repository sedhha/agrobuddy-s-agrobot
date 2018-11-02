import serial
import numpy
import matplotlib.pyplot as plt

#Temperature/ Moisture/ Pressure
def TMP():
    aD=serial.Serial('COM8',9600)
    if  (aD.inWaiting()==0):
        break
    astring=str(aD.readline())
    arr=[T,M,P]
    return(arr)
