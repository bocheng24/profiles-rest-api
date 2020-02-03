from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format = None):

        an_apiview = [
            'This is an HELLO API View'
        ]
        
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})