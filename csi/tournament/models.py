from django.db import models
from datetime import datetime
SPORT_CHOICES = (
    ('Billiards','BILLIARDS'),
    ('Snooker', 'SNOOKER'),
    ('6REDS', '6REDS'),
    ('10REDS','10REDS'),
    ('Pool','POOL'),
    ('Carrom','CARROM'),
    ('Cue-Sports','CUE SPORTS'),
)
EVENT_CHOICES = (
    ('IBSF','IBSF'),
    ('ACBS','ACBS'),
    ('National','NATIONAL'),
    ('Invitation','INVITATION'),
    ('OpenEntry','OPEN ENTRY'),
    ('Professional','PROFESSIONAL'),
    ('State','STATE'),
    ('Corporate','CORPORATE'),
)

CURRENCY_CHOICES=(
    ('INR','INR'),
    ('EUR','EUR'),
    ('USD','USD'),
    ('GBP','GBP'),
    ('AUD','AUD'),
)

class Tournament(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_name = models.CharField(max_length=200, default="")
    slug = models.SlugField(max_length=200)
    event_category = models.CharField(max_length=50, choices = EVENT_CHOICES,default="")
    sports_category = models.CharField(max_length=50, choices = SPORT_CHOICES,default="")
    tournament_venue = models.TextField()
    tournament_city = models.CharField(max_length=70,default="")
    tournament_state = models.CharField(max_length=70,default="")
    note1 = models.CharField(max_length=70,default="",blank=True)
    note2 = models.CharField(max_length=70,default="",blank=True)
    tournament_startdate = models.DateTimeField(null=True)
    tournament_enddate = models.DateTimeField(null=True)
    last_date_of_entry = models.DateTimeField(null=True,blank=True)
    tournament_year = models.CharField(max_length=10,default="")
    currency = models.CharField(max_length=50, choices =CURRENCY_CHOICES ,default="",blank=True)
    
    entry_fee =                     models.CharField(default="",blank=True,max_length=100)
    prize_money_total =             models.CharField(default="",blank=True,max_length=100)
    prize_money_winner =            models.CharField(default="",blank=True,max_length=100)
    prize_money_runner_up =         models.CharField(default="",blank=True,max_length=100)
    prize_money_semi_finalist =     models.CharField(default="",blank=True,max_length=100)
    prize_money_quarter_finalist =  models.CharField(default="",blank=True,max_length=100)
    prize_money_last16 =            models.CharField(default="",blank=True,max_length=100)
    prize_money_last32 =            models.CharField(default="",blank=True,max_length=100)
    prize_money_highestbreak_1 =    models.CharField(default="",blank=True,max_length=100)
    prize_money_highestbreak_2 =    models.CharField(default="",blank=True,max_length=100)
    prize_money_highestbreak_3 =    models.CharField(default="",blank=True,max_length=100)
    
    # bank details
    bank_name = models.CharField(max_length=200, default="",blank=True)
    account_name = models.CharField(max_length=200, default="",blank=True)
    account_number = models.PositiveBigIntegerField(default=0,blank=True)
    ifsc_code = models.CharField(max_length=15, blank=True)
    branch = models.CharField(max_length=200,blank=True)
    paytm_number = models.CharField(max_length=15,default="",blank=True)
    payment_url = models.URLField(blank=True,null=True)
    payment_note = models.TextField(blank=True)
    # format
    group_Stage = models.CharField(max_length=150,default="",blank=True)
    prelim_Knockout = models.CharField(max_length=150,default="",blank=True)
    last64_Stage = models.CharField(max_length=150,default="",blank=True)
    last32_Stage = models.CharField(max_length=150,default="",blank=True)
    last16_Stage = models.CharField(max_length=150,default="",blank=True)
    quarter_Finals = models.CharField(max_length=150,default="",blank=True)
    semi_Finals = models.CharField(max_length=150,default="",blank=True)
    FINAL = models.CharField(max_length=150,default="",blank=True)
    # contact details
    name1 = models.CharField(max_length=100,default="",blank=True)
    contact_num1 = models.CharField(max_length=15,default="",blank=True)
    name2 = models.CharField(max_length=100, default="",blank=True)
    contact_num2 = models.CharField(max_length=15,default="",blank=True)
    name3 = models.CharField(max_length=100, default="",blank=True)
    contact_num3 = models.CharField(max_length=15,default="",blank=True)
    name4 = models.CharField(max_length=100, default="",blank=True)
    contact_num4 = models.CharField(max_length=15,default="",blank=True)
    
    tournament_image1 = models.ImageField(upload_to='tournament/images')
    tournament_image2 = models.ImageField(upload_to='tournament/images',blank=True,null=True)
    tournament_image3 = models.ImageField(upload_to='tournament/images',blank=True,null=True)
    
    details = models.TextField(blank=True)
    disclaimer = models.TextField(blank=True)
    
    draw_name = models.CharField(max_length=200,default="",blank=True)
    draw_file = models.FileField(upload_to="tournament/files",blank=True)
    draw_url = models.URLField(blank=True,null=True)
    results_name = models.CharField(max_length=200,default="",blank=True)
    results_file = models.FileField(upload_to="tournament/files",blank=True)
    results_url = models.URLField(blank=True,null=True)
    
    draw2_name = models.CharField(max_length=200,default="",blank=True)
    draw2_file = models.FileField(upload_to="tournament/files",blank=True)
    draw2_url = models.URLField(blank=True,null=True)
    results2_name = models.CharField(max_length=200,default="",blank=True)
    results2_file = models.FileField(upload_to="tournament/files",blank=True)
    results2_url = models.URLField(blank=True,null=True)
    
    draw3_name = models.CharField(max_length=200,default="",blank=True)
    draw3_file = models.FileField(upload_to="tournament/files",blank=True)
    draw3_url = models.URLField(blank=True,null=True)
    results3_name = models.CharField(max_length=200,default="",blank=True)
    results3_file = models.FileField(upload_to="tournament/files",blank=True)
    results3_url = models.URLField(blank=True,null=True)
    
    draw4_name = models.CharField(max_length=200,default="",blank=True)
    draw4_file = models.FileField(upload_to="tournament/files",blank=True)
    draw4_url = models.URLField(blank=True,null=True)
    results4_name = models.CharField(max_length=200,default="",blank=True)
    results4_file = models.FileField(upload_to="tournament/files",blank=True)
    results4_url = models.URLField(blank=True,null=True)
    
    draw5_name = models.CharField(max_length=200,default="",blank=True)
    draw5_file = models.FileField(upload_to="tournament/files",blank=True)
    draw5_url = models.URLField(blank=True,null=True)
    results5_name = models.CharField(max_length=200,default="",blank=True)
    results5_file = models.FileField(upload_to="tournament/files",blank=True)
    results5_url = models.URLField(blank=True,null=True)
    
    current_status = models.CharField(max_length=50,default="")
    hide_from_concluded = models.BooleanField(default=False)
    collecting_fee = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.tournament_name
        
class Registration_Fee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="",max_length=100)
    city = models.CharField(default="",max_length=50)
    state = models.CharField(default="",max_length=50)
    email = models.EmailField(default="")
    phone_no = models.CharField(default="",max_length=15) 
    event_name = models.CharField(default="",max_length=200)
    slug = models.SlugField(max_length=250,unique=True)
    entry_fee = models.IntegerField(default=0)
    payment_status = models.CharField(default="",max_length=50)
    
    class Meta:
        verbose_name = "Registration Fees"
        verbose_name_plural = "Registration Fees"