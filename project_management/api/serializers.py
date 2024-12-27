from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        username = validated_data.get('username', instance.username)  
        email = validated_data.get('email', instance.email)
        first_name = validated_data.get('first_name', instance.first_name)
        last_name = validated_data.get('last_name', instance.last_name)
        password = validated_data.pop("password")
        
        if User.objects.filter(email=email).exclude(username=instance.username).exists():
            raise serializers.ValidationError({"Email": "Email address already exists for another user"})

        if username != instance.username and User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "A user with that username already exists."})
        
        instance.username = username
        instance.email = email
        instance.first_name = first_name
        instance.last_name = last_name
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    
    
class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = '__all__'


class ProjectMemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProjectMember
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    project = serializers.IntegerField(source="project.id", read_only=True)
    
    class Meta:
        model = Task
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    task = serializers.IntegerField(source="task.id", read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        