from django.shortcuts import render
from .models import Newse
from home.models import Sponser
import datetime
# Create your views here.
def news(request):
    r = range(int(datetime.date.today().year),2005,-1)
    if request.method == 'POST':
        y = request.POST.get('year','')
        # filter(tournament_year=y)
        news = Newse.objects.all().filter(news_year=y).order_by("-timestamp")
        spons = Sponser.objects.all()
        params = {'news': news,'spons':spons,'y':y,'r':r}
        return render(request,"news/news.html",params)
    else:
        y = datetime.date.today().year
        news = Newse.objects.all().filter(news_year=y).order_by("-timestamp")
        spons = Sponser.objects.all()
        params = {'news': news, 'spons':spons ,'y':y,'r':r}
        return render(request,"news/news.html",params)

def newsview(request,myid,year,slug):
    news_view = Newse.objects.filter(id=myid,news_year=year,slug=slug).first()
    news_view.views = news_view.views + 1
    news_view.save()
    spons = Sponser.objects.all()
    params = {'news_view':news_view,'spons':spons}
    return render(request,"news/newsview.html",params)