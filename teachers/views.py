from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


@api_view(http_method_names=['POST', 'GET'])
def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token = Token.objects.get_or_create(user=user)
            print(token[0].key)
            return Response({
                "status": "ok",
                "token": token[0].key
            })
        return Response({
            "status": "error",
            "info": "Foydalanuvchi nomi yoki kalit so'zi xato"
        })
    return Response({
        "status": "faild"
    })