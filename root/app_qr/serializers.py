from rest_framework import serializers
from app_qr import models

class PmpModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PmpModel
        fields = '__all__'

class PmpModelHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PmpRepairHistory
        fields = '__all__'

class SiteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SiteInfo
        fields = '__all__'

class SitePmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SitePmp
        fields = '__all__'