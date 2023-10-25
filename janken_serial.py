from decide_hand import DecideHand
import serial
import time
 
ser = serial.Serial('COM4',9600)
time.sleep(2)
a = "1"
ser.write(bytes(a,'utf-8'))
# print(ser.read())
ser.close()
# dh = DecideHand()
# print(dh.DecideAIHand(battle = "win"))