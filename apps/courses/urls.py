# _*_ coding:utf-8 _*_

from django.conf.urls import url, include
from .views import CourseListView, CourseDetailView

urlpatterns = [
    #courses url
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    #课程详情
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),
]