from django.shortcuts import render
from .models import RegistrationData
from django.http.response import HttpResponse
from .forms import RegistrationForm,LoginForm
def registration_page(request):
    rform = RegistrationForm(request.POST or None)
    context = {
        'form': rform
    }

    if rform.is_valid():
        print(rform.cleaned_data)

        firstname = rform.cleaned_data.get('firstname')
        lastname = rform.cleaned_data.get('lastname')
        username = rform.cleaned_data.get('username')
        email = rform.cleaned_data.get('email')
        password1 = rform.cleaned_data.get('password1')
        password2 = rform.cleaned_data.get('password2')
        mobile = rform.cleaned_data.get('mobile')

        data = RegistrationData(
            firstname=firstname,
            lastname=lastname,
            username=username,
            email=email,
            password1=password1,
            password2=password2,
            mobile=mobile
        )
        data.save()

    return render(request, 'reg_form.html', context)


def home_view(request):
    return render(request,'home.html')


def login_page(request):
    if request.method == "POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            uname = request.POST.get('username', '')
            pwd = request.POST.get('password1', '')
            uname1 = RegistrationData.objects.filter(username=uname)
            pwd1 = RegistrationData.objects.filter(password1=pwd)
            if uname1 and pwd1:
                return HttpResponse("Your Entered Correct Details")
            else:
                return HttpResponse("Your Entered Wrong Username or Password")
        else:
            return HttpResponse("Invalid Data")
    else:
        lform = LoginForm()
        return render(request, 'login_form.html', {'lform': lform})


def search_page(request):
    search_term = ''

    if 'search' in request.GET:
        search_term = request.GET['search']
        articles = RegistrationData.objects.all().filter(feeder__icontains=search_term)

    articles = RegistrationData.objects.all()

    return render(request, 'search.html', {'articles': articles, 'search_term': search_term})

    # rdata = RegistrationData.objects.all()
    # return render(request, 'search.html', {'rdata': rdata})
    # return render(request,'search.html')