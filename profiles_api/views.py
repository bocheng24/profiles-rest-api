from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permission


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):

        an_apiview = [
            'This is an HELLO API View'
        ]
        
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(
                    serializer.errors, 
                    status = status.HTTP_400_BAD_REQUEST
                )
    
    def put(self, request, pk = None):
        """Handle Updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk = None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk = None):
        """To delete an object"""
        return Response({'method': 'DELETE'})

class HelloViewset(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self, request):

        a_viewset = [
            'This is a hello view set'
        ]

        return Response(
            {
                'message': "Hello",
                'a_viewset': a_viewset
            }
        )

    def create(self, request):
        '''Create a new hello message'''

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'Hellooooooo {name}!'

            return Response(
            {
                'message': msg
            }
        )
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk = None):
        '''Handle getting an object by its ID'''
        return Response(
            {'http_method': 'GET'}
        )
    
    def update(self, request, pk = None):
        '''Handle updating an object by its ID'''
        return Response(
            {'http_method': 'PUT'}
        )

    def partial_update(self, request, pk = None):
        '''Handle partial updating an object by its ID'''
        return Response(
            {'http_method': 'PATCH'}
        )

    def destroy(self, request, pk = None):
        '''Handle delete an object by its ID'''
        return Response(
            {'http_method': 'DELETE'}
        )

class UserProfileViewSet(viewsets.ModelViewSet):
    '''Handle Creating and updating profiles'''
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permission.UpdateOwnProfile, )