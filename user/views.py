import os

from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render


# index画面跳转
def index(request: HttpRequest):
    return render(request, 'index.html')


# appiumAutoTest画面跳转
def appiumAutoTest(request: HttpRequest):
    return render(request, 'appiumAutoTest.html')


def uploadFiles(request: HttpRequest):
    if request.method == "POST":
        if request.POST.get("upload") == "upload":
            myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
            if myFile:
                destination = open(os.path.join("C:\\Users\\Administrator\\IdeaProjects\\untitled\\src\\main\\resources", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
                for chunk in myFile.chunks():  # 分块写入文件
                    destination.write(chunk)
                destination.close()
                return HttpResponse("upload successful!")
            else:
                return HttpResponse("upload fail......")
