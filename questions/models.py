from django.db import models


class Questions_quiz(models.Model):
    id_q = models.CharField(max_length=120)
    text_q = models.TextField(unique=True)
    text_answ = models.TextField()
    pub_date = models.DateTimeField()
