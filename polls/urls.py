from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

from .apiviews import *

# schema_view = get_swagger_view(title='Polls API')

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    path("polls/<int:pk>/choice/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choice/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    # path("login/", views.obtain_auth_token, name="login"),
    path("login/", LoginView.as_view(), name="login"),
    # path(r'swagger-docs/', schema_view),
    path(r'swagger-docs/', get_swagger_view(title='Polls API')),
    path(r'docs/', include_docs_urls(title='Polls API')),
]

urlpatterns += router.urls
