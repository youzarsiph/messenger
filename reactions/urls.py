""" URLConf for messenger.reactions """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.reactions.views import UserReactionsViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("reactions", UserReactionsViewSet, "reaction")


urlpatterns = [
    path("", include(router.urls)),
]
