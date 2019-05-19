from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import TrainInfo, TrainResult
from django.core import serializers
from user.utils import login_required
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

    @login_required
    def post(self, request):
        front_input = json.loads(request.body)
       
        for t in front_input:
            TrainResult(
                activation_time = t['activation_time'],
                break_time = t['break_time'],
                train_set = t['train_set'],
                calorie_consumption = t['calorie_consumption'],
                train = TrainInfo.objects.get(id=t['train_id']),
                user = request.user
            ).save()

        return JsonResponse({'success': True, 'message': 'train result saved'},status=200)