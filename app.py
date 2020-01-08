from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
                                 # 패키지로 명령하는 문구는 항상 위에오기

client = MongoClient('localhost', 27017)  # mongo클라이언트는 항상 localhost 27017 포트로 불러줄것 (공식!).
db = client.drawer  # 'drawer'라는 이름의 db를 만든다.


app = Flask(__name__)



## HTMㅣ페이지의 주소를 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/popup') #맨 밑에 app.run 에서 주어진 포트 주소 + /popup을 입력하면 알맞은 페이지로 연결시켜준다.
def popup():
    return render_template('popup.html')


## API 역할을 하는 부분
@app.route('/save', methods=['POST']) #세이브 버튼을 누르면 input 박스에 입력된 정보를 받아서 mongodb에 저장. 저장할때는 POST 명령어
def test_post():
    type_1 = request.form['type']
    name_1 = request.form['name']
    company_1 = request.form['company']
    position_1 = request.form['position']
    number_1 = request.form['number']
    email_1 = request.form['email']
    print(type_1)

    # 'cards'라는 collection에 {'tyle (개발자가 이름을 정함-프론트엔드 페이지와는 상관없음. 하지만 request.form[여기] 에 들어가는 부분은 프론트에서 받은 정보를 백엔드에서 다시 받아
    # 정보를 저장하는 방식이기 때문에 popup.html에서 개발자가 정보를 받을 때 준 고유의 이름을 따라야 한다.)
    db.cards.insert_one({'type': type_1, 'name': name_1, 'company': company_1, 'position': position_1, 'number': number_1, 'email': email_1})
    # db.users.insert_one({'type': '1'})

    return jsonify({'result': 'success', 'msg': 'card saved'})

@app.route('/test', methods=['GET']) #mongodb에서 가져온 정보들을 프론트 페이지에 게시할 수 있도록 준비시켜줄 때 GET 명령어
def test_get():

    # rank의 값이 받은 rank와 일치하는 document 찾기 & _id 값은 출력에서 제외하기 (:0 <-제외한다)
    card_info = db.cards.find({},{'_id':0})

    # info라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'info':card_info})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)







