from django.urls import path
from customer import views

urlpatterns=[
    path("accounts/signup",views.customersignup,name="signup"),
    path("accounts/signin",views.customersignin,name="signin"),
    path("acconts/signout",views.signout,name="signout")
]