from rest_framework import serializers
from .models import Customer,Activity


class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        
        fields = "__all__"
        

class ActivitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Activity
        
        fields = "__all__"
        read_only_fields = ["customer"]