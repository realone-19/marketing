from django.urls import path
from products import views


app_name = 'products'


urlpatterns = [
    path('',views.ProductsList.as_view(),name='products'),
    path('farm',views.FarmList.as_view(),name='farm'),
    path('carcass',views.CarcassList.as_view(),name='carcass'),
    path('about',views.About.as_view(),name='about'),
    # path('',views.ProductsList.as_view(),name='products'),
    path('prospect',views.ProspectCreateView.as_view(),name='prospect')
]
