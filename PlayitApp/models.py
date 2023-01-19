from django.db import models

# Create your models here.
class Videos(models.Model):
    Video_Tittle = models.CharField(max_length=25, default='')
    Video_Description = models.TextField(default='')
    Video_Thumbline = models.FileField(upload_to='VideoThumblines')
    Video = models.FileField(upload_to='Vidoes')

    def __str__(self):
        return self.Video_Tittle
