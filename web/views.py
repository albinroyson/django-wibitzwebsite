import json
from django.http import HttpResponse
from django.shortcuts import render



from web.models import Customer, Marketing, Subscribe,Feature,Video,Profile,Studio,Blog

# Create your views here.
def index(request):
    customers=Customer.objects.all()
    features=Feature.objects.all()
    videos=Video.objects.all()
    profiles=Profile.objects.all()
    marketings=Marketing.objects.all()
    studios=Studio.objects.all()
    blogs=Blog.objects.all()

    context ={
    
        "customers": customers,
        "features":features,
        "videos":videos,
        "profiles":profiles,
        "marketings":marketings,
        "studios":studios,
        "blogs":blogs
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
    elif email=="":
        response_data={
            "status":"error",
            "title":"enter email",
            "message":"Please type email"
        }

    else:
        response_data={
            "status":"error",
            "title":"you are already subscribed",
            "message":"already a member"
        }
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")