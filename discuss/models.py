from django.db import models
from django.conf import settings
from django.contrib.auth.models import  User, auth

# Create your models here.

class stock_model(models.Model):
    stock = models.TextField()

class chat(models.Model):
    chatt = models.ForeignKey(stock_model ,related_name="comments", on_delete= models.CASCADE , null= True)

    user = models.ForeignKey(User, on_delete=models.CASCADE , null= True  )
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    content = models.TextField()
    
    def __aiter__(self):
        return "%s - %s" % (self.chat.content , self.name)