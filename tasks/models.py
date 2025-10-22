from django.db import models
from django.contrib.auth.models import User
# from django.urls import reverse


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Task(TimeStampModel):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse('task_detail', args=[str(self.id)])
