from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from tournament.models import Tournament,Registration_Fee
from news.models import Newse
from django.contrib import messages 
from django.core.mail import send_mail,EmailMessage
from django.views.decorators.csrf import csrf_exempt
from .models import Sponser,Writing_About,Ranking,Rule,Champion,Title,Book,Equipment,Rule,Payment
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from datetime import date
import json
import requests
from PayTm import Checksum
MERCHANT_KEY = '!ASz9uCI_YEFkdys'
def index(request):
    count = 0
    today = datetime.now()
    tour = Tournament.objects.all().filter(approved=True).order_by("tournament_startdate")
    tour_ongoing = Tournament.objects.all().filter(approved=True).order_by("-tournament_startdate")
    tour_concluded = Tournament.objects.all().filter(approved=True).order_by("-tournament_enddate")
    champs_billiards = Champion.objects.all().filter(sport_name='Billiards')
    champs_snooker = Champion.objects.all().filter(sport_name='Snooker')
    champs_6RED_10RED = Champion.objects.all().filter(sport_name='6REDS/10REDS')
    champs_carrom_pool = Champion.objects.all().filter(sport_name='Carrom/Pool')
    # news_featured = {
    #     'news1' : Newse.objects.filter(news_category='Featured').order_by('-id')[0],
    #     # 'news2' : Newse.objects.filter(news_category='Featured').order_by('-id')[1],
    #     # 'news3' : Newse.objects.filter(news_category='Featured').order_by('-id')[2]
    # }
    news_featured = Newse.objects.filter(news_category='Featured').order_by('-id')[0],
    news_latest = Newse.objects.filter(news_category='Latest').order_by('-timestamp')[:4]
    spons = Sponser.objects.all()[0:6]
    spons1 = Sponser.objects.all()[6:]
    params = {'count':count,'spons':spons,'spons1':spons1,'tour': tour,'champs_billiards':champs_billiards,'champs_snooker':champs_snooker,
    'champs_6RED_10RED':champs_6RED_10RED,'champs_carrom_pool':champs_carrom_pool,
    'tour_concluded':tour_concluded,'tour_ongoing':tour_ongoing,'today':today,'news_featured':news_featured,'news_latest':news_latest}
    return render(request,"home/index.html",params)

def events(request):
    event = Tournament.objects.all().filter(approved=True).values('id','tournament_name','tournament_startdate').order_by("tournament_startdate")
    params = {'event': event}
    return render(request,"home/events.html",params)

def about(request):
    cont = Writing_About.objects.values('content_about')
    spons = Sponser.objects.all()
    params = {'cont':cont,'spons':spons}
    return render(request,"home/about.html",params)

def photographs(request):
    return render(request,"home/photographs.html")

def billiards(request):
    cont = Writing_About.objects.values('content_billiards')
    spons = Sponser.objects.all()
    params = {'cont':cont,'spons':spons}
    return render(request,"home/billiards.html",params)

def snooker(request):
    cont = Writing_About.objects.values('content_snooker')
    spons = Sponser.objects.all()
    params = {'cont':cont,'spons':spons}
    return render(request,"home/snooker.html",params)

def pool(request):
    cont = Writing_About.objects.values('content_pool')
    spons = Sponser.objects.all()
    params = {'cont':cont,'spons':spons}
    return render(request,"home/pool.html",params)

def carrom(request):
    cont = Writing_About.objects.values('content_carrom')
    spons = Sponser.objects.all()
    params = {'cont':cont,'spons':spons}
    return render(request,"home/carrom.html",params)



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        f_email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        country = request.POST.get('country', '')
        state = request.POST.get('state', '')
        city = request.POST.get('city', '')
        subject = request.POST.get('subject', '')
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
            thank = True
            send_mail(subject, f''' Name :- {name}\n Phone:- {phone}\n email id:- {f_email}\n country:- {country}\n state:- {state}\n city:- {city}\n\n {message}''', f_email ,['contactus@cuesportsindia.com'])
            return render(request, "home/contact.html",{'thank':thank})
        else:
            return HttpResponse('Please Check the captcha and try again')
    else:
        return render(request,"home/contact.html")

def rankings(request):
    rank = Ranking.objects.all().order_by("category")
    spons = Sponser.objects.all()
    params = {'rank':rank,'spons':spons}
    return render(request,"home/rankings.html",params)


