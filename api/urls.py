from django.conf.urls import url
import read, write

urlpatterns = [
    url(r'^apply/$', write.apply, name='apply'),
    url(r'^get_clients/$', read.search_clients, name='get_clients'),
    url(r'^get_applicants/$', read.get_applicants, name='get_applicants'),
    url(r'^mark_reviewed/$', write.mark_reviewed, name='mark_reviewed'),
    url(r'^get_shelters/$', write.get_shelters, name='get_shelters'),
    url(r'^update_shelters/$', write.update_shelters, name='update_shelters')

]
