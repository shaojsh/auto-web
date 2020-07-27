import os

from django.core.paginator import PageNotAnInteger
from django.http import HttpRequest
import time

from pure_pagination import Paginator

from .ExcelDataHandle import ReadExcel
from .models import ApiTask


# 接口任务创建DB登录
def InsertApiTaskData(request: HttpRequest):
    if request.method == "POST":
        # 获取上传的excel文件
        myFile = request.FILES.get("myfile", None)
        if myFile:
            # 写入文件
            filepath = ".//user//Excel//AutoTestData.xlsx"
            destination = open(os.path.join(filepath), 'wb+')
            for chunk in myFile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
            data = ReadExcel(filepath, "api-reqdata")
            projectApiPare = data.keys
        else:
            projectApiPare = ""
        UserName = 'sjs'
        email = '2319898128@qq.com'
        projectBlongTo = request.POST.get('project')
        projectEnvir = request.POST.get('evn')
        projectApiName = request.POST.get('taskName')
        projectApiDes = request.POST.get('taskDes')
        projectApiPath = request.POST.get('ApiPath')
        projectApiReqWay = request.POST.get('ApiPath')
        projectCreatDate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        # 执行插入语句文件
        ApiTask.objects.create(  # 执行插入语句
            UserName=UserName,
            email=email,
            projectBlongTo=projectBlongTo,
            projectEnvir=projectEnvir,
            projectApiName=projectApiName,
            projectApiDes=projectApiDes,
            projectApiPath=projectApiPath,
            projectApiReqWay=projectApiReqWay,
            projectApiPare=projectApiPare,
            projectCreatDate=projectCreatDate
        )
        datas = ApiTask.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(datas, 80, request=request)
        return p.page(page)


