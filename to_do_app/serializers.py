from .models import Task
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class taskSeri(ModelSerializer):
    class Meta:
        model=Task
        fields = ["id","title","description","completed","created_at","updated_at","user"]
class userSeri (ModelSerializer):
    class Meta:
        model=User
        fields = ["username", "email"]

