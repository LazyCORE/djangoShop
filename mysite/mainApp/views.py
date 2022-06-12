from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html', )

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Якщо у вас є питання то задавайте їх мені по телефону',
                                                              '(098) 83-87-870']})

