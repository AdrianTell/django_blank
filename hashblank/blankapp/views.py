from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes

from hashblank.blankapp import serializers

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import User

from rest_framework.parsers import JSONParser

from rest_framework_simplejwt.views import TokenObtainPairView

from hashblank import settings



#CustomTokenView
#Unprotected
class CustomTokenObtainView(TokenObtainPairView):
    serializer_class = serializers.CustomerTokenObtainPairSerializer


@api_view(['GET'])
def NiceView(GenericAPIView):
    return HttpResponse(':)', status=200)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def ProtectedNice(GenericAPIView):
    return HttpResponse(':)', status=200)

@api_view(['GET'])
@permission_classes((IsAdminUser,))
def AdminNice(GenericAPIView):
    return HttpResponse(':)', status=200)
