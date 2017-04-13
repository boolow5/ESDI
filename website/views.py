from django.shortcuts import render
from website.models import *

# Create your views here.
def index(request):
    p = Page()
    p.name = "Home"
    return render(request, "website/pages/index.html", {"title": "Home", "page":p, "Countries": getRegions()})

def pages(request, page):
    p = Page()
    p.name = page.capitalize()
    sidebar_items = getSidebarItems(page)

    try:
        p = Page.objects.get(name=page.capitalize())
    except Exception as e:
        error = {"message": "Page Not Found", "description": "The page you request is not in the database. Please contact the system admin to report this error"}
        p.name = page.capitalize()
        return render(request, "website/pages/error.html", {"error": error, "page":p, "SidebarItems": sidebar_items, "Countries": getRegions()})
    return render(request, "website/pages/others.html", {"page":p, "SidebarItems": sidebar_items, "Countries": getRegions()})

def profiles(request, shortname):
    p = Person()
    try:
        p = Person.objects.get(shortname=shortname)
    except Exception as e:
        error = {"message": "Profile Not Found", "description": "Please make sure the link in the address bar is correct and then try again."}
        return render(request, "website/pages/profile.html", {"error": error, "person":p})
    return render(request, "website/pages/profile.html", {"person":p})


# non-view functions
def getConsultants():
    cs = Person.objects.all()
    if cs is None:
        return None
    return cs

def getClients():
    cs = Organization.objects.all()
    if cs is None:
        return None
    return cs

def getRegions():
    rs = Region.objects.all()
    if rs is None:
        return None
    return rs

def getSidebarItems(page):
    if page is None:
        return None
    if page.lower() == "consultants":
        return getConsultants()
    elif page.lower() == "clients":
        return getClients()
    return None
