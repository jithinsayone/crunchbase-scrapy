from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views

from .views import PeopleSave,CompanySave,AngelList



urlpatterns = [
    url(r'^save-people/$', PeopleSave.as_view(), name='api-people'),
    url(r'^save-company/$', CompanySave.as_view(), name='api-company'),
    url(r'^angellist/$', AngelList.as_view(), name='api-angellist'),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
