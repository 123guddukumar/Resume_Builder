from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Resume

# Create your views here.
def index(request):
    return render(request, 'index.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Check if user already exists
        user_exists = User.objects.filter(username=username).exists()

        if user_exists:
            # Log in the existing user
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('/')  # Replace 'home' with the name of your home page URL pattern
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Log in the new user
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, 'Account created and logged in successfully!')
            return redirect('/')
    return render(request, 'singup.html')

@login_required
def template1(request):
    context = {'resume':Resume.objects.all()}
    if request.user.is_authenticated:
        return render(request,'next2.html',context)
    return redirect('signup')



def template2(request):
    context = {'resume':Resume.objects.all()}
    if request.user.is_authenticated:
        return render(request,'next3.html',context)
    return redirect('signup')

def upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            f_name = request.POST.get('f_name')
            l_name = request.POST.get('l_name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            address = request.POST.get('address')
            dob = request.POST.get('dob')
            about = request.POST.get('about')
            gender = request.POST.get('gender')
            
            graduation = request.POST.get('graduation')
            start_grad = request.POST.get('start_grad')
            end_grad = request.POST.get('end_grad')
            grad_marks = request.POST.get('grad_marks')
            
            inter = request.POST.get('inter')
            start_inter = request.POST.get('start_inter')
            end_inter = request.POST.get('end_inter')
            inter_marks = request.POST.get('inter_marks')
            
            tenth = request.POST.get('tenth')
            start_ten = request.POST.get('start_ten')
            end_ten = request.POST.get('end_ten')
            ten_marks = request.POST.get('ten_marks')
            
            experience= request.POST.get('experience')
            ex_job = request.POST.get('ex_job')
            start_job = request.POST.get('start_job')
            end_job = request.POST.get('end_job')
            skills = request.POST.get('skills')
            hobbies = request.POST.get('hobbies')
            
            project = request.POST.get('project')
            project_link = request.POST.get('project_link')
            
            project1 = request.POST.get('project1')
            project_link1 = request.POST.get('project_link1')
            
            project2 = request.POST.get('project2')
            project_link2 = request.POST.get('project_link2')
            
            achievement = request.POST.get('achievement')
            position = request.POST.get('position')
            achievement1 = request.POST.get('achievement1')
            position1 = request.POST.get('position1')
            achievement2 = request.POST.get('achievement2')
            position2 = request.POST.get('position2')
            
            resume = Resume(f_name=f_name,
                            l_name=l_name,
                            email=email,
                            number=number,
                            address=address,
                            dob=dob, 
                            about=about,
                            gender=gender,
                            
                            experience=experience,
                            ex_job=ex_job,
                            start_job=start_job,
                            end_job=end_job,
                    
                            graduation=graduation,
                            start_grad=start_grad,
                            end_grad=end_grad,
                            grad_marks=grad_marks,
                            
                            inter=inter,
                            start_inter=start_inter,
                            end_inter=end_inter,
                            inter_marks=inter_marks,
                            
                            tenth=tenth,
                            start_ten=start_ten,
                            end_ten=end_ten,
                            ten_marks=ten_marks,
                            
                            project=project,
                            project_link=project_link,
                            project1=project1,
                            project1_link=project_link1,
                            project2=project2,
                            project_link2=project_link2,
                            
                            skills=skills,
                            hobbies=hobbies,
                            achievement=achievement,
                            position=position,
                            achievement1=achievement1,
                            position1=position1,
                            achievement2=achievement2,
                            position2=position2,
                                )
            resume.save()
        return render(request,'upload_detail.html')
    else:
        return render(request,'Pages/login.html')

# For Download PDF file......
import pdfkit
from django.urls import reverse

# Correct the path separator and check for typos
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

def generatePDF(request):
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('index')), False, configuration=config)
    response = HttpResponse(pdf, content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="file_name.pdf"'

    return response


