from django.shortcuts import render
from .models import Tournament
from home.models import Sponser
from django.http import HttpResponse
import datetime
import json
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import requests
from django.core.files.storage import FileSystemStorage

def tournament(request):
    try:
        r = range(int(datetime.date.today().year),2005,-1)
        if request.method == 'POST':
            y = request.POST.get('year','')
            # filter(tournament_year=y)
            tour = Tournament.objects.all().filter(tournament_year=y,approved=True).order_by("-tournament_startdate")
            spons = Sponser.objects.all()
            params = {'tour': tour,'spons':spons,'y':y,'r':r}
            return render(request,"tournament/tournament.html",params)
        else:
            y = datetime.date.today().year
            tour = Tournament.objects.all().filter(tournament_year=y,approved=True).order_by("-tournament_startdate")
            spons = Sponser.objects.all()
            params = {'tour': tour, 'spons':spons ,'y':y,'r':r}
            return render(request,"tournament/tournament.html",params)
    except:
        return HttpResponse('Please enable the cookies of your browser')
        

def tourview(request,myid,slug,year):
    t_view = Tournament.objects.filter(id=myid,slug=slug,tournament_year=year,approved=True)
    spons = Sponser.objects.all()[0:6]
    spons1 = Sponser.objects.all()[6:]
    params = {'t_view': t_view[0],'spons':spons,'spons1':spons1}
    return render(request,"tournament/tourview.html",params)

def tour_eve_category(request,slug):
    tour = Tournament.objects.all().filter(event_category=slug,approved=True).order_by("-tournament_startdate")
    e = slug
    spons = Sponser.objects.all()
    params = {'tour': tour,'spons':spons,'e':e}
    return render(request,"tournament/tour_event_category.html",params)

def tour_sport_category(request,slug):
    tour = Tournament.objects.all().filter(sports_category=slug,approved=True).order_by("-tournament_startdate")
    e = slug
    spons = Sponser.objects.all()
    params = {'tour': tour,'spons':spons,'e':e}
    return render(request,"tournament/tour_sport_category.html",params)
    
def tour_form(request):
    if (request.method == "POST" and (request.FILES['image1'] or request.FILES['image2'] or request.FILES['image3']) ):    
        f_name =  request.POST.get('fname')
        l_name =  request.POST.get('lname')
        phone =   request.POST.get('phone')
        email =   request.POST.get('email')
        tour_name = request.POST.get('tour-name')
        event_cat = request.POST.get('event-cat')
        sport_cat = request.POST.get('sport-cat')
        city =      request.POST.get('city')
        state =     request.POST.get('st')
        venue =     request.POST.get('venue')
        start_date =request.POST.get('start-date')
        end_date =  request.POST.get('end-date')
        last_doe =  request.POST.get('last-doe')
        #money
        currency =  request.POST.get('currency')
        entry_fee = request.POST.get('entry-fee')
        
        pm_total =  request.POST.get('pm-total')
        pm_winner = request.POST.get('pm-winner')
        pm_runner = request.POST.get('pm-runner')
        pm_semi =   request.POST.get('pm-semi')
        pm_quad =   request.POST.get('pm-quad')
        pm_16 =     request.POST.get('pm-16')
        pm_32 =     request.POST.get('pm-32')
        pm_hb1 =    request.POST.get('pm-hb1')
        pm_hb2 =    request.POST.get('pm-hb2')
        pm_hb3 =    request.POST.get('pm-hb3')
        # formats
        group = request.POST.get('group')
        pre_knock = request.POST.get('pre-knock')
        format_64 = request.POST.get('format-64')
        format_32 = request.POST.get('format-32')
        format_16 = request.POST.get('format-16')
        format_quat = request.POST.get('format-quat')
        format_semi = request.POST.get('format-semi')
        format_final = request.POST.get('format-final')

        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')

        add_info = request.POST.get('add-info')

        # contact info

        name1 =  request.POST.get('name1')
        phone1 = request.POST.get('phone1')
        name2 =  request.POST.get('name2')
        phone2 = request.POST.get('phone2') 
        name3 =  request.POST.get('name3') 
        phone3 = request.POST.get('phone3') 
        name4 =  request.POST.get('name4')
        phone4 = request.POST.get('phone4')
        slug = tour_name.replace(" ","-")
        clientkey = request.POST['g-recaptcha-response']
        secretkey = '6LcluBEaAAAAAOrny9M6GMed67hFSCk1_k3-raEe'
        captchaData = {
            'secret': secretkey,
            'response': clientkey 
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchaData)
        response = json.loads(r.text)
        verify = response['success']
        if verify:
            tour = Tournament(tournament_name=tour_name,slug=slug,event_category=event_cat,sports_category=sport_cat,tournament_city=city,tournament_state=state,tournament_venue=venue,currency=currency,entry_fee=entry_fee,prize_money_total=pm_total,prize_money_winner=pm_winner,prize_money_runner_up=pm_runner,prize_money_semi_finalist=pm_semi,prize_money_quarter_finalist=pm_quad,prize_money_last16=pm_16,prize_money_last32=pm_32,prize_money_highestbreak_1=pm_hb1,prize_money_highestbreak_2=pm_hb2,prize_money_highestbreak_3=pm_hb3,tournament_image1=image1,tournament_image2=image2,tournament_image3=image3,tournament_startdate=start_date,tournament_enddate=end_date,last_date_of_entry=last_doe,name1=name1,name2=name2,name3=name3,name4=name4,contact_num1=phone1,contact_num2=phone2,contact_num3=phone3,contact_num4=phone4,details=add_info,tournament_year=start_date[0:4],group_Stage=group,prelim_Knockout=pre_knock,last64_Stage=format_64,last32_Stage=format_32,last16_Stage=format_16,quarter_Finals=format_quat,semi_Finals=format_semi,FINAL=format_final)
            tour.save()
            thank = True
            send_mail("Tournament Request,A request for a adding a tournament is raised please take a look", f''' Name :- {f_name} {l_name}\n Phone:- {phone}\n email id:- {email}\n Tournament name:- {tour_name}\n''', email ,['contactus@cuesportsindia.com'])
            return render(request, "tournament/tour_form.html",{'thank':thank})
        else:
            return HttpResponse('Please Check the captcha and try again')
    else:
            return render(request, "tournament/tour_form.html")
    return render(request, "tournament/tour_form.html")
