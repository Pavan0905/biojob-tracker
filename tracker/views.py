from django.shortcuts import render, redirect
from .models import Job
from django.core.mail import send_mail
import subprocess

def home(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'tracker/job_list.html', {'jobs': jobs})

def submit_job(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        Job.objects.create(name=name, email=email)
        return redirect('home')
    return render(request, 'tracker/submit.html')

def update_status(request, job_id, status):
    job = Job.objects.get(id=job_id)
    job.status = status
    job.save()

    if status == 'running':
        subprocess.Popen(["bash", "scripts/process_job.sh", str(job.id)])

    if status == 'done':
        send_mail(
            'Your Bioinformatics Job is Complete',
            f"Hi {job.name}, your job has finished successfully!",
            'admin@example.com',
            [job.email],
            fail_silently=True
        )

    return redirect('home')