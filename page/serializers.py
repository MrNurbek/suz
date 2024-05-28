from rest_framework import serializers
from page.models import *


class LogatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logat
        fields = "__all__"


