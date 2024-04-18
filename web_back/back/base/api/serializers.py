from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from base.models import *

from django.contrib.auth.models import User, Group

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class LicenseModelSerializer(ModelSerializer):
    class Meta:
        model = LicenseModel
        fields = "__all__"
        extra_kwargs = {'key': {'read_only': True}}

    def create(self, validated_data):
        license_instance = LicenseModel.objects.create(**validated_data)
        html_content = render_to_string('email_license.html', {'license_uuid': license_instance.key})
        text_content = strip_tags(html_content)
        send_mail(
            subject="This is your license",
            message=text_content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["vlad.tyabin2006@mail.ru"],
            html_message=html_content,
            fail_silently=False,
        )
        return license_instance




class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(slug_field='name', queryset=Group.objects.all(), many=True, required=False)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        groups_data = validated_data.pop('groups', None)
        user = User.objects.create_user(**validated_data)
        if groups_data:
            for group_name in groups_data:
                group, _ = Group.objects.get_or_create(name=group_name)
                user.groups.add(group)
        return user