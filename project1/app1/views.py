from django.shortcuts import render,redirect
from . models import adminDatabase,userDatabase,queryDatabase

# Create your views here.
def home(request):
    return render(request,'index.html')

def regadmin(request):
    if request.method=="POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        email=request.POST['email']
        ct=request.POST['contact']
        pw=request.POST['password']
        cpw=request.POST['cpassword']
        user=adminDatabase.objects.filter(Email=email)
        if user:
            msg=" admin user already exist"
            return render(request,'regadmin.html',{'msg':msg})
        else:
            if pw==cpw:
                adminDatabase.objects.create(Fname=fn,Lname=ln,Email=email,Contact=ct,Password=pw)
                msg="data send to database successfully"
                return render(request,'loginadmin.html',{'msg':msg})
            else:
                msg="password dosent match"
                return render(request,'regadmin.html',{'msg':msg})
    return render(request,'regadmin.html')

def loginadmin(request):
    if request.method=="POST": 
        email=request.POST['email']
        pw=request.POST['password']
        try:
            user=adminDatabase.objects.get(Email=email)
            if user:
                if user.Password==pw:
                    return render(request,'admindashboard.html')
                else:
                    msg="password dosent match"
                    return render(request,'loginadmin.html',{'msg':msg})
        except:
            msg="user does not exist"
            return render(request,'regadmin.html',{'msg':msg})
    return render(request,'loginadmin.html')

#----------------------------------------------------------------------
def reguser(request):
    if request.method=="POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        email=request.POST['email']
        ct=request.POST['contact']
        pw=request.POST['password']
        cpw=request.POST['cpassword']
        user=userDatabase.objects.filter(Email=email)
        if user:
            msg="user already exist"
            return render(request,'reguser.html',{'msg':msg})
        else:
            if (pw==cpw):
                userDatabase.objects.create(Fname=fn,Lname=ln,Email=email,Contact=ct,Password=pw)
                msg="user data registered successfully"
                return render(request,'loginuser.html',{'msg':msg})
            else:
                msg="password does not match"
                return render(request,'reguser.html',{'msg':msg})
    return render(request,'reguser.html')

def loginuser(request):
    if request.method=="POST":
        email=request.POST['email']
        pw=request.POST['password']
        try:
            user=userDatabase.objects.get(Email=email)
            if user:
                if user.Password==pw:
                    return render(request,'userdashboard.html')
                else:
                    msg="wrong password"
                    return render(request,'loginuser.html',{'msg':msg})
        except:
            msg="user does not exist"
            return render(request,'reguser.html',{'msg':msg})
    return render(request,'loginuser.html')

def query(request):
   return render(request,'queryform.html')

def insertquery(request):
    if request.method=="POST":
        nm=request.POST['name']
        em=request.POST['email']
        ct=request.POST['contact']
        q=request.POST['query']
        queryDatabase.objects.create(Name=nm,Email=em,Contact=ct,Query=q)
        return render(request,'userdashboard.html')

def userdashboard(request):
    return render(request,'userdashboard.html')

def admindashboard(request):
    return render(request,'admindashboard.html')

def showquery(request):
    data=queryDatabase.objects.all()
    return render(request,'showquery.html',{'d':data})

def update(request,id):
    udata=queryDatabase.objects.get(id=id)
    return render(request,'update.html',{'d1':udata})

def showupdate(request,id):
    updata=queryDatabase.objects.get(id=id)
    nm=request.POST['name']
    em=request.POST['email']
    ct=request.POST['contact']
    q=request.POST['query']
    filldata=queryDatabase(id=id,Name=nm,Email=em,Contact=ct,Query=q)
    filldata.save()
    return redirect('showquery')

def delete(request,id):
    data=queryDatabase.objects.get(id=id)
    data.delete()
    return redirect('showquery')