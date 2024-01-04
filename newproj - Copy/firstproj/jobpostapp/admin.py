from django.contrib import admin

from jobpostapp.models import job_posts,job,add_job,comment

# Register your models here.
admin.site.register(job_posts),
admin.site.register(job)
admin.site.register(add_job)
admin.site.register(comment)


