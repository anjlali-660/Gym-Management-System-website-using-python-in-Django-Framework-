from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
# Create your views here.
def index(request):
    res=render(request,'application/index.html')
    return res


def Contact(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=="POST":
        n=request.POST['name']
        l=request.POST['last_name']
        c=request.POST['contact']
        e=request.POST['email']
        a=request.POST['age']
        d=request.POST['describe']

        try:
            Contact.objects.create(First_Name=n,Last_Name=l,Contact=c,Email_Id=e,Age=a,Describe=d)
            error ="no"

        except:
            error="yes"


    d={'error':error}
    return render(request,'application/Contact.html',d)


def About(request):
    res=render(request,'application/About.html')
    return res



def Services(request):
    res=render(request,'application/Services.html')
    return res


def Contact(request):
    res=render(request,'application/Contact.html')
    return res

def admin_homepage(request):
    if not request.user.is_staff:
        return redirect('login')

    enquiry=Enquiry.objects.all()
    eqp=Equipments.objects.all()
    plan=Plan.objects.all()
    mem=Member.objects.all()
    a1=0
    b1=0
    c1=0
    d1=0

    for i in enquiry:
        a1+=1

    for i in eqp:
        b1+=1

    for i in plan:
        c1+=1
    for i in mem:
        d1+=1
    d={'a1':a1,'b1':b1,'c1':c1,'d1':d1}
    res=render(request,'application/admin_homepage.html',d)
    return res


def admin_login(request):
    data={}
    if request.method=="POST":
        u=request.POST['admin']
        p=request.POST['pwd']

        user=authenticate(request,username=u,password=p)
        if user:
            login(request,user)
            return HttpResponseRedirect("http://localhost:5000/applications/admin_homepage/")

        else:
            data['error']="Login Failed..Either Username or password is incorrect"
            return render(request,'application/login.html',data)

    else:
        return render(request,'application/login.html',data)



def admin_logout(request):
    logout(request)
    return HttpResponseRedirect("http://localhost:5000/applications/login/")



def add_enquiry(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')

    if request.method=="POST":
        n=request.POST['name']
        c=request.POST['contact']
        e=request.POST['email']
        a=request.POST['age']


        try:
            Enquiry.objects.create(Name=n,Contact=c,Email_Id=e,Age=a)
            error ="no"

        except:
            error="yes"


    d={'error':error}
    return render(request,'application/add_enquiry.html',d)
def view_enquiry(request):
    if not request.user.is_staff:
        return redirect('admin_login')

    enq=Enquiry.objects.all()
    d={'enq':enq}
    return render(request,'application/view_enquiry.html',d)

def delete_enquiry(request):
    pid=request.GET['pid']
    enq=Enquiry.objects.get(id=pid)
    enq.delete()
    return redirect('/applications/view_enquiry')

def add_equipments(request):
    error=""
    if not request.user.is_staff:
        return('login')

    if request.method=="POST":
        n=request.POST['Name']
        p=request.POST['Price']
        u=request.POST['Unit']
        d=request.POST['Date']
        de=request.POST['Description']

        try:
            Equipments.objects.create(Name=n,Price=p,Unit=u,Date=d,Description=de)
            error="no"

        except:
            error="yes"
    data={'error':error}
    return render(request,'application/add_equipments.html',data)




def view_equipments(request):
    if not request.user.is_staff:
        return('admin_login')

    equip=Equipments.objects.all()
    data={'equip':equip}
    return render(request,'application/view_equipments.html',data)



def delete_equipments(request):
    pid=request.GET['pid']
    enq=Equipments.objects.get(id=pid)
    enq.delete()
    return redirect('/applications/view_equipments')




def add_plan(request):
    error=""
    if not request.user.is_staff:
        return('login')

    if request.method=="POST":
        n=request.POST['Name']
        a=request.POST['Amount']
        d=request.POST['Duration']

        try:
            Plan.objects.create(Name=n,Amount=a,Duration=d)
            error="no"

        except:
            error="yes"

    data={'error':error}
    return render(request,'application/add_plan.html',data)



def view_plan(request):
    if not request.user.is_staff:
        return('login')
    pla=Plan.objects.all()
    data={'pla':pla}
    return render(request,'application/view_plan.html',data)


def delete_plan(request):
    pid=request.GET['pid']
    enq=Plan.objects.get(id=pid)
    enq.delete()
    return redirect('/applications/view_plan')





def add_member(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')

    plan1=Plan.objects.all()

    if request.method=="POST":
        n=request.POST['Name']
        c=request.POST['Contact']
        e=request.POST['Email_Id']
        a=request.POST['Age']
        g=request.POST['gender']
        p=request.POST['Plan']
        jd=request.POST['Join_Date']
        ed=request.POST['Expiry_Date']
        ia=request.POST['Initial_Amount']
        plan=Plan.objects.filter(Name=p).first()

        try:
            Member.objects.create(Name=n,Contact=c,Email_Id=e,Age=a,Gender=g,Plan=plan,Join_Date=jd,Expiry_Date=ed,Initial_Amount=ia)
            error ="no"

        except:
            error="yes"


    d={'error':error,'plan':plan1}
    return render(request,'application/add_member.html',d)



def view_member(request):
    if not request.user.is_staff:
        return redirect('login')

    mem=Member.objects.all()
    d={'mem':mem}
    return render(request,'application/view_member.html',d)


def delete_member(request):
    pid=request.GET['pid']
    enq=Member.objects.get(id=pid)
    enq.delete()
    return redirect('/applications/view_member')
