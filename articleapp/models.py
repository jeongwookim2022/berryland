from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# 1. Reason why related_name = 'article'
# - User's object approaches Article using 'related_name'.
# 2. writer = ~(on_delete=SET_NULL)
# - Articles will stay although User object is deleted.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_when = models.DateField(auto_created=True, null=True)

    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)