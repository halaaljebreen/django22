from django.shortcuts import render , redirect

# Create your views here.
people = []

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def add_person(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        person = Person(username, password)
        people.append(person)
        return redirect('people_list')
    return render(request, 'myapp/add.html')

def people_list(request):
    return render(request, 'myapp/people_list.html', {'people': people})