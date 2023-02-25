from rest_framework import serializers
from TaskManager.models import Task, Status, Project
from django.contrib.auth import get_user_model

class TaskSerializer(serializers.ModelSerializer):

    Author = serializers.CharField(source='Author.username', default=None)
    Project = serializers.CharField(default=None)
    Executor = serializers.CharField(source='Executor.username', default=None)
    Status = serializers.CharField(default=None)

    class Meta:
        model = Task
        read_only_fields = ["id", "CreationTime", "Author"]
        fields = read_only_fields + ["Name", "Description", "DeadlineForCompleting", "CompletionTime", "Project", "Executor", "Status"]

    def to_internal_value(self, data):
        if self.context["request"]._request.method == "POST":
            if not data.get("Executor"):
                data["Executor"] = None
        return super().to_internal_value(data)

    def create(self, validated_data):
        User = get_user_model()
        validated_data["Executor"] = User.objects.first()
        validated_data["Author"] = User.objects.first()
        return Task.objects.create(**validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["_request_data_method"] = self.context["request"]._request.method
        representation["_request_data_url"] = self.context["request"]._request.path
        return representation