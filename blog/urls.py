"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

# 模版
# def index(request):
#     print(request)
#     print(type(request))
#     return render(request,'index.html',{'user':'hello world'})
    #return HttpResponse('hello world')

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    # url(r'^index$', index),
    # 配置多级路由
    url(r'^user/', include('user.urls'))
]
