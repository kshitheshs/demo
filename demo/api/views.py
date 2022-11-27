from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.models import User, Customer
from .serializers import UserSerializer


@api_view(['GET'])
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def addData(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)