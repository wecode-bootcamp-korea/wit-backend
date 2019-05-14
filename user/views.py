from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import User
import json, bcrypt, jwt, secrets
from wit_backend.settings import wit_secret


# 회원가입
class UserSignUpView(View):
    def post(self, request):
        user_input = json.loads(request.body)
        if User.objects.filter(user_email=user_input['user_email']).exists():
                return JsonResponse({'success': False, 'message': 'email already exists'},status=409)

        else:
            password = bytes(user_input['user_password'], "utf-8")
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            print(hashed_password)
            User(
                user_email = user_input['user_email'],
                user_nickname = user_input['user_nickname'],
                user_password = hashed_password.decode("UTF-8")
            ).save()

            return JsonResponse({'success': True, 'message': 'sign up success'},status=200)

# 로그인
class UserSignInView(View):
    def post(self, request):

# 디버깅
        # print(f"body == {request.body}")
        
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