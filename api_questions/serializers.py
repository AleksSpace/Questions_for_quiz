from rest_framework import serializers

from questions.models import Questions_quiz


class MyInputSerializer(serializers.Serializer):
    questions_num = serializers.IntegerField()


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions_quiz
        exclude = ('id',)
