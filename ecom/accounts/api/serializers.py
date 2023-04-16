from rest_framework import serializers
from accounts.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','password','mobile','role')
        extra_kwargs = {
            'password':{'required':True,'write_only':True},
            'username':{'required':True},
            'mobile':{'required':True},
            'role': {'required':True}
        }
    
    def create(self, validated_data):
        try:
            password = validated_data.pop('password')
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
                instance.save()
                return instance
            else:
                raise ValueError("Invalid or None Password...")
        except KeyError as e:
            raise KeyError("Password must be provided...")

        