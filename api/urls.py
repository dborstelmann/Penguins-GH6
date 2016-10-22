from django.conf.urls import url
import read, write

urlpatterns = [
    url(r'^apply/$', write.apply, name='apply'),
    url(r'^get_clients/$', read.search_clients, name='get_clients'),
    url(r'^get_applicants/$', read.get_applications, name='get_applicants'),
    url(r'^mark_reviewed/$', write.mark_reviewed, name='mark_reviewed')
]
