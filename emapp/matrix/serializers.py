from rest_framework import serializers
from matrix.models import Task, Topic

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'topic', 'importance', 'due_date')

class TopicSerializer(serializers.ModelSerializer):
    task_set = TaskSerializer(many=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Topic
        fields = ('id', 'name', 'color', 'owner', 'task_set')

    def create(self, validated_data):
        task_set_data = validated_data.pop('task_set')
        topic = Topic.objects.create(**validated_data)
        for task_data in task_set_data:
            Task.objects.create(topic=topic, **task_data)
        return topic

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.color = validated_data.get('color', instance.color)
        instance.save()
        return instance
