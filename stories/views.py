""" API endpoints for messenger.stories """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from messenger.mixins import OwnerMixin
from messenger.permissions import IsOwner
from messenger.stories.models import Story, User
from messenger.stories.serializers import StorySerializer


# Create your views here.
class StoryViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete stories"""

    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]
        return super().get_permissions()


class UserStoriesViewSet(StoryViewSet):
    """User stories"""

    def get_queryset(self):
        """Filter queryset by user"""

        user = User.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(user=user)
