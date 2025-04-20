from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def home(request):
    return render (request, 'home.html')

def add_user(request):
    if request.method == 'POST':
        name=request.POST['name']
        address=request.POST['address']
        mail=request.POST['mail']
        mobile=request.POST['mobile']
        password=request.POST['password']

        obj=User()
        obj.Name=name
        obj.Mail=mail
        obj.Address=address
        obj.Mobile=mobile
        obj.Password=password
        obj.save()
        print("User saved:", obj)
    datas = User.objects.all()
    return render(request, 'Register.html', {'datas': datas})


def user_list(request):
    Datas=User.objects.all()
    if(Datas):
        return redirect(request,'Register.html', {'datas':Datas})
    else:
     return render (request,'Register.html')
 
 
def User_Update(request,user_id):
    orginal_data=User.objects.get(id=user_id)
    if request.method == 'POST':
        name=request.POST['name']
        mail=request.POST['mail']
        address=request.POST['address']
        mobile=request.POST['mobile']
        
        
        orginal_data.Name=name
        orginal_data.Mail=mail
        orginal_data.Address=address
        orginal_data.Mobile=mobile
        orginal_data.Password=orginal_data.Password
        orginal_data.save()
        return redirect('add_user')  # Or redirect to user_list if you want

    return render(request, 'Update.html', {'datas': orginal_data})


def Delete_User(request, user_id):
    datas=User.objects.get(id=user_id)
    datas.delete()
    return redirect('add_user')