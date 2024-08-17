from django.db import models
# Create your models here.

SPORT_CHOICES = (
    ('Billiards','BILLIARDS'),
    ('Snooker', 'SNOOKER'),
    ('6REDS/10REDS', '6REDS/10REDS'),
    ('Carrom/Pool','CARROM/POOL'),
)

RANKING_CHOICES = (
    ('Men-Ranking-Billiards','Men-Ranking-Billiards'),
    ('Men-Ranking-Snooker', 'Men-Ranking-Snooker'),
    ('Women-Ranking-Billiards', 'Women-Ranking-Billiards'),
    ('Women-Ranking-Snooker','Women-Ranking-Snooker'),
)

TITLE_CHOICES = (
    ('National','National'),
    ('International','International'),
)

class Writing_About(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="")
    content_about = models.TextField(blank=True)
    content_billiards = models.TextField(blank=True)
    content_snooker = models.TextField(blank=True)
    content_pool = models.TextField(blank=True)
    content_carrom = models.TextField(blank=True)
    content_general_tips = models.TextField(blank=True)
    content_support_us = models.TextField(blank=True)
    content_site_terms = models.TextField(blank=True)
    class Meta:
        verbose_name = "Writing About"
        verbose_name_plural = "Writing Abouts"
    
    def __str__(self):
        return self.name

class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="")
    slug = models.SlugField(max_length=100)
    image_at_front = models.ImageField(upload_to="home/images")
    image_at_back = models.ImageField(upload_to="home/images")
    caption = models.CharField(max_length=50,default="",blank=True)
    content_equipments = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Sponser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    Banner = models.ImageField(upload_to="home/images")
    url = models.URLField(max_length=200,blank=True)
    file = models.FileField(upload_to="home/files",blank=True)
    def __str__(self):
        return self.name

class Rule(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image_at_front = models.ImageField(upload_to="home/images")
    image_at_back = models.ImageField(upload_to="home/images")
    caption = models.CharField(max_length=50,default="",blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Ranking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default="",blank=True)
    category = models.CharField(max_length=100,choices = RANKING_CHOICES,default="")
    image = models.ImageField(upload_to="home/images")
    top_rank = models.CharField(max_length=100,default="",blank=True)
    content = models.TextField(blank=True)
    content_extra = models.TextField(blank=True)
    
    def __str__(self):
        return self.category

# class Support(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100,default="",blank=True)
#     content = models.TextField(blank=True)

class Champion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to="home/images")
    sport_name = models.CharField(max_length=100,choices = SPORT_CHOICES,default="")
    event = models.CharField(max_length=100,default="")
    profile_url = models.URLField(max_length=200,blank=True)

    def __str__(self):
        return self.name +' '+ self.sport_name

class Title(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default="",blank=True)
    slug = models.SlugField(max_length=100)
    category = category = models.CharField(max_length=100,choices = TITLE_CHOICES,default="")
    image_at_front = models.ImageField(upload_to="home/images")
    image_at_back = models.ImageField(upload_to="home/images")
    caption = models.CharField(max_length=50,default="",blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100,default="",blank=True)
    slug = models.SlugField(max_length=100)
    author_name = models.CharField(max_length=100,default="",blank=True)
    image = models.ImageField(upload_to="home/images")
    content = models.TextField(blank=True)

    def __str__(self):
        return self.book_name
        
class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default="")
    amount = models.IntegerField(default=0)
    mobile_number = models.CharField(max_length=10,default="",blank=True)
    email = models.EmailField(default="",blank=True)
    city = models.CharField(max_length=100,default="",blank=True)
    state = models.CharField(max_length=100,default="",blank=True)
    entry_for = models.CharField(max_length=100,default="",blank=True)
    payment_status = models.CharField(max_length=100,default="Pending",blank=True)
    def __str__(self):
        return self.name