from django.urls import path
from . import views


urlpatterns=[
    path('',views.home, name="home"),
    path('login',views.login_page,name="login_page"),
    path('add_student',views.add_student,name="add_student"),
    path('register',views.register, name="register"),
    path('logout',views.logout_page, name="logout_page"),
    path('update/<int:id>',views.update, name="update"),
    path('delete/<int:id>',views.delete, name="delete"),
]