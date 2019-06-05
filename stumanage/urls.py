from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.sm_user.urls', namespace='sm_user')),
    url(r'^sm_teacher/', include('apps.sm_teacher.urls', namespace='sm_teacher')),
    url(r'^sm_class_head/', include('apps.sm_class_head.urls', namespace='sm_class_head')),
    url('^sm_edu_admin/',include('apps.sm_edu_admin.urls',namespace='sm_edu_admin')),
]
