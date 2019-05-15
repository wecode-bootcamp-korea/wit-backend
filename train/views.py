from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import User, TrainInfo, TrainResult
from django.core import serializers
from user.utils import login_decorator
import json


#운동별 상수값 가져오기
class TrainInfoView(View):
    
    model = TrainInfo

    def get(self, request):
        data = serializers.serialize('json', TrainInfo.objects.all())
        return HttpResponse(data, content_type='application/json')
        
#유저별 운동결과 저장
class TrainResultView(View):

    model = TrainResult

    @login_decorator
    def post(self, request):
        front_input = json.loads(request.body)

        # print(TrainInfo.objects.get(id=front_input['train_id']))

        TrainResult(
            activation_time = front_input['activation_time'],
            break_time = front_input['break_time'],
            train_set = front_input['train_set'],
            calorie_consumption = front_input['train_set'],
            train = TrainInfo.objects.get(id=front_input['train_id']),
            user = request.user
        ).save()

        return JsonResponse({'success': True, 'message': 'sign up success'},status=200)
