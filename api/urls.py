from django.conf.urls import url
import read, write

urlpatterns = [
    url(r'^apply/$', write.apply, name='apply'),
    url(r'^get_clients/$', read.search_clients, name='get_clients'),
    url(r'^get_applicants/$', read.get_applicants, name='get_applicants'),
    url(r'^mark_reviewed/$', write.mark_reviewed, name='mark_reviewed'),
    url(r'^get_shelters/$', read.get_shelters, name='get_shelters'),
    url(r'^update_shelter/$', write.update_shelter, name='update_shelters'),
    url(r'^new_client/$', write.new_client, name='new_client'),
    url(r'^get_user/$', read.profile, name='get_user'),
    url(r'^update_user/$', write.profile, name='update_user')
]
