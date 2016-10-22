from django.conf.urls import url
import read, write

urlpatterns = [
    url(r'^apply/$', write.apply, name='apply')
]
