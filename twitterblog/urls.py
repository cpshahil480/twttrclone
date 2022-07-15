from django.urls import path
from twitterblog import views





urlpatterns=[
    path("account/signup",views.UserRegistrationView.as_view(),name="sign-up"),
    path("account/login",views.LogInView.as_view(),name="log-in"),
    path("account/base",views.IndexView.as_view(),name="base"),
    path("account/user/creation",views.UserCreationView.as_view(),name="user-creation"),
    path("account/home",views.IndexView.as_view(),name="home"),
    path("account/user/profile",views.ProfileView.as_view(),name="my-profile"),
    path("account/user/logout",views.log_out,name="log-out"),
    path("account/user/update/<int:user_id>",views.UserUpdateView.as_view(),name="profile-update")

]