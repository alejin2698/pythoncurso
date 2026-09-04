from rest_framework.serializers import ModelSerializer
from posts.models import Post

## Formatea los datos y valida los datos que entran y salen de la api
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'order', 'created_at']
        # fields = '__all__'
        