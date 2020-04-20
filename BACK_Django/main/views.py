from django.shortcuts import render
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from sub3.settings import MEDIA_ROOT

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

import os, datetime, random



def uploaded(f):
    name = str(datetime.datetime.now().strftime('%H%M%S')) + str(random.randint(0, 1000)) + str(f)
    path = default_storage.save(MEDIA_ROOT + '/' + name, ContentFile(f.read()))
    return os.path.join(MEDIA_ROOT, path), name


@api_view(['POST'])
@permission_classes([AllowAny, ])
def image_upload(request):
    for _file in request.FILES.getlist('images[]'):
        request.FILES['images[]'] = _file
        file_path, file_name = uploaded(request.FILES['images[]'])
    return JsonResponse({'result':'true'})
