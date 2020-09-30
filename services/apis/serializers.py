from rest_framework import serializers 
from rest_framework.serializers import SerializerMethodField
from .models import taluka, village, visitHistory, login

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = '__all__'

class talukaSerializer(serializers.ModelSerializer):
    class Meta:
        model = taluka
        fields = '__all__'

class villageSerializer(serializers.ModelSerializer):
    taluka = serializers.SlugRelatedField(read_only=True, slug_field='name')
    villageName = serializers.CharField(required=True)
    class Meta:
        model = village
        fields = '__all__'
      
class visitHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = visitHistory
        fields = ('__all__')
