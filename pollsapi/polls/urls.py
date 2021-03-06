from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.views import get_swagger_view
# from rest_framework.documentation import include_docs_urls
from .apiviews import UserCreate, LoginView, PollViewSet, PollList, PollDetail, ChoiceList, CreateVote

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

# schema_view = get_swagger_view(title='Polls API')
# schema_view = get_schema_view(
#     title="Polls API",
#     description="Description of Polls API",
#     version="0.0.1"
# )

urlpatterns = [
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path("signin/", views.obtain_auth_token, name="signin"),
    path("polls-list/", PollList.as_view(), name="polls_list"),
    path("polls-list/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    # path('schema', schema_view, name='coreapi-schema'),
    # path(r'docs/', include_docs_urls(title='Polls API')),
    # url('^schema$', schema_view),
]

urlpatterns += router.urls
