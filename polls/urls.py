from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from polls.views import QuestionViewSet, QuestionListView, QuestionRetrieveView,\
    ChoiceRetrieveView, ChoiceViewSet, ChoiceListView, CreateQuestionView

router = routers.DefaultRouter()
router.register('polls', QuestionViewSet, basename='polls')

urlpatterns = [
    path('list-question/', QuestionListView.as_view(), name='list-question'),
    path('detail-question/<str:pk>/', QuestionRetrieveView.as_view(), name='detail-question'),
    path('register/', CreateQuestionView.as_view(), name='create'),
    path('')
]