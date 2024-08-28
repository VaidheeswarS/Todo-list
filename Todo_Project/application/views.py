from django.shortcuts import render,get_object_or_404,redirect
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet 
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
# Create your views here.


class home(APIView):
    def get(self,request):
        return render(request,"home.html")
    

class Datas(ModelViewSet):
    queryset=User_Registration.objects.all()
    serializer_class=postdata
    # user1=User.objects.create(username=queryset.Email)


class log_in(APIView):
    # permission_classes=
    def get(self,request):
        return render(request,"login.html")
    
    def post(self,request):
        email=request.POST.get("email")
        password=request.POST.get("password")
        row=get_object_or_404(User_Registration,Email=email)
        chk=Login_data.objects.all()
        for i in chk:
            print(row.Email)
            if i.email_id != email:
                continue
            else:
                break
        else:
            user1=User.objects.create_user(username=row.Email,password=row.Password)
            user1.save()
            Login_data.objects.create(email_id=row.Email,password=row.Password)
        user2=authenticate(request,username=row.Email, password=row.Password)   

        if user2 is not None:
            user2=authenticate(request,username=row.Email, password=row.Password)
            print(user2)
            login(request,user2)
            ltable=get_object_or_404(Login_data,email_id=email)
            return render (request,"myprofile.html",{"ltable":ltable, "row":row})
        else:
            return Response("error")

        # permission_classes=    

# @login_required
class log_out(APIView):

    def get(self,request):
        logout(request)
        return redirect("/")

# class addwork(ModelViewSet):
#     queryset=Works.objects.all()
#     serializer_class=wtable
# @login_required
class addworks(APIView):
    def get(self,request,wrk):
        rdata=get_object_or_404(Login_data,email_id=wrk)
        return render(request,"addwork.html",{"rdata":rdata})
    
    def post(self,request,wrk):
        remainder=request.POST.get("remainder")
        time=request.POST.get("date")
        wrksts=request.POST.get("status")
        sno=request.POST.get("sno")
        new=get_object_or_404(Login_data,email_id=wrk)
        print(new.S_No)
        print(new.email_id)
        sv=Login_data.objects.all()
        for i in sv:
            if i.email_id==wrk:
                print(i.email_id)
                Works.objects.create(To=i,work=remainder,email=new.email_id,Submit_time=time,status=wrksts)
                fldata=Works.objects.filter(email=new.email_id)
                mtable=get_object_or_404(User_Registration,Email=wrk)
                return render(request,"myprofile.html",{"fldata":fldata, "row":mtable ,"ltable":new})
            else:
                continue
        else:
            return Response("not proceed")
        
# @login_required
class decision(APIView):
    
    def get(self,request,email,No):
        dec=get_object_or_404(Works,No=No)
        # dec2=get_object_or_404(Works,email=email)
        return render(request,"decision.html",{"dec":dec,})
    
    def post(self,request,email,No):
        dec=get_object_or_404(Works,No=No)
        fldata=Works.objects.filter(email=email)
        dec.status=request.POST.get("Decision")
        dec.save()
        mtable=get_object_or_404(User_Registration,Email=email)
        new=get_object_or_404(Login_data,email_id=email)
        return render(request,"myprofile.html",{"fldata":fldata,"row":mtable,"ltable":new})

# @login_required
class update(APIView):

    def get(self,request,No):
        urow=get_object_or_404(Works,No=No)
        return render(request,"update.html",{"urow":urow})
    def post(self,request,No):
        urow=get_object_or_404(Works,No=No)
        remainder=request.POST.get("remainder")
        time=request.POST.get("date")
        wrksts=request.POST.get("status")
        # sno=request.POST.get("sno")
        urow.work=remainder
        urow.Submit_time=time
        urow.status=wrksts
        urow.save()
        mtable=get_object_or_404(User_Registration,Email=urow.email)
        ltable=get_object_or_404(Login_data,email_id=urow.email)
        fldata=Works.objects.filter(email=urow.email)
        return render(request,"myprofile.html",{"fldata":fldata,"row":mtable,"ltable":ltable})

class delete(APIView):
    def get(self,request,remove):
        rem=get_object_or_404(Works,No=remove)
        mtable=get_object_or_404(User_Registration,Email=rem.email)
        ltable=get_object_or_404(Login_data,email_id=rem.email)
        fldata=Works.objects.filter(email=rem.email)
        rem.delete()
        return render(request,"myprofile.html",{"fldata":fldata,"row":mtable,"ltable":ltable})

