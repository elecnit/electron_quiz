from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView,name='home'),
    path('stage_1_view/',views.Stage1View,name='stage1'),
    path('stage_1/<str:answer>/<str:correct_answer>',views.Stage1Correcter,name='stage1correcter'),
    path('stage_2/<str:answer>/<str:correct_answer>',views.Stage2Correcter,name='stage2correcter'),
    path('stage_3/<str:answer>/<str:correct_answer>',views.Stage3Correcter,name='stage3correcter'),
]