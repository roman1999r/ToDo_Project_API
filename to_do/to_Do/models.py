import uuid

from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class ToDoItem(models.Model):
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True, default=uuid.uuid1)
    title = models.CharField(max_length=64, verbose_name="Title")
    date = models.DateField
    comment = models.CharField(max_length=255, verbose_name="Comment", blank=True)
    text = models.TextField(verbose_name="Text", blank=True)
    PRIORITY_TYPES = (
        (1, 'Обовязково'),
        (2, 'Бажано'),
        (3, 'По можливості')
    )
    priority = models.IntegerField(verbose_name='Приоритет', choices=PRIORITY_TYPES)
    user = models.ForeignKey(User, verbose_name='Юзер', on_delete=models.CASCADE)


    class Meta:
        ordering = ['priority']



'''
class User(models.Model):
    login = models.CharField(verbose_name="Login", max_length=50)
    password = models.CharField(verbose_name="Password", max_length=50)
    nickname = models.CharField(verbose_name="Nick Name", max_length=50)
    todoitem = models.ForeignKey(ToDoItem, verbose_name='Завдання', on_delete=models.CASCADE())
'''

