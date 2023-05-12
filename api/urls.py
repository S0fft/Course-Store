from django.urls import path, include
from api.models import CourseResource, CategoryResource
from tastypie.api import Api


course_resource = CourseResource()
api = Api(api_name='v1')
api.register(CourseResource())
api.register(CategoryResource())

# urlpatterns = [
#     path('', inc)
# ]
