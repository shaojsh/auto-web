from django.conf.urls import url,include
from .views import index, uploadFiles, ApiTaskCreate, ApiTaskDataCreate

urlpatterns = [
    # 配置多级路由
    url(r'^index$', index),
    url(r'^$', index),
    url(r'^ApiTaskCreate', ApiTaskCreate),
    url(r'^uploadFiles', uploadFiles),
    url(r'^ApiTaskDataCreate', ApiTaskDataCreate),
]