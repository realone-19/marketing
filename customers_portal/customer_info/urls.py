from django.urls import path
from customer_info import views
from django.contrib.auth.models import User

app_name = 'customer_info'


urlpatterns = [
    # path('',views.IndexView.as_view(),name='index'),
    path('user_login', views.user_login,name='user_login'),
    # path('about',views.About.as_view(),name='about'),
    path('payment',views.PaymentListView.as_view(),name='payment'),
    path('detail/<int:pk>/',views.CustomerDetailView.as_view(),name='detail'),
    path('register', views.register,name='register')
]
