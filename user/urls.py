from django.conf.urls import url,include

from .views import index

urlpatterns = [
    # 配置多级路由
    url(r'^index$', index),
    url(r'^$', index),
]