from rest_framework import serializers
from .models import MoodData
from users.form import UserForm
from rest_framework import serializers
from .models import CustomUser
from django.core.exceptions import ValidationError
from datetime import date


class MoodDataSerializers(serializers.ModelSerializer):

    token=serializers.SerializerMethodField(read_only=True)
    dateposted=serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=MoodData
        fields='__all__'

    def get_token(self,obj):

        return obj.token
    
    def get_dateposted(self, obj):

        return obj.dateposted.strftime('%Y-%m-%d %H:%M:%S')

    def get_user(self, obj):

        return obj.user.username
    



class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    date_of_birth = serializers.DateField(write_only=True, input_formats=['%Y-%m-%d'])
    password1 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate_date_of_birth(self, value):
        min_age = 10
        if value:
            age = (date.today() - value).days // 365
            if age < min_age:
                raise ValidationError(f'You must be at least {min_age} years old to register.')
        return value

    def validate(self, data):
        form = UserForm(data)
        if not form.is_valid():
            raise serializers.ValidationError(form.errors)
        return data

    def create(self, validated_data):
        return CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password1'],
            date_of_birth=validated_data['date_of_birth']
        )
