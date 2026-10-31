from rest_framework import serializers
from .models import Customer,Activity,User,Profile


class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        
        fields = "__all__"
        

class ActivitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Activity
        
        fields = "__all__"
        read_only_fields = ["customer"]
        
        
class UserSerializer(serializers.ModelSerializer):
    
    
    profile_image =serializers.ImageField(
            source="profile.image",
            read_only=True
        )
    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "profile_image",

        ]
        
class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = "__all__"
    