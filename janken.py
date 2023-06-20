from flask import Flask, render_template, request
from decide_hand import DecideHand #本当はDecideAIHandnのみを使いたい

app = Flask(__name__,static_folder='./templates/images')
dh = DecideHand()
@app.route('/')
def janken():
    return render_template("base.html")
@app.route('/sampleform-post', methods=['Get','POST'])
def sample():
    print('POSTデータ受け取ったので処理します')
    dh.DecideAIHand()
    if dh.DecideAIHand() == "チョキ":
        return "チョキ"
    elif dh.DecideAIHand() == "パー":
        return "パー"
    elif dh.DecideAIHand() == "グー":
        return "グー"
    else:
        hand_num = dh.CountHandNum()
        return "手が" + str(hand_num) + "つあります"
    
    '''
    if(not( names.get(boxes) == None)):
        cls_text = names.get(int(boxes))
        if(cls_text == "paper"):
            return "チョキ"
        if(cls_text == "rock"):
            return "パー"
        if(cls_text == "scissors"):
            return "グー"
    else:
        return "None"
    '''
if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
