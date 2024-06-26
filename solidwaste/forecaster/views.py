import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.handlers import exception
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from forecaster.models import *
from .newcnn1 import predict

def login(request):
    return render(request,"login_index.html")


def logout(request):
    auth.logout(request)
    return render(request,"login_index.html")



def logincode(request):
    try:
        un=request.POST['textfield']
        ps=request.POST['textfield2']
        ob=Login.objects.get(username=un,password=ps)
        if ob is None:
            ob1=auth.authenticate(username='admin',password='admin')
            if ob1 is not None:
                auth.login(request,ob1)
            return HttpResponse('''<script>alert("invalid username or password");window.location='/'</script>''')
        elif ob.type=="company":
            ob1 = auth.authenticate(username='admin', password='admin')
            if ob1 is not None:
                auth.login(request, ob1)
            return redirect('/companyhome')
        elif ob.type=="agent":
            ob1 = auth.authenticate(username='admin', password='admin')
            if ob1 is not None:
                auth.login(request, ob1)
            request.session['lid']=ob.id
            return redirect('/agenthome')
        else:
            return HttpResponse('''<script>alert("invalid username or password");window.location='/'</script>''')

    except Exception as e:

         print(e)

         return  HttpResponse('''<script>alert("invalid username or password");window.location='/'</script>''')


@login_required(login_url='/')
def companyhome(request):
    return render(request,"company_index.html")

@login_required(login_url='/')
def manageagent(request):
    ob=Agent.objects.all()
    return render(request,"manage agent.html",{'val':ob})

@login_required(login_url='/')
def search_manageagent(request):
    n=request.POST['textfield']
    ob=Agent.objects.filter(name=n)
    return render(request,"manage agent.html",{'val':ob,"n":n})

@login_required(login_url='/')
def deleteagent(request,id):
    ob=Agent.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location='/manageagent#about'</script>''')

@login_required(login_url='/')
def addagent(request):
    return render(request,"addagent.html")

@login_required(login_url='/')
def addelement(request):
    nm=request.POST['textfield']
    pt= request.FILES['file']
    fs=FileSystemStorage()
    fsave=fs.save(pt.name,pt)
    plc = request.POST['textfield2']
    pst= request.POST['textfield3']
    pin= request.POST['textfield4']
    ph = request.POST['textfield5']
    email = request.POST['textfield6']
    un= request.POST['textfield7']
    ps = request.POST['textfield8']

    ob1=Login()
    ob1.username=un
    ob1.password =ps
    ob1.type ="Agent"
    ob1.save()

    ob=Agent()
    ob.name =nm
    ob.photo =fsave
    ob.place =plc
    ob.post =pst
    ob.pin =pin
    ob.phone =ph
    ob.email =email


    ob.LOGIN=ob1
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location='/manageagent'</script>''')


@login_required(login_url='/')
def viewpickuprequest(request):
    ob=Picup_Request.objects.all()
    return render(request,"view pickup request.html",{'val':ob})

@login_required(login_url='/')
def search_viewpickuprequest(request):
    d=request.POST['textfield']
    ob=Picup_Request.objects.filter(date=d)
    return render(request,"view pickup request.html",{'val':ob,"d":d})

@login_required(login_url='/')
def feedback(request):
    ob=Feedback.objects.all()
    return render(request,"feedback.html",{'val':ob})

@login_required(login_url='/')
def search_feedback(request):
    d = request.POST['textfield']
    ob=Feedback.objects.filter(date=d)
    return render(request,"feedback.html",{'val':ob,"d":d})

@login_required(login_url='/')
def assignwork(request,id):
    on=Agent.objects.all()
    request.session['rid']=id
    return render(request,"assignwork.html",{'val':on})


