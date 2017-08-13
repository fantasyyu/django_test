# _*_ coding:utf-8 _*_

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

from .models import Course, CourseResource, Video
from operation.models import UserFavoriate, CourseComments, UserCourse
from utils.mixin_utils import LoginRequiredMixin

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")

        hot_courses = Course.objects.all().order_by("-click_nums")[:3]

        #课程排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_courses = all_courses.order_by("-students")
            elif sort == 'hot':
                all_courses = all_courses.order_by("-click_nums")

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 5, request=request)

        courses = p.page(page)
        return render(request, 'course-list.html', {
            "all_courses": courses,
            "sort": sort,
            "hot_courses": hot_courses
        })


class CourseDetailView(View):

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()

        has_fav_course = False
        has_fav_org = False

        if request.user.is_authenticated():
            #判断用户登录状态
            if UserFavoriate.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course=True
            if UserFavoriate.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org=True

        tag = course.tag
        if tag:
            relate_courses = Course.objects.get(tag=tag)[:1]
        else:
            relate_courses=[]
        return render(request, "course-detail.html", {
            "course": course,
            "relate_courses": relate_courses,
            "has_fav_course": has_fav_course,
            "has_fav_org": has_fav_org
        })


class CourseInfoView(LoginRequiredMixin, View):

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course.students+1
        course.save
        #查询用户是否已经关联了课程
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()

        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)  # 加上__in 是传入一个list  django特有属性
        course_ids=[user_course.course.id for user_course in all_user_courses]  # 取出所有课程id
        related_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
        all_resources = CourseResource.objects.filter(course=course)
        return render(request, "course-video.html", {
            "course": course,
            "course_resources": all_resources,
            "related_courses": related_courses
        })


class CourseCommentView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_resources = CourseResource.objects.filter(course=course)
        all_comments = CourseComments.objects.all()
        return render(request, "course-comment.html", {
            'course': course,
            'course_resources': all_resources,
            'all_comments': all_comments
        })


class AddCommentsView(View):
    """
    用户添加评论
    """
    def post(self, request):
        if not request.user.is_authenticated():
            #判断用户登录状态
            return HttpResponse('{"status": "fail", "msg": "user not login"}',  content_type='application/json')

        course_id = request.POST.get("course_id", 0)
        comment = request.POST.get("comments", "")

        if course_id > 0 and comment:
            course_comments = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments.comments = comment
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}',  content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg": "添加失败"}',  content_type='application/json')


class VideoPlayView(View):
    #视频播放页面
    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))
        course = video.lesson.course
        #查询用户是否已经关联了课程
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()

        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)  # 加上__in 是传入一个list  django特有属性
        course_ids=[user_course.course.id for user_course in all_user_courses]  # 取出所有课程id
        related_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
        all_resources = CourseResource.objects.filter(course=course)
        return render(request, "course-play.html", {
            "course": course,
            "course_resources": all_resources,
            "related_courses": related_courses,
            "video": video
        })