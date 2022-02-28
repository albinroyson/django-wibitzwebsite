import json
from django.http import HttpResponse
from django.shortcuts import render



from web.models import Customer, Subscribe,Feature

# Create your views here.
def index(request):
    customers=Customer.objects.all()
    features=Feature.objects.all()
    context ={
    
        "customers": customers,
        "features":features
    }

    return render(request,"index.html",context=context)
   
def subscribe(request):
    email=request.POST.get("email")

    if not Subscribe.objects.filter(email=email).exists():

        Subscribe.objects.create(
        email=email
        )
        response_data={
            "status":"success",
            "title":"successfully registerd",
            "message":"you subscribed to our newsletter successfuly"
        }
    else:
        response_data={
            "status":"error",
            "title":"you are already subscribed",
            "message":"already a member"
        }



    return HttpResponse(json.dumps(response_data),content_type="application/javascript")