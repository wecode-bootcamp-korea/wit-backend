import jwt
import json

from django.http import JsonResponse, HttpResponse
from .models import User
from wit_backend.settings import wit_secret

def login_decorator(f):        
    def wrapper(self, request, *args, **kwargs):
        access_token = request.headers.get('Authorization', None)
        print(access_token)
        try:                   
            if access_token:   
                decoded = jwt.decode(access_token, wit_secret, algorithms=['HS256'])
                user_id = decoded["user_id"]    
                user = User.objects.get(id=user_id)
                request.user = user             
                
                return f(self, request, *args, **kwargs)
            else:   
                print('else')           
                return HttpResponse(status=401) 
        except jwt.DecodeError:
            print('DecodeError') 
            return HttpResponse(status=401) 
    return wrapper

def login_decorator_pass(f):        
    def wrapper(self, request, *args, **kwargs):
        access_token = request.headers.get('Authorization', None)

        try:                   
            if access_token:   
                decoded = jwt.decode(access_token, wit_secret, algorithms=['HS256'])
                user_id = decoded["user_id"]    
                user = User.objects.get(id=user_id)
                request.user = user             
    
                return f(self, request, *args, **kwargs)
            else:              
                return f(self, request, *args, **kwargs) 
        except jwt.DecodeError:
            return f(self, request, *args, **kwargs) 

    return wrapper