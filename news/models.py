from django.db import models
from django.conf import settings
from helpers.models import BaseModel

# Create your models here.

class News(BaseModel):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    text = models.TextField()
    date_published = models.DateField(auto_now_add=True, db_index=True)
    
    def __str__(self):
        return self.title