@login_required(login_url='/')
def assignworkcode(request):
    agent=request.POST['select']
    work=request.POST['work']
    ob=Work_assign()
    ob.AGENT=Agent.objects.get(id=agent)
    ob.REQUEST=Picup_Request.objects.get(id=request.session['rid'])
    ob.wtype=work
    ob.status='pending'
    ob.date=datetime.datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("assigned");window.location='/viewpickuprequest'</script>''')





@login_required(login_url='/')
def viewpickupstatus(request):
    ob=Work_assign.objects.all()
    return render(request,"feedback.html",{'val':ob})

@login_required(login_url='/')
def search_viewpickupstatus(request):
    d = request.POST['textfield']
    ob=Work_assign.objects.filter(date=d)
    return render(request,"viewpickupstatus.html",{'val':ob,"d":d})

@login_required(login_url='/')
def viewcomplaintsendreply(request):
    ob=Complaint.objects.all()
    return render(request,"view complaint & send reply.html",{'val':ob})

@login_required(login_url='/')
def search_viewcomplaintsendreply(request):
    d = request.POST['textfield']
    ob=Complaint.objects.filter(date=d)
    return render(request,"view complaint & send reply.html",{'val':ob, "d":d})

@login_required(login_url='/')
def sendreply(request,id):
    request.session['comid']=id
    return render(request,"sendreply.html")

@login_required(login_url='/')
def sendd(request):
    reply = request.POST['textfield']
    ob = Complaint.objects.get(id=request.session['comid'])
    ob. reply= reply
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location='/updateworkstatus'</script>''')



@login_required(login_url='/')
def managerecycleproduct(request):
    ob=Product.objects.all()
    return render(request,"Manage recycle product.html",{'val':ob})

@login_required(login_url='/')
def search_managerecycleproduct(request):
    n=request.POST['textfield']
    ob=Product.objects.filter(name=n)
    return render(request,"Manage recycle product.html",{'val':ob,"n":n})

@login_required(login_url='/')
def addproduct(request):
    return render(request,"addproduct.html")

@login_required(login_url='/')
def verifyorder(request):
    ob=Order.objects.all()
    return render(request,"Verify order.html",{'val':ob})

@login_required(login_url='/')
def search_verifyorder(request):
    d=request.POST['textfield']
    ob=Order.objects.filter(date=d)
    return render(request,"Verify order.html",{'val':ob, "d":d})

@login_required(login_url='/')
def accept(request,id):
    ob = Order.objects.get(id=id)
    ob.status='accept'
    ob.save()
    return HttpResponse('''<script>alert("Accepted");window.location='/viewitems'</script>''')

@login_required(login_url='/')
def reject(request,id):
    ob = Order.objects.get(id=id)
    ob.status = 'reject'
    ob.save()
    return HttpResponse('''<script>alert("Rejected");window.location='/viewitems'</script>''')


@login_required(login_url='/')
def viewitems(request):
    ob = Orderdetails.objects.all()
    return render(request,"viewitems.html",{'val':ob})

@login_required(login_url='/')
def agentlogin(request):
    return render(request,"agentlogin.html")

@login_required(login_url='/')
def agenthome(request):
    return render(request,"agent_index.html")

@login_required(login_url='/')
def viewassignedworkrequest(request):
    ob= Work_assign.objects.filter(AGENT__LOGIN__id=request.session['lid'])
    return render(request,"viewassignedworkrequest.html",{'val':ob})

@login_required(login_url='/')
def search_viewassignedworkrequest(request):
    d=request.POST['textfield']
    ob= Work_assign.objects.filter(date=d)
    return render(request,"viewassignedworkrequest.html",{'val':ob,"d":d})

@login_required(login_url='/')
def updateworkstatus(request):
    ob=Work_assign.objects.all()
    return render(request,"Update work status.html",{'val':ob})

@login_required(login_url='/')
def search_updateworkstatus(request):
    d=request.POST['textfield']
    ob=Work_assign.objects.filter(date=d)
    return render(request,"Update work status.html",{'val':ob,"d":d})

@login_required(login_url='/')
def update(request,id):
    ob=Work_assign.objects.get(id=id)
    request.session['wr']=ob.id
    return render(request,"update.html",{'val':ob})

