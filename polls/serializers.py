from rest_framework import serializers
from .models import Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        # fields = ('id', 'question', 'choice_text', 'votes')
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Question
        # fields = ['id', 'question_text', 'pub_date'] # need to insert id not seen in the models
        # fields = ['choices']  # doesn't show content but works
        fields = '__all__'  # shows all fields



