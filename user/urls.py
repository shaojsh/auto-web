from django.conf.urls import url

from .views import reg, index

urlpatterns = [
    # 配置多级路由
    url(r'^reg$', reg),
    url(r'^index$', index),
]