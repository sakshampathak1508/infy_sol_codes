from django.db import models

# Create your models here.
GENDER_CHOICES=(
    ('Men','MALE'),
    ('Women','FEMALE'),
)

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120,default="")
    slug = models.SlugField(max_length=120)
    breaks = models.CharField(max_length=200,default="") 
    gender = models.CharField(max_length=50, choices = GENDER_CHOICES,default="")
    awards = models.TextField(blank=True)
    highest_achievements = models.TextField(blank=True)
    DOB = models.DateField()
    image = models.ImageField(upload_to='profile/images')
    city = models.CharField(max_length=50,default="")
    state = models.CharField(max_length=50,default="")
    highest_break_billiards = models.CharField(max_length=100,default="",blank=True)
    highest_break_snooker = models.CharField(max_length=100,default="",blank=True)
    cue_in_use = models.CharField(max_length=200,default="")
    practice_at = models.CharField(max_length=300,default="",blank=True)
    represents = models.TextField(blank=True)
    Employed_with = models.CharField(max_length=200,default="",blank=True)
    other_activites = models.TextField(blank=True)
    content = models.TextField()
    Instagram_url = models.URLField(blank=True)
    Facebook_url = models.URLField(blank=True)
    Twitter_url = models.URLField(blank=True)
    is_approved = models.BooleanField(blank=True,default=False)

    def __str__(self):
        return self.name 

class Coache(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120,default="")
    slug = models.SlugField(max_length=120)
    caption_at_front = models.CharField(max_length=50,default="")
    image = models.ImageField(upload_to='profile/images')
    DOB = models.DateField()
    award = models.TextField()
    certificate = models.CharField(max_length=100,default="",blank=True) 
    city = models.CharField(max_length=50,default="")
    state = models.CharField(max_length=50,default="")
    experience = models.CharField(max_length=100,default="",blank=True)
    experties = models.TextField(blank=True)
    formal_training = models.TextField(blank=True)
    Employed_with = models.CharField(max_length=200,default="",blank=True)
    other_activites = models.TextField(blank=True)
    content  = models.TextField()
    Instagram_url = models.URLField(blank=True)
    Facebook_url = models.URLField(blank=True)
    Twitter_url = models.URLField(blank=True)

    def __str__(self):
        return self.name 

class Referee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120,default="")
    slug = models.SlugField(max_length=120)
    caption_at_front = models.CharField(max_length=50,default="")
    DOB = models.DateField()
    image = models.ImageField(upload_to='profile/images')
    certificate = models.CharField(max_length=100,default="",blank=True) 
    city = models.CharField(max_length=50,default="")
    state = models.CharField(max_length=50,default="")
    experience_in_national = models.CharField(max_length=100,default="",blank=True)
    experience_in_international = models.CharField(max_length=100,default="",blank=True)
    experties = models.TextField(blank=True)
    Employed_with = models.CharField(max_length=200,default="",blank=True)
    other_activites = models.TextField(blank=True)
    content  = models.TextField()
    Instagram_url = models.URLField(blank=True)
    Facebook_url = models.URLField(blank=True)
    Twitter_url = models.URLField(blank=True)
    class Meta:
         verbose_name = "Referee"
         verbose_name_plural = "Referee's"

    def __str__(self):
        return self.name
        
class Position(models.Model):
    id = models.AutoField(primary_key=True)
    association_name = models.CharField(max_length=100,blank=True,default="")
    position_name = models.CharField(max_length=100,blank=True,default="")
    position_fill = models.CharField(max_length=100,blank=True,default="")

    def __str__(self):
        return self.association_name+' '+self.position_name

class Association(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default="")
    short_name = models.CharField(max_length=100,default="")
    slug = models.SlugField(max_length=150)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100,default="",blank=True)
    state = models.CharField(max_length=100,default="",blank=True)
    phone_number = models.CharField(max_length=100,default="",blank=True)
    mobile_number = models.CharField(max_length=100,default="",blank=True)
    email = models.CharField(max_length=100,default="",blank=True)
    image = models.ImageField(upload_to='profile/images')
    image2 = models.ImageField(upload_to='profile/images',blank=True)
    position = models.ManyToManyField(Position,blank=True, null=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.name
        
class Club(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default="")
    short_name = models.CharField(max_length=100,default="")
    slug = models.SlugField(max_length=150)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100,default="",blank=True)
    state = models.CharField(max_length=100,default="",blank=True)
    email1 = models.CharField(max_length=100,default="",blank=True)
    email2 = models.CharField(max_length=100,default="",blank=True)
    phone_number1 = models.CharField(max_length=100,default="",blank=True)
    phone_number2 = models.CharField(max_length=100,default="",blank=True)
    phone_number3 = models.CharField(max_length=100,default="",blank=True)
    timing_from = models.TimeField(null=True,blank=True)
    timing_to = models.TimeField(null=True,blank=True)
    snooker_tables = models.CharField(max_length=100,default="",blank=True)
    pool_tables = models.CharField(max_length=100,default="",blank=True)
    carrom_tables = models.CharField(max_length=100,default="",blank=True)
    manager_name = models.CharField(max_length=100,default="",blank=True)
    entry_system = models.CharField(max_length=100,default="",blank=True)
    logo = models.ImageField(upload_to='profile/images')
    image1 = models.ImageField(upload_to='profile/images',blank=True)
    image2 = models.ImageField(upload_to='profile/images',blank=True)
    image3 = models.ImageField(upload_to='profile/images',blank=True)
    insta_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    content = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
