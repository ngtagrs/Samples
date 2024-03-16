from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.user.is_anonymous: # 未ログインの処理
            if ('/logout' in request.path) or ('/login' in request.path):
                return response
            else:
                return redirect('/accounts/login')
        return response