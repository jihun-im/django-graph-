from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^blog/', include('blog.urls')),
    url(r'^urllist/', include('urllist.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
