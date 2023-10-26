import serial
from decide_hand import DecideHand #本当はDecideAIHandのみを使いたい
# ttyのすべてにデータを送ってる
ser = serial.Serial('/dev/tty.',9600,timeout=None)
dh = DecideHand()
trans_janken_data = dh.DecideAIHand(battle = "win")[0]
ser.write(trans_janken_data)
ser.close