@login_required(login_url='/')
def updates(request):
    nm=request.POST['textfield']
    ob=Work_assign.objects.get(id= request.session['wr'])
    ob.status=nm
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location='/updateworkstatus'</script>''')



@login_required(login_url='/')
def trackrequest(request):
    ob = Picup_Request.objects.all()
    return render(request,"trackrequest.html",{'val':ob})

@login_required(login_url='/')
def search_trackrequest(request):
    d=request.POST['textfield']
    ob = Picup_Request.objects.filter(date=d)
    return render(request,"trackrequest.html",{'val':ob ,"d":d})

@login_required(login_url='/')
def editagent(request,id):
    ob=Agent.objects.get(id=id)
    request.session['aid']=ob.id
    return render(request,"editagent.html",{'val':ob})

@login_required(login_url='/')
def edited(request):
    if 'photo' in request.FILES:
        nm = request.POST['textfield']
        pt = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(pt.name, pt)
        plc = request.POST['textfield2']
        pst = request.POST['textfield3']
        pin = request.POST['textfield4']
        ph = request.POST['textfield5']
        email = request.POST['textfield6']

        ob = Agent.objects.get(id=request.session['aid'])
        ob.name = nm
        ob.photo = fsave
        ob.place = plc
        ob.post = pst
        ob.pin = pin
        ob.phone = ph
        ob.email = email
        ob.save()
        return HttpResponse('''<script>alert("Edited");window.location='/manageagent'</script>''')
    else:
        nm = request.POST['textfield']
        plc = request.POST['textfield2']
        pst = request.POST['textfield3']
        pin = request.POST['textfield4']
        ph = request.POST['textfield5']
        email = request.POST['textfield6']

        ob = Agent.objects.get(id=request.session['aid'])
        ob.name = nm

        ob.place = plc
        ob.post = pst
        ob.pin = pin
        ob.phone = ph
        ob.email = email
        ob.save()
        return HttpResponse('''<script>alert("Added");window.location='/manageagent'</script>''')




@login_required(login_url='/')
def editproduct(request,id):
    ob=Product.objects.get(id=id)
    request.session['pid'] = ob.id
    return render(request,"editproduct.html",{'val':ob})

@login_required(login_url='/')
def deletep(request,id):
    ob=Product.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location='/managerecycleproduct'</script>''')

@login_required(login_url='/')
def editedp(request):
    if 'image' in request.FILES:
        nm = request.POST['textfield']
        photo = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(photo.name, photo)
        qty = request.POST['textfield2']
        price = request.POST['textfield3']
        Description = request.POST['textfield6']

        ob = Product.objects.get(id=request.session['pid'])
        ob.name = nm
        ob.image = fsave
        ob.quantity = qty
        ob.description=Description
        ob.price = price
        ob.save()

        return HttpResponse('''<script>alert("Added");window.location='/addproduct'</script>''')
    else:
        nm = request.POST['textfield']
        qty = request.POST['textfield2']
        price = request.POST['textfield3']
        Description = request.POST['textfield6']


        ob = Product.objects.get(id=request.session['pid'])
        ob.name = nm
        ob.quantity = qty
        ob.description=Description
        ob.price = price
        ob.save()

        return HttpResponse('''<script>alert("Added");window.location='/addproduct'</script>''')

