from django.shortcuts import render, redirect
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
from contacts.forms import ContactForm
from contacts.models import Contacts
from contacts.serializers import ContactSerializers
import requests, json


class ContactAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        contact = Contacts.objects.all()
        serializers = ContactSerializers(contact, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializer = ContactSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        data = self.request.data
        name = data['name']
        queryset = Contacts.objects.all().filter(name=name)
        serializer = ContactSerializers(queryset, many=True)

        return Response(serializer.data)


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        data = form.data
        url = 'http://127.0.0.1:8000/contact/newContact/'
        api = requests.post(url=url, data=data)
        if api:
            return redirect('home')
        try:
            resp = json.loads(api.text)
        except:
            resp = None
        print(resp)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
