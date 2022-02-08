from django.urls import path
from .views import poll_result,result_sum_total,add_poll_result

urlpatterns = [
    path('',poll_result,name='poll_result'),
    path('result',result_sum_total,name='result'),
    path('add_result',add_poll_result,name='add_result')
    ]