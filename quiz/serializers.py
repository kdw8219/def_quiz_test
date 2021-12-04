from rest_framework import serializers
from .models import Quiz

#json으로 직렬화
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['title', 'body', 'answer',]