from django.conf.urls import include, url
# from django.urls import path

from django.contrib import admin
admin.autodiscover()
from django.contrib.auth import views as auth_views

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    # url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url('admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'user_auth/register.html'}),
    url(r'^logout/$', auth_views.logout),
    url(r'^animals/$', include('api.urls')),
    url(r'^', include('user_auth.urls'))
]