def search(request):
    query=request.GET['query']
    if len(query)>78:
        allposts_news=Newse.objects.none()
        allposts_tour=Newse.objects.none()
    else:
        allpostsTitle= Newse.objects.filter(news_title__icontains=query)
        allpostsAuthor= Newse.objects.filter(news_writer__icontains=query)
        allpostsContent =Newse.objects.filter(content__icontains=query)
        allpostsYear =Newse.objects.filter(news_year__icontains=query)
        allpostsname = Tournament.objects.filter(tournament_name__icontains=query,approved=True)
        allpostsvenue = Tournament.objects.filter(tournament_venue__icontains=query,approved=True)
        allpostsyear = Tournament.objects.filter(tournament_year__icontains=query,approved=True)
        allpostsevent = Tournament.objects.filter(event_category__icontains=query,approved=True)
        allpostssport = Tournament.objects.filter(sports_category__icontains=query,approved=True)
        
        allposts_news=  allpostsTitle.union(allpostsContent, allpostsAuthor, allpostsYear)
        allposts_tour=  allpostsname.union(allpostsvenue,allpostsyear,allpostsevent,allpostssport )
    params={'allposts_news': allposts_news, 'allposts_tour':allposts_tour ,'query': query}
    return render(request, 'home/search.html', params)

def general_tips(request):
    cont = Writing_About.objects.values('content_general_tips')
    spons = Sponser.objects.all()
    params = {'cont':cont,'spons':spons}
    return render(request,"home/generaltips.html",params)

def equipments(request):
    equipment = Equipment.objects.all().order_by("id")
    params = {'equipment':equipment}
    return render(request,"home/equipments.html",params)
    
def equipments_view(request,myid,slug):
    equip_view = Equipment.objects.filter(id=myid,slug=slug)
    params = {'equip_view':equip_view[0]}
    return render(request,"home/equipments_view.html",params)
    
    
def rules(request):
    rule = Rule.objects.all().order_by("id")
    params = {'rule':rule}
    return render(request,"home/rules.html",params)
    
def rules_view(request,myid,slug):
    rule_view = Rule.objects.filter(id=myid,slug=slug)
    params = {'rule_view':rule_view[0]}
    return render(request,"home/rulesview.html",params)

def title(request,category):
    title = Title.objects.filter(category=category).order_by("id")
    params = {'title':title}
    return render(request,"home/title.html",params)

def title_view(request,myid,category,slug):
    t_view = Title.objects.filter(id=myid,category=category,slug=slug)
    params = {'t_view':t_view[0]}
    return render(request,"home/title_view.html",params)

