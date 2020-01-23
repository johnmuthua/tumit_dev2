from rest_framework import generics
from .models import Meet, Comment, Profile
from .serializers import ProfileSerializer, MeetSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly


# Create your views here.
class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class MeetView(generics.ListCreateAPIView):
    queryset = Meet.objects.all()
    serializer_class = MeetSerializer


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
