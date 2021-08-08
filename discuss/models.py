from django.db import models
from django.conf import settings
from django.contrib.auth.models import  User, auth

# Create your models here.

# class stock_model(models.Model):
#     stock = models.TextField()

# class chat(models.Model):
#     chatt = models.ForeignKey(stock_model ,related_name="comments", on_delete= models.CASCADE , null= True)

#     user = models.ForeignKey(User, on_delete=models.CASCADE , null= True  )
#     pub_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
#     content = models.TextField()
    
#     def __aiter__(self):
#         return "%s - %s" % (self.chat.content , self.name)




class TutorialCategory(models.Model):

    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)

    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_title2 = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published')
    #https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)
    def __str__(self):
        return self.tutorial_title                

