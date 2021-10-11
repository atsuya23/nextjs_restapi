from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from training.views import TrainingViewSet, TrainingListView, TrainingRetrieveView, \
    ContentViewSet, ContentRetrieveView, ContentListView, CreateTrainingView, CreateUserView

router = routers.DefaultRouter()
router.register('training', TrainingViewSet, basename='training')

urlpatterns = [
    path('list-training/', TrainingListView.as_view(), name='list-training'),
    path('detail-training/<str:pk>/', TrainingRetrieveView.as_view(), name='detail-training'),
    path('list-content/', ContentListView.as_view(), name='list-content'),
    path('detail-content/', ContentRetrieveView.as_view(), name='detail-content'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
