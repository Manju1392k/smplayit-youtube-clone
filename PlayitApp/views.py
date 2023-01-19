from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Videos

# Function for Homepage Render, Videos Thumbline data fetching
def Home(request):
    # messages.success(request, 'Home pages changing text')
    # Fetching all videos
    allvideos = Videos.objects.all()
    return render(request, 'index.html', {'allvideos':allvideos})

#Function for Videoplaying page render, fetching only one video, recommended videos
def Videoplaying(request, video_id):
    # Fetching only one id video for playing
    onevideo = Videos.objects.get(pk = video_id)
    # Removing playing video
    allvideos = Videos.objects.exclude(id=video_id)
    return render(request, 'playvideo.html', {'onevideo':onevideo, 'allvideos':allvideos})

# Function for UploadVideo page render, saving the video
def uploading(request):
    try:
        if request.method == 'POST':
            Video_Tittle = request.POST.get('Video_Tittle')
            Video_Description = request.POST.get('Video_Description')
            Video_Thumbline = request.FILES.get('Video_Thumbline')
            Video = request.FILES.get('Video')

            # Input tag and model name is same
            savingvideo = Videos(Video_Tittle=Video_Tittle, Video_Description=Video_Description,
                                 Video_Thumbline=Video_Thumbline, Video=Video)
            savingvideo.save()
            messages.success(request, 'video has been uploaded successfully')

            return redirect('home')
    except:
        messages.error(request, 'unable to upload please upload it later')
        return redirect('home')

    return render(request, 'upload.html')

# Function for Search feature
def search(request):
    try:
        if request.method == 'POST':
            search = request.POST.get('search')
            result = Videos.objects.filter(Video_Tittle__contains = search)
            return render(request, 'index.html', {'result':result})
        else:
            return render(request, 'index.html')
    except:
        messages.error(request, 'something went wrong')
        return redirect('home')


