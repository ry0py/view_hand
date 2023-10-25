
import serial
import time

start_time = time.time()
from decide_hand import DecideHand # importに時間がかかっている
# dh = DecideHand() # ここで初期化すると時間がかかる
# print(dh.cls_text)# print(dh.DecideAIHand(battle = "win"))
print("DecideHand time: ", time.time() - start_time)
