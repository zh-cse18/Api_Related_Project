from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializers


@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully done'
            data['email'] = user.email
            data['username'] = user.username
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name

        else:
            data = serializer.errors
        return Response(data)
