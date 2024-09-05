from django.shortcuts import render,redirect
from . models import Student
# Create your views here.
def index(req):
    stu=Student.objects.all()
    studict={"stu":stu}
    return render(req,"index.html",studict)

def stureg(req):
    if req.method=="POST":
        rollno=req.POST["rollno"]
        stuname=req.POST["stuname"]
        branch=req.POST["branch"]
        year=req.POST["year"]
        #print(rollno,stuname,branch,destination,salary)
        emp=Student(rollno=rollno,stuname=stuname,branch=branch,year=year)
        emp.save()
        return redirect("index")

    return render(req,"stureg.html")

def delstu(req,id):
    stu=Student.objects.get(rollno=id)
    stu.delete()
    return redirect("index")

def editstu(req,id):
    stu=Student.objects.get(rollno=id)
    return render(req,"editstu.html",{"stu":stu})

#query for update 
def updatestu(req):
    rollno=req.POST["rollno"]
    stuname=req.POST["stuname"]
    branch=req.POST["branch"]
    year=req.POST["year"]
    Student.objects.filter(rollno=rollno).update(stuname=stuname,branch=branch,year=year)
    return redirect("index")