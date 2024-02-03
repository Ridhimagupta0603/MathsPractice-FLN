from django.urls import path
from . import views

app_name="practice"
urlpatterns = [
    path('practice/',views.practicehome,name='practicehome' ),
    path('practice/Q1',views.practiceQ1,name='practiceQ1' ),

]