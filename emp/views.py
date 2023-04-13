from django.shortcuts import render, redirect


# Create your views here.
from .models import Employee

# INDEX


def index(req):

    if req.method == 'POST':

        id = req.POST['id']
        name = req.POST['name']
        email = req.POST['email']
        city = req.POST['city']
        profession = req.POST['profession']
        if id:
            # FOR UPDATE USER

            emp = Employee.objects.get(id=id)

            emp.name = name
            emp.email = email
            emp.city = city
            emp.profession = profession
            emp.save()

            print('# UPDATE ------- USER')

        else:
            # FOR ADD USER

            emp = Employee(name=name, email=email,
                           city=city, profession=profession)
            emp.save()

            print('# ADD ------- USER')

    allEmp = Employee.objects.all()

    data = {
        'noOfCount': allEmp.count(),
        'noOfRecord': allEmp
    }

    return render(req, "index.html", data)
    # return HttpResponse("ddd>")


# DELETE :

def delete(req, emp_id):
    Employee.objects.get(pk=emp_id).delete()

    return redirect('/emp/')
