from django.contrib.auth import login,authenticate
from django.shortcuts import render,redirect
from django.contrib import messages

from PIL import Image
# import keras
import numpy as np
#import os
from django.core.files.storage import FileSystemStorage

#for intergration
media='media'
# model=keras.models.load_model('3person.h5')

def home(request):
    return render(request,'upload.html')

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,('Provide valid usename and password..Try again!!!'))
            return redirect('login')
            
    else:
        return render(request,'login.html',{})
def makeVerification(path):
    #we can open the image
    img=Image.open(path)
    #we resize the image for the model
    img_d=img.resize((244,244))
    #we check if image is RGB or not
    if len(np.array(img_d).shape)<4:
        rgb_img=Image.new("RGB",img_d.size)
        rgb_img.paste(img_d)
    else:
        rgb_img=img_d
    #here we convert the image into numpy array and reshape
    rgb_img=np.array(rgb_img,dtype=np.float64)
    rgb_img=rgb_img.reshape(244,244)

    #make verification logic here
    #def verification

    #this is the process of preprocessing
def upload_verfiy(request):
    if request.method=="POST" and request.FILES['filePath']:
        if 'filePath' not in request.FILES:
            err='No Image Selected'
            return render(request,'upload.html',{
                'err':err
            })
        f=request.FILES['filePath']
        if f=='':
            err='No files selected'
            return render(request,'upload.html',{
                'err':err
            })
        filePath=request.FILES['filePath']
        fss=FileSystemStorage()
        file=fss.save(filePath.name,filePath)
        file_url=fss.url(file)
        #verification=makeVerification(os.path.join(media,file))
        return render(request,'upload.html',{
            'file_url':file_url
        })
    else:
        return render(request,'upload.html')
