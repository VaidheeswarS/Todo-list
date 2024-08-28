from rest_framework import serializers
from .models import *

class postdata(serializers.ModelSerializer):
    class Meta:
        model=User_Registration
        fields="__all__"

class wtable(serializers.ModelSerializer):
    class Meta:
        model=Works
        fields="__all__"

