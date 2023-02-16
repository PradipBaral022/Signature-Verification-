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
    import tensorflow as tf
    import matplotlib.pyplot as plt
    import cv2
    import os
    import numpy as np
    from tensorflow.keras.preprocessing.image import ImageDataGenerator,array_to_img, img_to_array
    from tensorflow.keras.preprocessing import image
    import pandas as pd
    import itertools
    import sklearn
    #this is for submitted image to array
    folder="media_path"
    def load_images_from_folder(folder_path):
        for image in os.listdir(folder_path):
            img_arr= cv2.imread(os.path.join(folder,image),cv2.IMREAD_GRAYSCALE)
            img_arr=img_arr/255
            new_arr=cv2.resize(img_arr,(70,70))
            return new_arr
    img=load_images_from_folder(folder)

    #this for customer id to image convert
    DATADIR="C:/Users/safal/Downloads/archive (3)/sign_data/sign_data/train"
    CATEGORIES=['001','002','003']
    data=[]#this is a list
    labl=[]
    def create_image_data():
        for category in CATEGORIES:
            class_num=CATEGORIES.index(category)
            path=os.path.join(DATADIR,category)#path to 001 or 001_forg or 002 ----dir
            for img in os.listdir(path):
                    img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                    img_array=img_array/255
                    new_array=cv2.resize(img_array,(70,70))
                    #print(new_array)
                    data.append([new_array])
                    labl.append(class_num)
    create_image_data()
    labl= np.array(labl)
    images= np.array(data)
    images=np.reshape(images,(72,70,70))
    if cid=="001":
        label=0
        image=images[label]
    elif cid=="002":
        label=24
        image=images[label]
    elif cid=="003":
        label=49
        image=images[label]
    else:
        error_message="not a valid customer id"
    

    #customer id bata derieve vako image 'image' variable ma xa ani submit garda deko image chai 'img' array ma aaxa
    #the code below is for loading the model
    from tensorflow.keras.models import load_model
    siamese_model=load_model('3person.h5')
    verification=siamese_model.predict([image.reshape((1, 100, 100)), img.reshape((1, 100, 100))]).flatten()
    verification=verification*100
    if(verification>=80):
        print("real")
    else:
        print("forgery")


        
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
