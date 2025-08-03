from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('create/', views.employee_create, name='employee_create'),
    path('update/<int:pk>/', views.employee_update, name='employee_update'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('login/', LoginView.as_view(template_name='employees/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
      # or use Django's LoginView
]
