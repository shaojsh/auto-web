import os

from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render
# index画面跳转
from user import API


def index(request: HttpRequest):
    return render(request, 'index.html')


# 自动化(API)任务创建画面跳转
def ApiTaskCreate(request: HttpRequest):
    return render(request, 'ApiTaskCreate.html')


# 自动化(API)任务创建
def ApiTaskDataCreate(request: HttpRequest):
    data = API.InsertApiTaskData(request)
    return render(request, "ApiTasks.html", {"data": data})


# appiumAutoTest画面跳转
def appiumAutoTest(request: HttpRequest):
    # L = []
    L_PhoneType = []
    L_ExcelType = []
    L_JavaType = []
    filePhoneType = 'C:\\Users\\Administrator\\IdeaProjects\\untitled\\src\\main\\resources'
    fileJavaType = 'C:\\Users\\Administrator\\IdeaProjects\\untitled\\src\\test\\java\pajk\\folw'
    # 手机类型
    for root, dirs, files in os.walk(filePhoneType):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                L_PhoneType.append(file)

    # EXCEL类型
    for root, dirs, files in os.walk(filePhoneType):
        for file in files:
            if (os.path.splitext(file)[1] == '.xls') | (os.path.splitext(file)[1] == '.xlxs'):
                L_ExcelType.append(file)

    # JAVA类型
    for root, dirs, files in os.walk(fileJavaType):
        for file in files:
            if os.path.splitext(file)[1] == '.java':
                L_JavaType.append(file)

    return render(request, "appiumAutoTest.html",
                  {"L_PhoneType": L_PhoneType, "L_ExcelType": L_ExcelType, "L_JavaType": L_JavaType})


def uploadFiles(request: HttpRequest):
    if request.method == "POST":
        if request.POST.get("upload") == "upload":
            myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
            if myFile:
                destination = open(
                    os.path.join("C:\\Users\\Administrator\\IdeaProjects\\untitled\\src\\main\\resources", myFile.name),
                    'wb+')  # 打开特定的文件进行二进制的写操作
                for chunk in myFile.chunks():  # 分块写入文件
                    destination.write(chunk)
                destination.close()
                return HttpResponse("upload successful!")
            else:
                return HttpResponse("upload fail......")
