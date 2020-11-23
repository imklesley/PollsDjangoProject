from django.db import models


# Create your models here.

# Cada classe representa uma tabela, e cada tabela automaticamente possui já um campo id autoincrement


class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    #Sobrescrevi para que no admin, seja possível vê algo diferente de Question Object 1. ..
    #Agora irá aparecer a question_text
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # Referencio a qual question essa choice representa, e também digo que se caso a questão seja deletada, a choice tbm será
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
