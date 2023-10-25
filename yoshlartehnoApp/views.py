from django.shortcuts import render
from .models import Project, Video
from django.http.response import StreamingHttpResponse
from .camera import IPWebCam
# Create your views here.


def home(request):
    return render(request, 'index.html', {'video_list' : Video.objects.all()})

def about(request):
    return render(request, 'about.html', {'video_list' : Video.objects.all()})

def project(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects' : projects})

def contact(request):
    return render(request, 'contact.html')

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def webcam_feed(request):
	return StreamingHttpResponse(gen(IPWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')
