from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import User, UserDetail
from train.models import TrainInfo
from django.core import serializers
import json, bcrypt, jwt, secrets
from wit_backend.settings import wit_secret
from user.utils import login_required



# 회원가입
class UserSignUpView(View):
    def post(self, request):
        user_input = json.loads(request.body)
        if User.objects.filter(user_email=user_input['user_email']).exists():
                return JsonResponse({'success': False, 'message': 'email already exists'},status=409)

        else:
            password = bytes(user_input['user_password'], "utf-8")
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            User(
                user_email = user_input['user_email'],
                user_nickname = user_input['user_nickname'],
                user_password = hashed_password.decode("UTF-8")
            ).save()

            return JsonResponse({'success': True, 'message': 'sign up success'},status=200)

# 로그인
class UserSignInView(View):
    def post(self, request):        
        user_input = json.loads(request.body)
        input_email = user_input["user_email"]
        input_password = user_input["user_password"]

        if User.objects.filter(user_email=user_input['user_email']).exists():
            password = bytes(user_input['user_password'], "utf-8")
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            user = User.objects.get(user_email=user_input['user_email'])
            encoded_jwt_id = jwt.encode({'user_id' : user.id}, wit_secret, algorithm='HS256')

            if bcrypt.checkpw(user_input['user_password'].encode("UTF-8"), user.user_password.encode("UTF-8")):
                return JsonResponse({"access_token" : encoded_jwt_id.decode("UTF-8")}, status=200)
            else:
                return JsonResponse({'success': False, 'message':'invalid password'},status=401)
        else:
            return JsonResponse({'success': False, 'message': 'email does not exist'},status=401)


# 설정페이지 / 유저 상세정보 GET/SET
class UserDetailView(View):

    model = UserDetail

    @login_required
    def get(self, request):
        user = request.user
        user_detail = UserDetail.objects.filter(user_id=user.id)
        user_preference = User.objects.filter(id=user.id).values('user_preference')
    
        # for a in range(len(user_preference)):
        #     ttt = user_preference[a].values
        #     print(ttt)

        print(f"user detail = {user_detail[0]}")
        print(f"user detail = {user_preference}")

        new_list = []
        for pref in user_preference:
            new_list.append(pref['user_preference'])

        data = {
            'user_sex' : user_detail[0].user_sex,
            'user_birthdate' : user_detail[0].user_birthdate,
            'user_weight' : user_detail[0].user_weight,
            'user_height' : user_detail[0].user_height,
            # 'train_ids': [user_preference[0]['user_preference']]
            'train_ids': [pref['user_preference'] for pref in user_preference]
        }

            # d['user_preference'] for d in user_preference

        return HttpResponse(json.dumps(data, ensure_ascii=False), safe=False)

        # serialized_data = serializers.serialize('json', user_preference_list)
        # return HttpResponse(user_preference_list, content_type='application/json')

    @login_required
    def post(self, request):
        user_input = json.loads(request.body)
        # 특정유저의 닉네임 수정하기
        # 특정유저의 디테일정보 수정하기

        UserDetail(
            user_sex = user_input['user_sex'],
            user_birthdate = user_input['user_birthdate'],
            user_weight = user_input['user_weight'],
            user_height = user_input['user_height'],
            # user_preference = TrainInfo.objects.get(id=user_input['train_id']),
            # user_preference = user_input['train_id'],
            user = request.user
        ).save()

        for train_id in user_input['train_ids']:
            train = TrainInfo.objects.get(id = train_id)
            request.user.user_preference.add(train)
        
        return JsonResponse({'success': True, 'message': 'user detail saved'},status=200)



  