# _*_ coding:utf-8 _*_

from django.conf.urls import url, include
from .views import CourseListView, CourseDetailView, CourseInfoView, CourseComments, AddCommentsView, VideoPlayView

urlpatterns = [
    #courses url
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    #课程详情
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),
    #
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),
    #课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CourseComments.as_view(), name="course_comment"),

    #添加评论
    url(r'^add_comment/$', AddCommentsView.as_view(), name="add_comment"),

    #视频地址
    url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name="video_play"),
]