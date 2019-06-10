
from rest_framework import viewsets
from .serializers import ImageSerializer
from DachoreApp.models import Image
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from rest_framework import status
from rest_framework.decorators import api_view


import os
import json
import Image_add


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

def get_image(request, imageName):
    image_Name = Image_add.Dachore_image(imageName)
    if not image_Name.Image_add(imageName):
        return HttpResponseNotFound("{} is not exist. plz try input image again.. ' ".format(imageName))
    image_Name.Image_packageList(imageName)
    image_Name.Image_delete()
    return HttpResponse("{} analysis success!!".format(imageName))


def get_images(request,firstName,secondName):
    image_Name = firstName + "/" + secondName
    fullName = Image_add.Dachore_image(image_Name)
    fullName.Image_add(image_Name)
    fullName.Image_packageList(image_Name)
    fullName.Image_delete()
    return HttpResponse("Docker image Name {}".format(image_Name))

