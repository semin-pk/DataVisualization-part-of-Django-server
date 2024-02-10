#클래스형 View를 만들기 위해서 import
from django.views import View
#csrf 설정을 위한 import
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

#데이터 모델을 가져오기 위한 import
from .models import Todo
#날짜와 시간을 사용하기 위한 import
from datetime import datetime

#JSON으로 응답을 하기 위한 import
from django.http import JsonResponse

#클라이언트의 정보를 JSON 문자열로 만들기 위한 import
import json

@method_decorator(csrf_exempt, name = 'dispatch')
class Todoview(View):
    '''def post(self, request):
        #클라이언트의 데이터를 json 형식으로 가져오기
        request = json.loads(request.body)

        #userid 와 title 매개변수 값을 읽어서 저장
        #클라이언트에서 입력해주는 데이터만 읽어오면 됨
        
        userid = request["userid"]
        title = request["title"]
        #모델 인스턴스를 생성
        todo = Todo()
        todo.userid = userid
        todo.title = title

        todo.save()

        #userid와 일치하는 데이터만 추출
        todos = Todo.objects.filter(userid = userid)
        #todos = todoToDictionary(todos)
        return JsonResponse({"list":list(todos.values())})'''

    def get(self, request):
        #userid 라는 파라미터를 읽기
            fields_list = [field.name for field in Todo._meta.fields]
            return JsonResponse({"list": fields_list})