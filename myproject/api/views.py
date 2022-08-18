from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .models import Predict
from .models import Asmr
from .models import Video
from .serializers import UserSerializer
from .serializers import AsmrSerializer
from .serializers import VideoSerializer
from rest_framework.parsers import JSONParser

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user(request, pk):

    obj = User.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = UserSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def login(request):
    if request.method == 'GET':
        data = JSONParser().parse(request)
        search_email = data['email']
        obj = User.objects.get(email=search_email)
        if obj:
            if data['password'] == obj.password:
                return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)

@csrf_exempt
def asmr(request):

    if request.method == 'GET':
        data = JSONParser().parse(request)
        search_email = data['email']
        search_time = data['time']
        obj = Predict.objects.get(email=search_email, time=search_time)
        
        if obj:
            asmrObj = Asmr.objects.get(emotion=obj.emotion)
            serializer = AsmrSerializer(asmrObj)
            return JsonResponse(serializer.asmr, status=201)
        else:
            return JsonResponse(status=400)

@csrf_exempt
def video(request):

    if request.method == 'GET':
        data = JSONParser().parse(request)
        search_email = data['email']
        search_time = data['time']
        obj = Predict.objects.get(email=search_email, time=search_time)
        
        if obj:
            videoObj = Video.objects.get(emotion=obj.emotion)
            serializer = VideoSerializer(videoObj)
            return JsonResponse(serializer.video, status=201)
        else:
            return JsonResponse(status=400)

