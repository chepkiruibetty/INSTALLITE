from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.usersignup, name='register_user'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),
    url(r'^post/$', views.post,name='post'), 
    url(r'^image/$', views.image_upload,name='upload'),
    url(r'^user/$',views.search_user,name='search_user'),
    url(r'^profile/$', views.profile_info,name='profile'),
    url(r'^edit/$',views.profile_edit,name='edit'),
    url(r'^new_comment/(\d+)/$' ,views.add_comment,name='Comments'),
    url(r'likes/(\d+)/$', views.likes, name="likes"),


    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)