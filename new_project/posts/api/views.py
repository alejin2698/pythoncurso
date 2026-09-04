from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from posts.api.permissions import IsAdminOrReadOnly


##### formato modelViewSet de api con serializadores
class  PostModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # http_method_names = ['get', 'post', 'put', 'delete', 'patch']


##### formato viewSet con serializadores
# class PostViewSet(ViewSet):
#     def list(self, request):
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#     def retrieve(self, request, pk=int):
#         serializer = PostSerializer(Post.objects.get(pk=pk))
#         return Response( status=status.HTTP_200_OK, data=serializer.data)


#     def create(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_200_OK)


##### formato basico de api con serializadores
# class PostApiView(APIView):
#     def get(self, request):
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#       def post(self, request):
#           serializer = PostSerializer(data=request.data)
#           serializer.is_valid(raise_exception=True)
#           serializer.save()
#           return Response(data=serializer.data, status=status.HTTP_200_OK)


##### formato basico de api
# class PostApiView(APIView):
#     def get(self, request):
#         posts = [post.title for post in Post.objects.all()]
#         return Response(status=status.HTTP_200_OK, data='hola mundo')

#       def post(self, request):
#           Post.objects.create(title=request.POST['title'], description=request.POST['description'], order=request.POST['order'])
#           return self.get(request)