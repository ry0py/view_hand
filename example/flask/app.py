from flask import Flask, render_template, request

app = Flask(__name__)

# ホームページ
@app.route('/')
def index():
    return render_template('index.html')

# 入力値の表示ページ
@app.route('/result', methods=['GET', 'POST']) #GetとPostの受け取り方を指定(両方書かないといけない)
def result():
    # index.htmlのinputタグ内にあるname属性itemを取得し、textに格納した
    text = request.form.get('item')

    # もしPOSTメソッドならresult.htmlに値textと一緒に飛ばす
    if request.method == 'POST':
        return render_template('result.html', txt = text)

    # POSTメソッド以外なら、index.htmlに飛ばす
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)