from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=250, db_index=True)
    text = models.TextField()
    label = models.BinaryField()

    def __srt__(self):
        return self.name