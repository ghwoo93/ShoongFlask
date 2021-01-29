
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from places.matzip import Matzip
from places.janggwan import JangGwan

#플라스크 앱 생성
# Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
app = Flask(__name__)
#JSON 응답 한글 처리
app.config['JSON_AS_ASCII']=False
#CORS에러 처리
# 데코레이터 이용, '/hello' 경로에 클래스 등록
CORS(app)
#플라스크 앱을 인자로 하여 Api객체 생성:클래스와 URI매핑
# Flask 객체에 Api 객체 등록
api = Api(app)

#요청을 처리할 클래스와 요청 uri 매핑(라우팅)
#Api객체.add_resource(클래스명,'/요청url')
#/todos/<todo_id> url 패턴이면
#get방식이면 todo_id로 조회
#delete방식이면 todo_id로 삭제
#put방식이면 todo_id로 수정
#api.add_resource(Matzip,'/shoong/<lat>/<lng>')
api.add_resource(Matzip,'/places/matzip')
#api.add_resource(JangGwan,'/places/janggwan')
#/todos 로 요청시 get방식이면 전체조회
#                post방식이면 할일 등록
#api.add_resource(TodoList,'/todos')
#api.add_resource(Upload,'/upload')

if __name__ =='__main__':
    app.run(port=10004,host='0.0.0.0')