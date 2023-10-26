from flask import Flask, render_template, request
from decide_hand import DecideHand #本当はDecideAIHandのみを使いたい

app = Flask(__name__,static_folder='./templates/images')
dh = DecideHand()
@app.route('/')
def janken():
    return render_template("base.html")
@app.route('/sampleform-post', methods=['Get','POST'])
def sample():
    print('POSTデータ受け取ったので処理します')
    hand = dh.DecideAIHand(battle = "win")[0]
    #dh.ViewHandImage()
    hand_num = dh.CountHandNum()
    if(hand_num == 1):
        if hand == "scissors":
            return render_template("result_scissors.html", answer=hand)
        elif hand == "paper":
            return render_template("result_paper.html", answer=hand)
        elif hand == "rock":
            return render_template("result_rock.html", answer=hand)            
    else:
        answer = "手が" + str(hand_num) + "つあります"
        return render_template("result_none.html", answer=answer)
    
    '''
    if(not( names.get(boxes) == None)):
        cls_text = names.get(int(boxes))
        if(cls_text == "paper"):
            return "scissors"
        if(cls_text == "rock"):
            return "paper"
        if(cls_text == "scissors"):
            return "rock"
    else:
        return "None"
    '''
if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
