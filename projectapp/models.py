from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=16, null=False)
    description = models.TextField(max_length=255, null=True)
    image = models.ImageField(upload_to='project/', null=False)
    created_when = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}: {self.title}"
