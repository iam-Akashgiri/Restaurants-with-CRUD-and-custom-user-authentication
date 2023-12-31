from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings  
from django.conf.urls.static import static  

from .views import FoodListView, FoodCreateView, FoodDetailView, FoodDeleteView, FoodUpdateView
from .views import CategoriesDetailView, CategoriesCreateView

urlpatterns = [
    path('home', views.FoodListView.as_view(), name='food_list'),
    path('add_food/', views.FoodCreateView.as_view(), name='food_form'),
    path('<int:pk>/detail', views.FoodDetailView.as_view(), name='food_detail'),
    path('<int:pk>/delete', views.FoodDeleteView.as_view(), name='food_delete'),
    path('<int:pk>/update', views.FoodUpdateView.as_view(), name='food_delete'),

    path('add_categories/', views.CategoriesCreateView.as_view(), name='categories_form'),
    path('<int:id>', views.categories_filter, name='categories_filter'),

    # loginurls
    path('',views.homePage , name='home') , 
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('cart/', views.cart, name="cart"),
    path('checkout/',views.checkout,name='checkout'),
    path('suc',views.suc, name='suc'),
    path('success',views.success, name='success')

]

# if settings.DEBUG:  
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.STATIC_ROOT)   