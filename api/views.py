from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from .serializers import UserSerializer, RoomSerializer, OwnerSerializer, EventSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.views.generic.edit import CreateView


from .models import Room, Owner, Event
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication, SessionAuthentication)
    # permission_classes = (IsAuthenticated,)

class RoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (AllowAny,)

class OwnerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
            """
            This view should return a list of all the purchases
            for the currently authenticated user.
            """
            user = self.request.user
            return Event.objects.filter(owner=user.id)

    def perform_create(self, serializer):
        user = self.request.user

        serializer.save(owner=Owner(user=user))

    # def perform_update(self, serializer):
    #     user = self.request.user
    #     serializer.save(client=User(id=user.id))

class EventAllViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # authentication_classes = (TokenAuthentication, SessionAuthentication)
    # permission_classes = (IsAuthenticated,)

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        serializer = UserSerializer(user, many=False, context={'request': request})
        return Response({'token': token.key, 'user': serializer.data})

