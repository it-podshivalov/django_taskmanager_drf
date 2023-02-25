from django.db import models
from django.conf import settings
from datetime import datetime
from django.urls import reverse

class Project(models.Model):
    Name = models.CharField(max_length=300)

    Description = models.CharField(max_length=5000, null=True)

    Author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="author_of_project",
        help_text="Автор проекта",
    )

    class Meta:
        ordering = ["Name"]

    def get_absolute_url(self):
        return reverse("project", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.Name       

class Task(models.Model):

    Name = models.CharField(max_length=300, help_text="Название задачи")

    Description = models.CharField(max_length=5000, null=True, help_text="Описание")

    CreationTime = models.DateTimeField(
        editable=False, auto_now_add=True, help_text="Время создания задачи", verbose_name='Creation Time'
    )

    DeadlineForCompleting = models.DateTimeField(
        null=True, blank=True, default=None, help_text="Срок выполнения задачи", verbose_name='Deadline'
    )

    CompletionTime = models.DateTimeField(
        null=True, default=None, blank=True, help_text="Время завершения задачи", verbose_name='Completion Time'
    )

    Project = models.ForeignKey(
        to="TaskManager.Project",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="task_by_project",
        help_text="Проект",
    )

    Executor = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="executor_of_task",
        help_text="Исполнитель задания",
        default=None,
    )

    Author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="author_of_task",
        help_text="Автор задания",

    )

    Status = models.ForeignKey(
        to="TaskManager.Status",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="status",
        help_text="Status",
    )

    def set_completiontime(self):
        if self.Status == 'Completed':
            self.CompletionTime = datetime.now()            
            return self.CompletionTime
        else:
            self.CompletionTime = None
            return self.CompletionTime
    set_completiontime_ = property(set_completiontime)

    def set_status(self):
        if not self.Executor:
            self.Status = Status.objects.get(Name="Not at work")
            return self.Status
        else:
            return self.Status            
    set_status_ = property(set_status)

    def get_absolute_url(self):
        return reverse("task", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs) -> None:
        self.CompletionTime = self.set_completiontime_
        self.Status = self.set_status_   
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.Name}"        

class Status(models.Model):

    # STATUS_CHOICES = (
    # ("Not at work", "Not at work"),
    # ("Assigned", "Assigned"),
    # ("At work", "At work"),
    # ("Completed", "Completed"),
    # )

    Name = models.CharField(
        max_length=300,
        blank=True,
        null=False,
        help_text="Статус выполнения",
        )

    # parent_status = models.ForeignKey(  # связь внешним ключом
    #     to="self",  # на эту же таблицу Category
    #     on_delete=models.SET_NULL,  # при удалении категории НЕ удалится все поддерево категорий, просто поставится null где надо
    #     blank=True,
    #     null=True,  # Может не быть родительской категории
    #     related_name="substatuses",  # имя, по которому из экземпляра родительской категории можно вытащить подкатегории
    #     help_text="Родительская категория",  # текст для человека
    # )           

    class Meta:
        verbose_name_plural = "Statuses"

    def get_absolute_url(self):
        return f'/task/{self}/'  

    def __str__(self) -> str:
        return self.Name 

# try:
#     Status.objects.get(Name="Not at work")
# except:
#     Status(Name="Not at work").save()
#     Status(Name="Assigned").save()
#     Status(Name="At work").save()
#     Status(Name="Completed").save()
