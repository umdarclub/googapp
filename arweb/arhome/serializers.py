from rest_framework import serializers
from arhome.models import Email, Password, Videos, Member

class EmailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Email
		field = ('id', 'email')

class PasswordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Password
		field = ('id', 'password')

class VideosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Videos
		field = ('id', 'videoID', 'title', 'timestamp')

class MemberSerializer(serializers.ModelSerializer):
	email = EmailSerializer()
	password = PasswordSerializer()
	video_subscribe = VideosSerializer()

	class Meta:
		model = Member
		field = ('id', 'phone', 'memberID', 'name', 'email', 'password', 'video_subscribe')