@login_required(login_url='/')
def additem(request):
    nm=request.POST['textfield']
    photo=request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(photo.name, photo)
    Description=request.POST['textfield6']

    qty=request.POST['textfield2']
    price=request.POST['textfield3']

    ob=Product()
    ob.name=nm
    ob.image=fsave
    ob.quantity=qty
    ob.price=price
    ob.description=Description
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location='/addproduct'</script>''')

@login_required(login_url='/')
def publicwaste(request):
    ob = Waste.objects.all()
    return render(request, "publicwaste.html", {'val': ob})


###########################################################################################################33

##Android
import json
def logincode1(request):
    # print(request.form)
    username = request.POST['username']
    password = request.POST['password']
    try:
        ob = Login.objects.get(username=username, password=password)
        if ob is None:
            return JsonResponse({'task': 'invalid'})
        else:
            print({'task': 'valid', "id": ob.id})
            return JsonResponse({'task': 'valid', "id": ob.id})
    except Exception as e:
        print(e)
        return JsonResponse({'task': 'invalid'})



def register(request):
    nm=request.POST['name']
    pt= request.FILES['file']
    fs=FileSystemStorage()
    fsave=fs.save(pt.name,pt)
    age=request.POST['age']
    # plc = request.POST['place']
    # pst= request.POST['post']
    # pin= request.POST['pin']
    ph = request.POST['phonenumber']
    email = request.POST['email']
    un= request.POST['username']
    ps = request.POST['password']

    ob1=Login()
    ob1.username=un
    ob1.password =ps
    ob1.type ="User"
    ob1.save()

    ob=User()
    ob.name =nm

    ob.age=age
    # ob.place =plc
    # ob.post =pst
    # ob.pin =pin
    ob.phoneno =ph
    ob.email =email
    ob.image =fsave


    ob.LOGIN=ob1
    ob.save()
    return JsonResponse({'task': 'success'})

def viewcmprply(request):
    lid=request.POST['lid']
    ob=Complaint.objects.filter(USER__LOGIN__id=lid)
    data=[]
    for i in ob:
        row={"complaint":i.Complaint,"date":i.date,"reply":i.reply}
        data.append(row)
    return JsonResponse(data,safe=False)



def sendpickuprequest(request):
    pickuprequest = request.POST["Picup_Request"]
    latitude = request.POST["Picup_Request"]
    longitude = request.POST["Picup_Request"]
    status = request.POST["Picup_Request"]
    u_id = request.POST["uid"]
    date = datetime.now()

    picuprequest_obj =Picup_Request()
    picuprequest_obj. request =pickuprequest
    picuprequest_obj.date = date
    picuprequest_obj.latitude  =latitude
    picuprequest_obj.longitude = longitude
    picuprequest_obj.status = status
    picuprequest_obj.USER = User.objects.get(LID__id=u_id)
    picuprequest_obj.save()
    return JsonResponse({'task': 'pickuprequest succesfully sent'})


def sendcomplaint(request):
    complaints = request.POST["Complaint"]
    u_id = request.POST["lid"]
    date = datetime.datetime.now()
    reply = "waiting"
    complaint_obj = Complaint()
    complaint_obj.Complaint = complaints
    complaint_obj.date = date
    complaint_obj.reply = reply
    complaint_obj.USER = User.objects.get(LOGIN=u_id)
    complaint_obj.save()
    return JsonResponse({'task': 'valid'})

def sendfeedback(request):
    feedback = request.POST["Feedback"]
    feedback_id = request.POST["lid"]
    feedback_obj =Feedback()
    feedback_obj.feedback= feedback
    feedback_obj.date = datetime.datetime.now()
    feedback_obj.USER= User.objects.get(LOGIN__id=feedback_id)
    feedback_obj.save()
    return JsonResponse({'task': 'valid'})


def and_viewproduct(request):
    ob=Product.objects.all()
    data=[]
    for i in ob:
        row={"name":i.name,"image":i.image.url,"description":i.description,"quantity":i. quantity,"price":i.price,"pid":i.id,"description":i.description}
        data.append(row)

    return JsonResponse(data,safe=False)

def searchproduct(request):
    name=request.POST['name']
    ob=Product.objects.filter(name__contains=name)
    data=[]
    for i in ob:
        row={"name":i.name,"image":i.image.url,"description":i.description,"price":i.price,"pid":i.id}
        data.append(row)
    return JsonResponse(data,safe=False)





def vieworderstatus(request):
    lid=request.POST['lid']
    ob=Order.objects.filter(USER__LOGIN__id=lid)
    data=[]
    for i in ob:
        row={"date":str(i.date),"status":i.status, "amount":i. amount,"Orderid":i.id}
        data.append(row)
    print("((((((((((((((((((", data)
    return JsonResponse(data,safe=False)

def viewpayment(request):
    lid=request.POST['lid']
    ob=Payment.objects.filter(ORDER__USER__LOGIN__id=lid)
    data=[]
    for i in ob:
        row={"date":i.date,"user":i.user,"amount":i.amount}
        data.append(row)
    return JsonResponse(data)

def reportpublic(request):
    photo = request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(photo.name, photo)
    waste_id = request.POST["lid"]
    # latitude = request.POST["latitude"]
    # longitude = request.POST["longitude"]
    res=predict(r"C:\Users\lenovo\PycharmProjects\solidwaste\media/"+str(fsave))
    print(res,"=========================")
    print(res,"=========================")
    print(res,"=========================")
    waste_obj =Waste()
    # waste_obj.feedback= feedback
    waste_obj.date = datetime.datetime.today()
    waste_obj.image = fsave
    # waste_obj.latitude = latitude
    # waste_obj.longitude = longitude
    waste_obj.USER= User.objects.get(LOGIN__id=waste_id)
    waste_obj.save()
    return JsonResponse({'task': 'success'})


def orderproduct(request):
    ob = Order.objects.get(id=id)
    ob.status = 'accept'
    ob.save()
#####################
def ordrprdctcard(request):
    print(request.POST,"hhhhhhhhhhhh")
    qty=request.POST['qty']
    pid=request.POST['pid']
    lid=request.POST['lid']
    date=datetime.datetime.now()
    print(date, "jjjjjjjjjjjjjjjjjjjjjj")
    qq=Product.objects.get(id=pid)
    tt = int(qq.price)* int(qty)
    quantity= int(qq.quantity)
    print(quantity,qty,"jjjjjjjjjjjjjjjjjjjjjj")
    nstk = int(quantity) - int(qty)
    if quantity>= int(qty):
        up=Product.objects.get(id=pid)
        up.quantity=nstk
        up.save()
        q=Order.objects.filter(USER=User.objects.get(LOGIN__id=lid),status='pending')
        if len(q)==0:
            qt=Order()
            qt.date=date
            qt.USER=User.objects.get(LOGIN=lid)
            qt.status='CART'
            qt.amount=tt
            qt.save()
            qty1=Orderdetails()
            qty1.quantity=qty
            qty1.amount=tt
            qty1.PRODUCT=Product.objects.get(id=pid)
            qty1.ORDER=qt
            qty1.date = date
            qty1.save()
            data = {"task": "valid"}
            r = json.dumps(data)
            print(r)
            return HttpResponse(r)
        else:
            total = int(q[0].amount) + int(tt)
            qt=Order.objects.get(id=q[0].id)
            qt.amount=total
            qt.save()
            qty1=Orderdetails.objects.filter(PRODUCT__id=pid,ORDER__id=q[0].id)
            if len(qty1)==0:
                qqt=Orderdetails()
                qqt.ORDER=q[0]
                qqt.PRODUCT=Product.objects.get(id=pid)
                qqt.quantity=qty
                qty1.amount = tt
                qqt.date = date
                qqt.save()
            else:
                qry1=Orderdetails.objects.get(id=qty1[0].id)
                quty=int(qty1[0].quantity) + int(qty)
                qry1.quantity=quty
                qry1.save()
                data = {"task": "valid"}
                r = json.dumps(data)
                print(r)
                return HttpResponse(r)
    else:
        data = {"task": "out"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    data = {"task": "invalid"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)

def addtocart(request):
    print(request.POST, "hhhhhhhhhhhh")
    qty = request.POST['qty']
    pid = request.POST['pid']
    lid = request.POST['lid']
    qq = Product.objects.get(id=pid)
    tt = int(qq.price) * int(qty)
    quantity = int(qq.quantity)
    print(quantity, qty, "jjjjjjjjjjjjjjjjjjjjjj")
    nstk = int(quantity) - int(qty)
    if quantity >= int(qty):
        up = Product.objects.get(id=pid)
        up.quantity= nstk
        up.save()
        q = Order.objects.filter(USER=User.objects.get(LOGIN__id=lid), status='CART')
        if len(q) == 0:
            qt = Order()
            qt.date = datetime.datetime.today()
            qt.USER = User.objects.get(LOGIN=lid)
            qt.status = 'CART'
            qt.amount = tt
            qt.save()
            qty1 = Orderdetails()
            qty1.amount = tt
            qty1.quantity = qty
            qty1.PRODUCT = Product.objects.get(id=pid)
            qty1.ORDER = qt
            qty1.date = datetime.datetime.today()

            qty1.save()
            data = {"task": "valid"}
            r = json.dumps(data)
            print(r)
            return HttpResponse(r)
        else:
            total = int(q[0].amount) + int(tt)
            qt = Order.objects.get(id=q[0].id)
            qt.amount = total
            qt.date = datetime.datetime.today()
            qt.save()
            qty1 = Orderdetails.objects.filter(PRODUCT__id=pid,ORDER__id=q[0].id)
            if len(qty1) == 0:
                print("if product is not exists")
                qqt = Orderdetails()
                qqt.ORDER = q[0]
                qqt.PRODUCT = Product.objects.get(id=pid)
                qqt.quantity = qty
                qqt.date = datetime.datetime.today()
                qqt.amount = tt
                qqt.save()
                data = {"task": "valid"}
                r = json.dumps(data)
                print(r)
                return HttpResponse(r)
            else:
                print("if product is exists")
                qry1 = Orderdetails.objects.get(id=qty1[0].id)
                quty = int(qty1[0].quantity) + int(qty)
                qry1.quantity = quty
                qry1.save()
                data = {"task": "valid"}
                r = json.dumps(data)
                print(r)
                return HttpResponse(r)
    else:
        data = {"task": "out"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    data = {"task": "invalid"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)

def cartorder(request):
    lid=request.POST['lid']
    total=request.POST['lid']





def ordrprdctcodeand(request):
    print(request.POST,"hhhhhhhhhhhh")
    qty=request.POST['qty']
    pid=request.POST['pid']
    lid=request.POST['lid']
    date = datetime.date.today()
    qq=Product.objects.get(id=pid)
    tt = int(qq.price)* int(qty)
    quantity = int(qq.quantity)
    print(quantity,qty,"jjjjjjjjjjjjjjjjjjjjjj")

    print(date,"jjjjjjjjj")
    if quantity >= int(qty):
        up=Product.objects.get(id=pid)
        nstk = int(quantity) - int(qty)
        up.quantity=nstk
        up.save()
        q=Order.objects.filter(USER=User.objects.get(LOGIN__id=lid),status='pending')
        if len(q)==0:
            qt=Order()
            qt.date=date
            qt.USER=User.objects.get(LOGIN=lid)
            qt.status='pending'
            qt.amount=tt
            qt.save()
            qty1=Orderdetails()
            qty1.quantity=qty
            qty1.PRODUCT=Product.objects.get(id=pid)
            qty1.ORDER=qt
            qty1.amount=tt
            qty1.date = date
            qty1.save()
            data = {"task": "valid"}
            r = json.dumps(data)
            print(r)
            return HttpResponse(r)
        else:
            total = int(q[0].amount) + int(tt)
            qt=Order.objects.get(id=q[0].id)
            qt.amount=total
            qt.save()
            qty1=Orderdetails.objects.filter(PRODUCT__id=pid,ORDER__id=q[0].id)
            if len(qty1)==0:
                qqt=Orderdetails()
                qqt.ORDER=q[0]
                qqt.PRODUCT=Product.objects.get(id=pid)
                qqt.quantity=qty
                qqt.amount=tt
                qqt.date=date
                qqt.save()
                data = {"task": "valid"}
                r = json.dumps(data)
                print(r)
                return HttpResponse(r)
            else:
                qry1=Orderdetails.objects.get(id=qty1[0].id)
                quty=int(qty1[0].quantity) + int(qty)
                qry1.quantity=quty
                qry1.save()
                data = {"task": "valid"}
                r = json.dumps(data)
                print(r)
                return HttpResponse(r)
    else:
        data = {"task": "out"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)

def viewcart(request):
    try:
        print(request.POST)
        lid = request.POST['lid']
        order_id=[]
        obb=Order.objects.filter(status='CART',USER__LOGIN__id=lid)
        print(obb,"gfffff")
        print(obb,"gfffff")
        print(obb,"gfffff")
        print(obb,"gfffff")
        ob = Order.objects.filter(status='CART',USER__LOGIN__id=lid)
        for i in ob:
            order_id.append(i.id)
        data = []
        ob1 = Orderdetails.objects.filter(ORDER_id__in=order_id)
        total=0
        for i in ob1:
            total=total+i.amount

            row = {"name": i.PRODUCT.name, "image": i.PRODUCT.image.url, "price": i.PRODUCT.price,"odid":i.id}
            data.append(row)
        print("&&&&&&&&&&&&&&&&&&&&&&", data)
        return JsonResponse({'data':data,"data1":total})
    except:
        return JsonResponse({'data':0,"data1":0})


def addtocartorder(request):
    uidd=request.POST['lid']


    ob=Order.objects.filter(USER__LOGIN__id=uidd,status='CART')
    if len(ob)>0:
        ob=ob[0]
        ob.status='ORDERD'
        ob.save()
        data = {"task": "success"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    else:
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)





def paymentfinish(request):

    oid=request.POST['bid']
    amount=request.POST['amt']
    lid=request.POST['lid']
    ob = Payment()
    ob.ORDER=Order.objects.get(id=oid)
    ob.USER=User.objects.get(LOGIN__id=lid)
    ob.status='PAID'
    ob.amount=amount
    ob.date=datetime.now()
    ob.save()
    obj=Order.objects.get(id=oid)
    obj.status='PAID'
    obj.save()
    data = {"task": "success"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)
# def viewitems(request):
#     ob = Orderdetails.objects.all()
#     return render(request,"viewitems.html",{'val':ob})
# def ordercart(request):
#     lid = request.POST['lid']


def cancel_s_order(request):
    oid=request.POST['odid']
    ob=Orderdetails.objects.get(id=oid)
    p = Product.objects.get(id=ob.PRODUCT.id)
    p.quantity=int(p.quantity)-int(ob.quantity)
    p.save()

    obb=Orderdetails.objects.get(id=oid)
    obb.amount=int(obb.amount)-(int(ob.quantity )*int(ob.PRODUCT.price))
    obb.save()
    ob.delete()
    data = {"task": "valid"}
    r = json.dumps(data)

    print(r)
    return HttpResponse(r)

def wasterequest(request):
    ob=Waste.objects.all()
    date=[]
    for i in ob:
        if str(i.date) not in date:
            date.append(str(i.date))
    x=[]
    y=[]
    for i in date:
        obb=Waste.objects.filter(date=i)
        x.append(len(obb))
        y.append(len(obb))

    xx = []
    yy = []
    for ii in range(len(x)):
        print("================================")
        print("================================")
        print("================================")


        try:
            xx.append(ii + 1)
            yy.append(y[ii])
        except:
            yy.append(0)

                # data = pd.read_csv('data.csv')
    data = np.array(y)
    print(data)
    print(type(data))
    print("<class 'numpy.ndarray'>")

    # Normalize the data
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data.reshape(-1, 1))

    # Split the data into training and testing sets
    train_size = int(len(data) * 0.8)
    train_data, test_data = data[:train_size], data[train_size:]

    # Create sequences for the LSTM model
    def create_sequences(data, look_back):
        print(len(data))
        X, Y = [], []
        for i in range(len(data) - look_back):
            X.append([data[i:i + look_back]])
            Y.append(data[i + look_back])
        print(len(X),"*********************")
        print(len(Y),"+++++++++++++++++++++++")
        print(X[0])
        print(Y[0])
        return np.array(X), np.array(Y)

    look_back = 3  # You can adjust this parameter to change the sequence length
    train_X, train_y = create_sequences(x, look_back)
    test_X, test_y = create_sequences(x, look_back)

    # Build the LSTM model
    model = Sequential()
    model.add(LSTM(units=50, input_shape=(1,look_back)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    print(len(train_X),len(train_y),"+++++__________")
    print(len(train_X),len(train_y),"+++++__________")
    print(len(train_X),len(train_y),"+++++__________")
    print(train_X)
    print(train_y)

    model.fit(train_X, train_y, epochs=100, batch_size=64)

    # Make predictions
    train_predict = model.predict(train_X)
    test_predict = model.predict(test_X)
    print(test_predict)

    # Inverse transform the predictions to original scale
    train_predict = scaler.inverse_transform(train_predict)
    test_predict = scaler.inverse_transform(test_predict)
    print(test_predict)
    return render(request,"viewresult.html",{"res":train_predict[-1]})


def result(request):
    return render(request,"viewresult.html")
