from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from django.db.models import Q

from app_qr import models
from app_qr import serializers


class PmpModel(APIView):
    def get(self, request):
        pmpModel = models.PmpModel.objects.all()

        serialize = serializers.PmpModelSerializer(pmpModel, many = True)
        return Response(serialize.data, status = status.HTTP_200_OK)

    def post(self, request):
        serialize = serializers.PmpModelSerializer(data=request .data)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)

        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
        

class SiteInfo(APIView):
    def get(self, request, id = None):

        if id:
            siteInfo = models.SiteInfo.objects.get(site_id = id)
            serialize = serializers.SiteInfoSerializer(siteInfo)
            return Response(serialize.data)    

        siteInfo = models.SiteInfo.objects.all()

        serialize = serializers.SiteInfoSerializer(siteInfo, many = True)
        return Response(serialize.data)

    def post(self, request):
        serialize = serializers.SiteInfoSerializer(data=request.data)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)

        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

class SitePmp(APIView):
    def get(self, request, id = None, pmp_id = None):

        if id and pmp_id:
            sitePmp = models.SitePmp.objects.filter(Q(site_id = id) & Q(pmp_manu_num = pmp_id))
            serialize = serializers.SitePmpSerializer(sitePmp, many = True)
            return Response(serialize.dat, status = status.HTTP_200_OK)    

        sitePmp = models.SitePmp.objects.filter(Q(site_id = id))

        serialize = serializers.SitePmpSerializer(sitePmp, many = True)
        return Response(serialize.data)

    def post(self, request, id = None, pmp_id = None):
        serialize = serializers.SitePmpSerializer(data=request .data)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)

        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
