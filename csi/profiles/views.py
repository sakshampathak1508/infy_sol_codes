from django.shortcuts import render
from .models import Player,Referee,Coache,Association,Club
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import json
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import requests
# Create your views here.

def profile(request,slug):
    player = Player.objects.all().filter(gender=slug).order_by("name")
    params = {'player':player}
    return render(request,"profiles/profile.html",params)

def profileview(request,myid,slug,gender):
    p_view = Player.objects.filter(id=myid,gender=gender,slug=slug)
    params = {'p_view':p_view[0]}
    return render(request,"profiles/profileview.html",params)

def allrefs(request):
    refs = Referee.objects.all().order_by("name")
    params = {'refs':refs}
    return render(request,"profiles/referees.html",params)

def allcoach(request):
    coach = Coache.objects.all().order_by("name")
    params = {'coach':coach}
    return render(request,"profiles/coaches.html",params)

def refview(request,myid,slug):
    ref_view = Referee.objects.filter(id=myid,slug=slug)
    params = {'ref_view':ref_view[0]}
    return render(request,"profiles/refereeview.html",params)


def coachview(request,myid,slug):
    coach_view = Coache.objects.filter(id=myid,slug=slug)
    params = {'coach_view':coach_view[0]}
    return render(request,"profiles/coachview.html",params)
    
def associations(request):
    ass = Association.objects.all().order_by('short_name')
    params = {'ass':ass}
    return render(request,"profiles/associations.html",params)

def associationsview(request,myid,slug):
    ass_view = Association.objects.filter(id=myid,slug=slug)
    params = {'ass_view':ass_view[0]}
    return render(request,"profiles/associationsview.html",params)
    
def clubs(request):
    club = Club.objects.all().order_by('short_name')
    params = {'club':club}
    return render(request,"profiles/clubs.html",params)

def clubsview(request,myid,slug):
    club = Club.objects.filter(id=myid,slug=slug)
    params = {'club':club[0]}
    return render(request,"profiles/clubsview.html",params)
    
def playerFormRequest(request):
    if request.method == "POST" and request.FILES['img']:    
        f_name = request.POST['first-name']
        l_name = request.POST['last-name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        city = request.POST['city']
        state = request.POST['st']
        rep = request.POST['rep']
        hbsnooker = request.POST['hbsnooker']
        hbbilliards = request.POST['hbbilliards']
        cue = request.POST['cue']
        prac = request.POST['prac']
        emp = request.POST['emp']
        phone = request.POST['phone']
        email = request.POST['email']
        otheracts = request.POST['otheracts']
        awards = request.POST['awards']
        achive = request.POST['achive']
        content = request.POST['content']
        insta_url = request.POST['insta']
        fb_url = request.POST['fb']
        tweet_url = request.POST['tweet']
        image = request.FILES['img']
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
            send_mail("PLayer Profile Request", f''' Name :- {f_name} {l_name}\n Phone:- {phone}\n email id:- {email}\n city:- {city}\n state:- {state}''', email ,['contactus@cuesportsindia.com'])
            player = Player(name=f_name+" "+l_name,slug=f_name+"-"+l_name,breaks=hbbilliards+" (Billiards); "+hbsnooker+" (Snooker)",gender=gender,awards=awards,highest_achievements=achive,DOB=dob,image=image,city=city,state=state,highest_break_billiards=hbbilliards+" Billiards",highest_break_snooker=hbsnooker+" Snooker",cue_in_use=cue,practice_at=prac,represents=rep,Employed_with=emp,other_activites=otheracts,content=content,Instagram_url=insta_url,Facebook_url=fb_url,Twitter_url=tweet_url)
            player.save()
            return render(request, "profiles/playerform.html",{'thank':thank})
        else:
            return HttpResponse('Please Check the captcha and try again')
    else:
        return render(request,"profiles/playerform.html")
    return render(request,"profiles/playerform.html")
