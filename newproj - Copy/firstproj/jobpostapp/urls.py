from jobpostapp import views
from django.urls import path

urlpatterns =[
    path("",views.don,name='jobposts'),
    path("<int:pk>/",views.company_details.as_view(),name='job_details'),
    path('jobpost/',views.jobs,name='jobpost'),
    path('apply/',views.apply,name='apply'),
    path('posted/',views.posted,name='posted'),
    path('blog/',views.blogs,name="blog"),
    path("blogdetail/<int:id>/",views.blogdetail,name="blogdetail"),
    path("search/",views.search,name='search'),
    path('like/<int:id>/',views.like_post,name='like'),
    path('bookmark/<int:id>/',views.bookmarks,name='bookmark'),
    path('book_post',views.book_post,name='book_post'),
    path('like_post',views.liked_post,name='like_post')
]
