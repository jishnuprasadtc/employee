from django.shortcuts import render,redirect
from django.views.generic import View
from crm.forms import EmployeeForms,EmployeeModelForm,RegistrationForm,LoginForm
from crm.models import Employees
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout




# Create your views here.



class EmployeeCreateView(View):

    def get(self,request,*args,**kwargs):
        form=EmployeeModelForm()
        return render(request,"emp_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=EmployeeModelForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully created!")
            # Employees.objects.create(** form.cleaned_data)
            print("created")
            return render(request,"emp_add.html",{"form":form})
        else:
            messages.error(request,"creation failed")
            return render(request,"emp_add.html",{"form":form})
        


class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employees.objects.all()
        return render(request,"Emp_list.html",{"data":qs})
    def post(self,request,*args,**kwargs):
        name=request.POST.get("box")
        qs=Employees.objects.filter(name__icontains=name)
        return render(request,"Emp_list.html",{"data":qs})
    


class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)

        return render(request,"emp_detail.html",{"data":qs})
    


class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employees.objects.get(id=id).delete()
        messages.success(request," delete successfull")
        return redirect("emp-all")



class EmployeeUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Employees.objects.get(id=id)
        form=EmployeeModelForm(instance=obj)
        return render(request,"emp_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Employees.objects.get(id=id)
        form=EmployeeModelForm(request.POST,instance=obj ,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully updated")
            print ("Edited")
            return redirect("emp-detail",pk=id)
        else:
            messages.error(request,"updation failed ")
            return render(request,"emp_edit.html",{"form":form})
        


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"reg.html",{"form":form})
    

    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"Created successfully")
            return redirect("signingit")
        else:
            messages.error(request,"Failed to create!")
            return render(request,"reg.html",{"form":form})


class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"Login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password") 
            user_object=authenticate(request,username=u_name,password=pwd)
            if user_object:
                print("valid credential")
                login(request,user_object)
                return redirect("emp-all")
            
        messages.error(request,"invaild credential")
        return render(request,"Login.html",{"form":form})
    

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    

        




