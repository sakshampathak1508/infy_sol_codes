from django.db import models
from datetime import datetime

NEWS_CATEGORY = (
    ('Latest','LATEST'),
    ('Featured', 'FEATURED'),
)
# Create your models here.
class Newse(models.Model):
    id = models.AutoField(primary_key=True)
    news_title = models.CharField(max_length=200,default="")
    slug = models.SlugField(max_length=200)
    views = models.IntegerField(default=0)
    news_category = models.CharField(max_length=50, choices = NEWS_CATEGORY,default="")
    news_image = models.ImageField(upload_to='news/images',blank=True)
    news_writer = models.CharField(max_length=100,default="")
    content = models.TextField()
    news_year = models.CharField(max_length=10,default="")
    timestamp  = models.DateTimeField(null=True)
    
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
    
    def __str__(self):
        return self.news_title