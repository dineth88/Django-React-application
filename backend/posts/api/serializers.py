from rest_framework.serializers import ModelSerializer
from ..models import Post

# convert django model to json format
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body')