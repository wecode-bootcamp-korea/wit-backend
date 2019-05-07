from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import User
import json
import bcrypt


class UserView(View):
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
