from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpRequest, QueryDict
from doge.models import Response
from doge.models import Response2
from doge.models import ResponseGood
from doge.models import ResponseBad
from doge.models import ResponseNeutral
from doge.models import GoodFortune
from doge.models import NeutralFortune
from doge.models import BadFortune
from doge.models import DefaultFortune
import random

def index(request):
    Entry11 = Response.objects.order_by('?')[0:1]
    for word11 in Entry11:
    	word11 = word11.text
    Entry21 = Response.objects.order_by('?')[0:1]
    for word21 in Entry21:
    	word21 = word21.text
    Entry31 = Response.objects.order_by('?')[0:1]
    for word31 in Entry31:
    	word31 = word31.text
    	
    Entry12 = DefaultFortune.objects.order_by('?')[0:1]
    for word12 in Entry12:
    	word12 = word12.text
    Entry22 = DefaultFortune.objects.order_by('?')[0:1]
    for word22 in Entry22:
    	word22 = word22.text
    Entry32 = DefaultFortune.objects.order_by('?')[0:1]
    for word32 in Entry32:
    	word32 = word32.text
    	
    return render_to_response('index.html', locals())
    
    
    
def submit(request):
    Year = request.GET.get('Year', '')
    FirstName = request.GET.get('FirstName', '')
    Randomize = random.randint(1,10)
    
    entries1 = Response.objects.order_by('?')[0:1]
    for e11 in entries1:
        e11 = e11.text
    entries2 = Response.objects.order_by('?')[0:1]
    for e22 in entries2:
        e22 = e22.text
    entries3 = Response.objects.order_by('?')[0:1]
    for e33 in entries3:
        e33 = e33.text
    
    if Randomize > 7:
       entries11 = ResponseGood.objects.order_by('?')[0:1]
       entries22 = ResponseGood.objects.order_by('?')[0:1]
       entries33 = ResponseGood.objects.order_by('?')[0:1]
    
    elif Randomize < 4:
        entries44 = ResponseBad.objects.order_by('?')[0:1]
        entries55 = ResponseBad.objects.order_by('?')[0:1]
        entries66 = ResponseBad.objects.order_by('?')[0:1]
    
    else:
       entries77 = ResponseNeutral.objects.order_by('?')[0:1]
       entries88 = ResponseNeutral.objects.order_by('?')[0:1]
       entries99 = ResponseNeutral.objects.order_by('?')[0:1]
    
    if Randomize > 7:
       entriesgood = GoodFortune.objects.order_by('?')[0:1]
       for e1 in entriesgood:
           e1 = e1.text
       entriesgood2 = GoodFortune.objects.order_by('?')[0:1]
       for e2 in entriesgood2:
           e2 = e2.text
       entriesgood3 = GoodFortune.objects.order_by('?')[0:1]
       for e3 in entriesgood3:
           e3 = e3.text
           
    elif Randomize <  4:  
       entriesbad = BadFortune.objects.order_by('?')[0:1]
       for e1 in entriesbad:
           e1 = e1.text
       entriesbad2 = BadFortune.objects.order_by('?')[0:1]
       for e2 in entriesbad2:
           e2 = e2.text
       entriesbad3 = BadFortune.objects.order_by('?')[0:1]
       for e3 in entriesbad3:
           e3 = e3.text
           
    
    else: 
       entriesneutral = NeutralFortune.objects.order_by('?')[0:1]
       for e1 in entriesneutral:
           e1 = e1.text
       entriesneutral2 = NeutralFortune.objects.order_by('?')[0:1]
       for e2 in entriesneutral2:
           e2 = e2.text
       entriesneutral3 = NeutralFortune.objects.order_by('?')[0:1]
       for e3 in entriesneutral3:
           e3 = e3.text
  
    return render_to_response('submit.html', locals())