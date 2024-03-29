""" Serializers for messenger.channels """


from rest_framework.serializers import ModelSerializer
from messenger.channels.models import Channel


# Create your serializers here.
class ChannelSerializer(ModelSerializer):
    """Channel Serializer"""

    class Meta:
        """Meta Data"""

        model = Channel
        read_only_fields = ["user"]
        fields = [
            "id",
            "url",
            "user",
            "photo",
            "name",
            "description",
            "private",
            "created_at",
            "updated_at",
        ]
