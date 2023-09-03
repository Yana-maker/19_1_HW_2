from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        print(f'{name} ({email}): {massage}')
    return render(request, 'catalog/contacts.html')


