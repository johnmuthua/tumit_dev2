from rest_framework import viewsets
from .models import Profile, Comment, Meet
from .serializers import ProfileSerializer, MeetSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly


# Create your views here.
class ProfileView(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class MeetView(generics.ListCreateAPIView):
    queryset = Meet.objects.all()
    serializer_class = MeetSerializer


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
