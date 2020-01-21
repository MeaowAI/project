from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create_accout',views.create_accout,name='create_accout'),
    path('requests',views.requests,name='requests'),
    path('inc_share_form',views.inc_share_form,name='inc_share_form'),
    path('withdraw_form',views.withdraw_form,name='withdraw_form'),
    path('reciept_form',views.reciept_form,name='reciept_form'),
    path('signin_form',views.signin_form,name='signin_form')
]
