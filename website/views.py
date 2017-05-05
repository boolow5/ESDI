from django.shortcuts import render
from website.models import *

# Create your views here.
def index(request):
    p = Page()
    p.name = "Home"
    All = getAllItems()
    esdi = esdi_detail = PageSection()
    try:
        esdi = PageSection.objects.get(name="esdi")
    except:pass
    try:
        esdi_detail = PageSection.objects.get(name="esdi detail")
    except:
        pass
    featured1, featured2, featured3 = getFeaturedSections()
    what, how = getWhatAndHowSection()
    return render(request, "website/pages/index.html", {"title": "Home", "page":p, "Countries": getRegions(), "ESDI": esdi, "featured1": featured1, "featured2": featured2, "featured3": featured3, "esdi_detail": esdi_detail, "what": what, "how": how, "all": All})

def pages(request, page):
    p = Page()
    p.name = page.capitalize()
    sidebar_items = getSidebarItems(page)
    All = getAllItems()

    esdi = esdi_detail = PageSection()
    try:
        esdi = PageSection.objects.get(name="esdi")
    except:pass
    try:
        esdi_detail = PageSection.objects.get(name="esdi detail")
    except:
        pass

    try:
        p = Page.objects.get(name=page.capitalize())
    except Exception as e:
        error = {"message": "Page Not Found", "description": "The page you request is not in the database. Please contact the system admin to report this error"}
        p.name = page.capitalize()
        return render(request, "website/pages/error.html", {"error": error, "page":p, "SidebarItems": sidebar_items, "Countries": getRegions(), "ESDI": esdi, "esdi_detail": esdi_detail, "all": All})
    return render(request, "website/pages/others.html", {"page":p, "SidebarItems": sidebar_items, "Countries": getRegions(), "ESDI": esdi, "esdi_detail": esdi_detail, "all": All})

def profiles(request, shortname):
    All = getAllItems()
    p = Person()
    try:
        p = Person.objects.get(shortname=shortname)
    except Exception as e:
        error = {"message": "Profile Not Found", "description": "Please make sure the link in the address bar is correct and then try again."}
        return render(request, "website/pages/profile.html", {"error": error, "person":p, "all": All})
    return render(request, "website/pages/profile.html", {"person":p, "all": All})


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
    rs = Country.objects.all()
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

def getAllItems():
    items = {}
    items["clients"] = getClients()
    items["consultants"] = getConsultants()
    items["countries"] = getRegions()
    esdi = PageSection()
    try:
        esdi = PageSection.objects.get(name="esdi")
    except:pass
    items["ESDI"] = esdi
    try:
        items["address"] = PageSection.objects.get(name="address")
    except: pass
    try:
        items["phones"] = PageSection.objects.get(name="phones")
    except:pass 
    return items

def getFeaturedSections():
    featured1 = featured2 = featured3 = PageSection()
    try:
        featured1 = PageSection.objects.get(name='featured1')
    except Exception as e:
        print(e)
    try:
        featured2 = PageSection.objects.get(name='featured2')
    except Exception as e:
        print(e)
    try:
        featured3 = PageSection.objects.get(name='featured3')
    except Exception as e:
        print(e)

    return (featured1, featured2, featured3)
def getWhatAndHowSection():
    what = how = PageSection()
    try:
        what = PageSection.objects.get(name="what we do")
    except: pass
    try:
        how = PageSection.objects.get(name="how we do")
    except: pass

    return (what, how)
