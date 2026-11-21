from django.db import models
from uuid import uuid4

# Create your models here.
class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    content = models.TextField()
    created_at =  models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title