from django.urls import path

from .views import ProfileView, MeetView, CommentView

urlpatterns = [
    path('profile/', ProfileView.as_view()),
    path('meet/<int:pk>/', MeetView.as_view()),
    path('', MeetView.as_view()),
    path('comments/<int:pk>/',CommentView.as_view()),
    path('comments/',CommentView.as_view()),
]