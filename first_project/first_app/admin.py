from django.contrib import admin
from first_app.models import AccessRecord, Topic, Web, User, User_info


# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Web)
admin.site.register(User)
admin.site.register(User_info)