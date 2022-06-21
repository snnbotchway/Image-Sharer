from django.urls import path
from .views import HomePageView,NewImageView, ImageDetail

app_name = 'feed'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('home/', HomePageView.as_view(), name='home'),
    path('index/', HomePageView.as_view(), name='home'),
    path('upload/', NewImageView.as_view(), name='upload'),
    path('detail/<int:pk>', ImageDetail.as_view(), name='detail'),
]