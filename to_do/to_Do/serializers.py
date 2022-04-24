from rest_framework import serializers
from to_Do.models import ToDoItem


class ToDoItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        exclude = ('slug',)


class ToDoItemDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = ToDoItem
        exclude = ('slug',)


