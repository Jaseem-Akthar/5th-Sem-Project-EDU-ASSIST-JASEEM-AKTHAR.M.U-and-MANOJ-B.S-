from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from module1.models import *
from .forms import UploadForm

# Create your views here.

def index(request):
    return render(request,"index.html")

def form(request):
    return render(request,"form.html")

def drag(request):
    if(request.session._session):
        return render(request,"drag.html")
    else:
        return render(request,"form.html")


def video(request):
    if(request.session._session):
        return render(request,"video.html")
    else:
        return render(request,"form.html")



def signup(request):
    if(request.POST.get('email')):
        email=request.POST.get('email')
        pswd=request.POST.get('pswd')
        confirmpassword=request.POST.get('confirmpassword')
        list_of_users=usercrd.objects.values_list(flat=True)
        if(email not in list_of_users):
            # print("----------------------------->>>>>>>>>>>>>",password,confirmpassword)
            if(pswd==confirmpassword):

                usercrd(email=email,pswd=pswd,confirmpassword=confirmpassword).save()
                return HttpResponseRedirect('signup')
            else:
                # print("_________________________________________22222")
                return render(request,'form.html',{'msg':'PASSWORD NOT MATCHING'})
        else:
                # print("*******************************************")
                return render(request,'form.html',{'msg':'USER REGISTERED SUCCESFULLY!!'})
    else:
       return render(request,"form.html")

def signin(request):
    if(request.POST.get('email')):
        email=request.POST.get('email')
        pswd=request.POST.get('pswd')
        # print("----------->",email,password)
        list_of_users=usercrd.objects.values_list(flat=True)
        if(email in list_of_users):
            temp=usercrd.objects.get(email=email)
            if(temp.pswd==pswd):
                request.session['email']=email
                return render(request,"index.html",{'username':email})
            else:
                return render(request,"form.html",{'msg':'WRONG PASSWORD!!'})
        else:
                return render(request,"form.html",{'msg':'USER NOT REGISTERED!! *PLEASE REGISTER*'})
    else:
                return render(request,"index.html")

def file_upload(request):
    if request.method == 'POST':
        print(">>>>>>>",request.FILES)
        image = request.FILES['upfile']
        fs = FileSystemStorage()
        imagedata(iname=image, imagePath=image).save()
        return render(request, "drag.html",{'path':'/notes/'+image.name})
    else:
        return render(request,"drag.html")

def contact(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    number=request.POST.get('number')
    course=request.POST.get('course')
    # gender=request.POST.get('gender')
    usercontact(name=name,email=email,number=number,course=course).save()
    return render(request,"index.html")



# def file_upload(request):
#     context = {}
#     if request.method == 'POST':
#         iname = request.FILES['file_upload']
#         fs = FileSystemStorage()
#         imagedata = fs.save(iname.name, imagePath)
#         context['url'] = fs.url(imagedata)
#     return render(request, 'drag.html', context)


# def file_upload(request):
#     form = UploadForm()
#     context = {'form':form}
#     return render(request, 'drag.html', context)

def download(request):
    files = imagedata.objects.all()
    context = {'files':files}
    return render(request, "download.html", context)

# def download(request):
#     if(request.session._session):
#         return render(request,"download.html")
#     else:
#         return render(request,"form.html")
