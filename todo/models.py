from datetime import timezone
from django.db import models
from django.utils import timezone

# Create your models here.
now = timezone.now()

# タスクに登録する内容
class Todo(models.Model):
    title = models.CharField('タスク名', max_length=30)
    description = models.TextField('詳細', blank=True)
    deadline = models.DateField('締切', default=now)
    
    def __str__(self):
        return self.title
    
