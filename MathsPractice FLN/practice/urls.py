from django.urls import path
from . import views


urlpatterns = [
    path('practice/',views.practice,name='practicehome' ),
    path('practice/Q1',views.practiceQ1,name='practiceQ1' ),

]