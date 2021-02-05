from django.urls import path
from main import views
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
urlpatterns=([
    path('students/',views.ListView.as_view()),
    path('updatestudent/<int:pk>',views.UpdateApiView.as_view()),
    path('filtering/',views.filtering.as_view()),
    #path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
])