from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .apiviews import *

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    path("polls/<int:pk>/choice/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choice/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    # path("login/", views.obtain_auth_token, name="login"),
    path("login/", LoginView.as_view(), name="login"),

]

urlpatterns += router.urls
