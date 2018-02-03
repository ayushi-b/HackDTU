from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import *

# Create your views here.

def register(request):
    msg = None

    if request.method == "POST":
        if request.POST.get('register'):
            form1 = UserForm(request.POST)

            if form1.is_valid():
                user1 = form1.save(commit=False)
                username = form1.cleaned_data['user_name']
                password = form1.cleaned_data['user_password']
                user1.password = password
                user1.save()
                user1 = authenticate(username = username, password = password)
                if user1 is not None:
                    msg = "Email Id already registered!"
                    context = {
                    'msg':msg,
                    'form':UserForm(),
                    }
                    return render(request, "login.html", context)
                else:
                    return render(request, "front.html", {})

            else:
                return HttpResponse('<h1> Invalid form element! Please check the data submitted. </h1>')

        elif request.POST.get('login'):

            username = request.POST['user_email']
            password = request.POST['user_password']
            user2 = authenticate(user_email = username, password = password)
            if user2 is not None:
                return render(request, 'front.html', {})
            else:
                msg = "Incorrect E-mail or password :("
                context = {'form2': LoginForm(), 'msg': msg, 'form':UserForm()}
                return render(request, 'login.html', context)

        else:
            return HttpResponse('<h1>Wrong form element! </h1>')

    else:
        form = UserForm()
        form2 = LoginForm()
        context = {
        'msg':msg,
        'form':form,
        'form2':form2
        }
        return render(request, 'login.html', context)
