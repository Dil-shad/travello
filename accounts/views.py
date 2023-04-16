from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def signup(request):
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            email = request.POST['email']

            if password == cpassword:  # password matching......
                # check Username Already Exists..
                if User.objects.filter(username=username).exists():
                    messages.info(
                        request, 'This username already exists!!!!!!')
                    
                    return redirect('signup')
                else:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        password=password,
                        email=email)
                    user.save()
                   
                    print("User Created")
                    messages.info(request, 'User Registered')
            else:
                messages.info(request, 'Password doesnt match!!!!!!!')
                print("Password is not Matching.. ")
                # return redirect('signup')
                return redirect('/')
        except:
            messages.info(request, 'Something wrong..!!')

    return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            #messages.info(request, f'Welcome {username}')
            return redirect('/')
        else:
            messages.info(request, 'Invalid Username or Password. Try Again.')
            return redirect('login_page')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')