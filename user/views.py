from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import authenticate
from .models import User
import json, bcrypt

# 회원가입
class UserSignUpView(View):
    def post(self, request):
        user_input = json.loads(request.body)

        if User.objects.filter(user_email=user_input['user_email']).exists():
                return JsonResponse({'success': False, 'message': '이미 존재하는 이메일입니다.'},status=409)

        else:
            password = bytes(user_input['user_password'], "utf-8")
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

            User(
                user_email = user_input['user_email'],
                user_nickname = user_input['user_nickname'],
                user_password = hashed_password.decode("UTF-8")
            ).save()

            return JsonResponse({'success': True, 'message': '회원가입 완료'},status=200)

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

            if bcrypt.checkpw(user_input['user_password'].encode("UTF-8"), user.user_password.encode("UTF-8")):
                return JsonResponse({'success': False, 'message':'로그인 성공'}, status=200)
            else:
                return JsonResponse({'success': False, 'message':'올바른 비밀번호가 아닙니다'},status=401)
        else:
            return JsonResponse({'success': False, 'message': '존재하지 않는 이메일입니다'},status=401)






        




