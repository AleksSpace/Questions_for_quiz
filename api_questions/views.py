import requests
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api_questions.serializers import MyInputSerializer, QuestionsSerializer
from questions.models import Questions_quiz

URL = 'https://jservice.io/api/random?count='


@api_view(['POST'])
def my_view(request):
    count_q = 0
    input = MyInputSerializer(data=request.data)
    input.is_valid(True)
    count = input.data['questions_num']
    tp_api = URL + str(count)
    response_data = requests.get(tp_api).json()
    for res_data in response_data:
        if not Questions_quiz.objects.filter(
            text_q=res_data['question']
        ).exists():
            quest = Questions_quiz(
                id_q=res_data['id'],
                text_q=res_data['question'],
                text_answ=res_data['answer'],
                pub_date=res_data['created_at'],
            )
            quest.save()
            count_q += 1
    res_int = count - count_q
    if res_int != 0:
        return requests.post(reverse(
            'questions',
            kwargs={'questions_num': res_int}))

    last_obj = Questions_quiz.objects.last()
    if last_obj is None:
        return None
    else:
        serializer_for_last_obj = QuestionsSerializer(
            instance=last_obj
        )
        return Response(serializer_for_last_obj.data)
