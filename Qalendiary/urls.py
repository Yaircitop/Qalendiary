from django.urls import include,path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[ 
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('calendario/',views.calendarioView,name='calendario'),
    path('subirobjetivo/',views.subirobjetivo,name="subirobjetivo"),
    path('verobjetivos/',views.verobjetivo,name="verobjetivo"),
    path('',views.indexView,name="index"),
    path('borrarobjetivo/<int:pk>/',views.borrarobjetivo, name="borrarobjetivo"),
    path('temporizador/',views.temporizadorView,name="temporizador"),
    path('revisarobjetivo/<int:pk>/',views.revisarobjetivo, name="revisarobjetivo"),
    path('mostrarmensaje/',views.mostrarmensaje,name="mostrarmensaje"),
]