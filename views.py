from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import Income,IncomeForm
def add_income(request):
    if request.method=="POST":
        f=IncomeForm(request.POST)
        f.save()
        return redirect('/')
    else:
        context={'form':IncomeForm}
        return render(request,"addincome.html",context)
 
def income_list(request):
    
    
    
    uid=request.session.get('uid')
        
        
    incl=Income.objects.filter(user=uid)
    #incl=Income.objects.get()
    inc_income=set()
    inc_type=set()
    inc_date=set()
    for i in incl:
        inc_income.add(i.income)
        inc_date.add(i.incomeDate)
        inc_type.add(i.incomeType)
    context={'incl':incl,'inc_income':inc_income,'inc_date':inc_date,'inc_type':inc_type}
    return render(request,"incomelist.html",context)

def delete_income(request,id):
    inc=Income.objects.get(id=id)
    inc.delete()
    return redirect('/')
def edit_income(request,id):
    inc=Income.objects.get(id=id)
    if request.method=="POST":
        f=IncomeForm(request.POST,instance=inc)
        f.save()
        return redirect('/')
    
    else:
        inc=IncomeForm(instance=inc)
        context={'form':inc}
        return render(request,"editincome.html",context)
        
def by_income(request,incometype):
    
    uid=request.session.get('uid')
    print(uid)
        
    incl=Income.objects.filter(user=uid,income=incometype)
    inc_income=set()
    inc_type=set()
    inc_date=set()
    for i in incl:
        inc_income.add(i.income)
        inc_date.add(i.incomeDate)
        inc_type.add(i.incomeType)
    context={'incl':incl,'inc_income':inc_income,'inc_date':inc_date,'inc_type':inc_type}
    return render(request,"incomelist.html",context)

def by_date(request,datetype):
    
    uid=request.session.get('uid')
    print(uid)
        
    incl=Income.objects.filter(user=uid,incomeDate=datetype)
    inc_income=set()
    inc_type=set()
    inc_date=set()
    for i in incl:
        inc_income.add(i.income)
        inc_date.add(i.incomeDate)
        inc_type.add(i.incomeType)
    context={'incl':incl,'inc_income':inc_income,'inc_date':inc_date,'inc_type':inc_type}
    return render(request,"incomelist.html",context)

def by_type(request,type):
    
    uid=request.session.get('uid')
    print(uid)
        
    incl=Income.objects.filter(user=uid,incomeType=type)
    inc_income=set()
    inc_type=set()
    inc_date=set()
    for i in incl:
        inc_income.add(i.income)
        inc_date.add(i.incomeDate)
        inc_type.add(i.incomeType)
    context={'incl':incl,'inc_income':inc_income,'inc_date':inc_date,'inc_type':inc_type}
    return render(request,"incomelist.html",context)
   