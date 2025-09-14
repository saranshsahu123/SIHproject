from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Candidate
from django.contrib import messages
from django.contrib.auth.hashers import make_password

def deshBord(request):

    candidate = Candidate.objects.get(id=1)
    username = candidate.name
    useremail = candidate.email
    jobRole = candidate.role


    job_roles = {
        "Full Stack Developer": ["python", "django", "html", "css", "javascript", "react", "node"],
        "Software Engineer": ["java", "python", "c++", "problem solving", "algorithms"],
        "DevOps Engineer": ["docker", "kubernetes", "aws", "jenkins", "terraform", "ansible", "linux"],
        "Data Scientist": ["python", "machine learning", "data analysis", "pandas", "numpy", "tensorflow"],
        "Cloud Engineer": ["aws", "azure", "gcp", "cloud computing", "vpc", "load balancer"]
    }

    skills = []
    for key in job_roles:

        if key == jobRole :
            skills = job_roles[key]


    data = {
        "name": username,
        "email": useremail,
        "skills" : skills ,
    }

    return render(request , 'deshbord.html' , {'data': data} )

# Create your views here.
def login_candidate(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Search candidate
        candidate = Candidate.objects.filter(email=email).first()

        if candidate:
            # Check password
            if check_password(password, candidate.password):
                # Successful login
                 return redirect('deshBord')
            else:
                # Password incorrect
                return render(request, 'login.html', {'error': 'Invalid password'})
        else:
            # Email not found
            return render(request, 'login.html', {'error': 'Candidate not found'})

    return render(request, 'login.html')


def sign_up(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        # Check if Candidate already exists
        if Candidate.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('deshBord')

        # Hash the password before saving
        hashed_password = make_password(password)

        # Save Candidate to database
        candidate = Candidate(name=name, email=email, password=hashed_password, role=role)
        candidate.save()

        messages.success(request, 'Registration successful. Please log in.')
        return redirect('login_candidate')

    return render(request, 'signin.html')