def supportus(request):
    user = request.user
    if request.method=="POST":
        f_name = request.POST['name']
        l_name = request.POST['lname']
        city = request.POST['city']
        state = request.POST['st']
        country = request.POST['country']
        phone = request.POST['phone']
        email = request.POST['email']
        amount = request.POST['amount']
        clientkey = request.POST['g-recaptcha-response']
        secretkey = '6LcluBEaAAAAAOrny9M6GMed67hFSCk1_k3-raEe'
        captchaData = {
            'secret': secretkey,
            'response': clientkey 
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchaData)
        response = json.loads(r.text)
        verify = response['success']
        id = Checksum.__id_generator__()
        mail = EmailMessage("Support CSI", f''' Name :- {f_name} {l_name}\n  City:- {city}\n State:- {state}\n Country:- {country}\n Phone:- {phone}\n Email id:- {email}\n amount:- ₹{amount}\n\n Kindly Check For PayTm Conformation mail for payment as well\n''', email ,['contactus@cuesportsindia.com'])
        mail.send()
        if verify:
            param_dict = {
    
                    'MID': 'CueSpo41129861430942',
                    'ORDER_ID': str(id),
                    'TXN_AMOUNT': str(amount),
                    'CUST_ID': email,
                    'INDUSTRY_TYPE_ID': 'Retail109',
                    'WEBSITE': 'DEFAULT',
                    'CHANNEL_ID': 'WEB',
                    'CALLBACK_URL':'https://www.cuesportsindia.com/handlerequest/',
    
            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return render(request, 'home/paytm.html', {'param_dict': param_dict})
        else:
            return HttpResponse('Please Check the captcha and try again')
    supp = Writing_About.objects.all().values('content_support_us')
    spons = Sponser.objects.all()
    params = {'supp':supp,'spons':spons}
    return render(request, "home/supportus.html",params)


def books(request):
    book = Book.objects.all()
    params = {'book':book}
    return render(request,"home/books.html",params)

def rankingview(request,myid,slug):
    rank_view = Ranking.objects.filter(id=myid,category=slug)
    # spons = Sponser.objects.all()
    params = {'rank_view':rank_view[0]}
    return render(request,"home/rankingview.html",params)
    
def bookview(request,myid,slug):
    book_view = Book.objects.filter(id=myid,slug=slug)
    params = {'book_view':book_view[0]}
    return render(request,"home/bookview.html",params)

def site_terms(request):
    cont = Writing_About.objects.all().values('content_site_terms')
    params = {'cont':cont}
    return render(request,"home/siteterms.html",params)
    
@csrf_exempt    
def coachingprogform(request):
    today = date.today()
    if request.method=="POST":
        f_name = request.POST['first-name']
        l_name = request.POST['last-name']
        dob = request.POST['DOB']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['st']
        pin = request.POST['pin']
        phone = request.POST['phone']
        email = request.POST['email']
        edu = request.POST['edu']
        crime = request.POST['crime']
        menatalhealth = request.POST['menatalhealth']
        publichealth = request.POST['publichealth'] 
        exp = request.POST['exp']
        notice_achive = request.POST['notice-achive']
        pfrom = request.POST['pfrom']
        pto = request.POST['pto']
        reason = request.POST['reason']
        coach_exp = request.POST['coach_exp']
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
            thank = True
            send_mail("Coaches Training Program", f''' Name :- {f_name} {l_name}\n  DOB:- {dob}\n address:- {address} \n City:- {city}\n State:- {state}\n PIN Code:- {pin} Phone:- {phone}\n Email id:- {email}\n Educational Qualification:- {edu}\n Do you have any Criminal Record in India or any other country? :- {crime}\n  Are you suffering from Serious Mental Disorder? :- {menatalhealth}\n Are you suffering of any Infectious disease of Public Health Disorder? :- {publichealth}\n Explanation(if any):- {exp}\n Notable Achievement in Cue Sports :- {notice_achive}\n Playing Since:- From {pfrom} To {pto}\n Reason for Leaving:- {reason}\n Coaching Experience (if any)?:- {coach_exp}\n''', email ,['contactus@cuesportsindia.com'])
            return render(request, "home/coachingForm.html",{'thank':thank,'today':today})
        else:
            return HttpResponse('Please Check the captcha and try again')
    else:
        return render(request,"home/coachingForm.html",{'today':today})
    return render(request,"home/coachingForm.html",{'today':today})

def payment(request):
    amount = 2000
    if request.method == "POST":
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        mobile_number = request.POST.get('phone', '')
        entry_for = request.POST.get('entryfor', '')
        amount = 2000
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
            pay = Payment(name=fname+' '+lname,email=email,amount=amount,city=city,state=state,mobile_number=mobile_number,entry_for=entry_for)
            pay.save()
            id = pay.id
            param_dict = {
    
                    'MID': 'CueSpo41129861430942',
                    'ORDER_ID': str(pay.id),
                    'TXN_AMOUNT': str(amount),
                    'CUST_ID': email,
                    'INDUSTRY_TYPE_ID': 'Retail109',
                    'WEBSITE': 'DEFAULT',
                    'CHANNEL_ID': 'WEB',
                    'CALLBACK_URL':'https://www.cuesportsindia.com/handlerequest_tournament/',
    
            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return render(request, 'home/paytm.html', {'param_dict': param_dict})
        else:
            return HttpResponse('Please Check the captcha and try again')
    return render(request, "home/payment.html",{'amount': amount})

@csrf_exempt
def handlerequest_tournament(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    pay = Payment.objects.get(id=response_dict['ORDERID'])
    if verify:
        if response_dict['RESPCODE'] == '01':
            pay.payment_status = 'Paid'
            pay.save()
        else:
            pay.payment_status = 'Failed'
            pay.save()
    return render(request, 'home/paymentstatus.html', {'response': response_dict})
    
@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('done')
        else:
            print('not done')
    return render(request, 'home/paymentstatus.html', {'response': response_dict})

def bspai_form(request):
    user = request.user
    y = datetime.today().year
    if request.method=="POST":
        f_name = request.POST['name']
        l_name = request.POST['lname']
        father_name = request.POST['fname']
        image = request.FILES['img']
        dob = request.POST['dob']
        gender = request.POST['gender']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['st']
        pin = request.POST['pin']
        phone = request.POST['phone']
        email = request.POST['email']
        role = request.POST['role']
        state_awards = request.POST['state']
        nat_awards = request.POST['national']
        inter_awards = request.POST['international']
        prac = request.POST['prac']
        # fee = request.POST['fee']
        # disc = request.POST['feedisc']
        # if(fee=="Joining Fee"):
        #     amount = 10
        # elif(fee=="Annual Renewal"):
        #     amount = 5
        clientkey = request.POST['g-recaptcha-response']
        secretkey = '6LcluBEaAAAAAOrny9M6GMed67hFSCk1_k3-raEe'
        captchaData = {
            'secret': secretkey,
            'response': clientkey 
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchaData)
        response = json.loads(r.text)
        verify = response['success']
        # id = Checksum.__id_generator__()
        if verify:
            # param_dict = {
    
            #         'MID': 'CueSpo41129861430942',
            #         'ORDER_ID': str(id),
            #         'TXN_AMOUNT': str(amount),
            #         'CUST_ID': email,
            #         'INDUSTRY_TYPE_ID': 'Retail109',
            #         'WEBSITE': 'DEFAULT',
            #         'CHANNEL_ID': 'WEB',
            #         'CALLBACK_URL':'http://www.cuesportsindia.com/handlerequest/',
    
            # }
            # param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
            thank = True
            # mail = EmailMessage("BSPAI Membership", f''' Name :- {f_name} {l_name}\n  Father's Name:- {father_name}\n DOB:- {dob}\n Gender:- {gender}\n address:- {address} \n City:- {city}\n State:- {state}\n PIN Code:- {pin}\n Phone:- {phone}\n Practicing At:- {prac} \nEmail id:- {email}\n Role:- {role}\n Awards & Medals received:- \n\n \t State:- \n{state_awards}\n \n \tNational:- {nat_awards}\n\n \tInternational:- {inter_awards}\n Fee Type:- {fee}\n Amount:- ₹ {amount}\n\n Checking: I hereby pay ₹{amount} towards BSPAI Membership {fee}:- {disc}\n\n Kindly Check For PayTm Conformation mail for payment as well\n''', email ,['contactus@cuesportsindia.com'])
            mail = EmailMessage("BSPAI Membership", f''' Name :- {f_name} {l_name}\n  Father's Name:- {father_name}\n DOB:- {dob}\n Gender:- {gender}\n address:- {address} \n City:- {city}\n State:- {state}\n PIN Code:- {pin}\n Phone:- {phone}\n Practicing At:- {prac} \nEmail id:- {email}\n Role:- {role}\n Awards & Medals received:- \n\n \t State:- \n{state_awards}\n \n \tNational:- {nat_awards}\n\n \tInternational:- {inter_awards}\n \n''', email ,['contactus@cuesportsindia.com'])
            mail.attach(image.name,image.read(),image.content_type)
            mail.send()
            return render(request, "home/bspai_form.html",{'thank':thank})
            # return render(request, 'home/paytm.html', {'param_dict': param_dict})
        else:
            return HttpResponse('Please Check the captcha and try again')
    return render(request, "home/bspai_form.html")
    
def payment_events(request):
    if request.method == 'POST':
        f_name = request.POST['name']
        l_name = request.POST['lname']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        email = request.POST['email']
        amount = request.POST['amount_to_be']
        entry_for = request.POST['entryfor']
        slug = entry_for.replace(" ", "-")
        clientkey = request.POST['g-recaptcha-response']
        secretkey = '6LcluBEaAAAAAOrny9M6GMed67hFSCk1_k3-raEe'
        captchaData = {
            'secret': secretkey,
            'response': clientkey 
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchaData)
        response = json.loads(r.text)
        verify = response['success']
        id = Checksum.__id_generator__()
        if verify:
            param_dict = {
                    'MID': 'CueSpo41129861430942',
                    'ORDER_ID': str(id),
                    'TXN_AMOUNT': str(amount),
                    'CUST_ID': email,
                    'INDUSTRY_TYPE_ID': 'Retail109',
                    'WEBSITE': 'DEFAULT',
                    'CHANNEL_ID': 'WEB',
                    'CALLBACK_URL': f'https://www.cuesportsindia.com/handlerequest_events/{slug}',
            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
            pay = Registration_Fee(name=f_name+' '+l_name,city=city,state=state,phone_no=phone,email=email,entry_fee=amount,event_name=entry_for,slug=slug,payment_status='Pending')
            pay.save()
            return render(request, 'home/paytm.html', {'param_dict': param_dict})
        else:
            return HttpResponse('Please Check the captcha and try again')
    tour = Tournament.objects.all().filter(collecting_fee=True)
    params = {'tour':tour} 
    return render(request,"home/payment_events.html",params)


@csrf_exempt
def handlerequest_events(request,slug):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    pay = Registration_Fee.objects.get(slug=slug)
    # return HttpResponse(pay.slug)
    if verify:
        if response_dict['RESPCODE'] == '01':
            pay.payment_status = 'Paid'
            pay.save()
        else:
            pay.payment_status = 'Failed'
    return render(request, 'home/paymentstatus.html', {'response': response_dict})
    
    
