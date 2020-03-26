from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm 

def signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
        else:
            return render(request, "signup.html", {"form": form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url
            })
    return render(request, "upload.html")
