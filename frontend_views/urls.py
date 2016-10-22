from django.conf.urls import url
import views as v

urlpatterns = [
    url(r'^$', v.base_view, name='base'),
    url(r'^apply$', v.apply_view, name='apply'),
    url(r'^home$', v.home_view, name='home'),
    url(r'^submit$', v.submit_view, name='submit'),
    url(r'^map$', v.map_view, name='map')
]
