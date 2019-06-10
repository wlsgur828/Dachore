from rest_framework import viewsets
from .serializers import ImageSerializer
from DachoreApp.models import Image
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

import os
import json
import Image_add
import DB_select

class ImageViewSet(viewsets.ModelViewSet):
        queryset = Image.objects.all()
        serializer_class = ImageSerializer

def get_image(request, imageName):


        #docker search imageName == true 이면 실행 ?


        #imageName 으로 받은 이름 OS : version으로 분리
        if ':' in imageName:
                arr = imageName.split(':')
                image_Version = arr[1]

        #Image_add.py 파일의 Dachore_image clsss 초기화
        image_Name = Image_add.Dachore_image(imageName)
        image_Name.Image_add(imageName)
        image_Name.Image_packageList(imageName)
        image_Name.Image_delete()

        #임시 변수 DB 테이블이랑 형식 맞추기 위함
        #ex) DB_table_Name = ubuntu1610 / 현재 ubuntu:16.10
        tmpImage = arr[0] + image_Version
        imageName = tmpImage.replace(".","")

        # 만약 해당 경로에 test.txt 파일이 추출되었으면 실행
        file = '/home/ubuntu/test.txt'
        if os.path.isfile(file):
                DB_image_Name = DB_select.DB_query(imageName)
                result_Version_vuln = DB_image_Name.Version_Vuln(imageName)
        #       result_Package_vuln = DB_image_Name.Package_Vuln()
                result_Package_vuln = DB_image_Name.Package_Vuln(imageName)
                return HttpResponse("{} *********** {}".format(result_Version_vuln,result_Package_vuln))

        else:
                return HttpResponse("Not Found DB_table")

def get_images(request,firstName,secondName):
        image_Name = firstName + "/" + secondName
        fullName = Image_add.Dachore_image(image_Name)
        fullName.Image_add(image_Name)
        fullName.Image_packageList(image_Name)
        fullName.Image_delete()
        return HttpResponse("Docker image Name {}".format(image_Name))


"""
@api_view (['GET'])

def image_detail(request, image_Name, format=None):
        return JsonResponse ({'message' : 'hi django','items' : ['파이썬', '장고', 'AWS', 'Azure'],}, json_dumps_params = {'ensure_ascii': True})
"""
