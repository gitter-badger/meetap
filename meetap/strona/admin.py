from django.contrib import admin


# Register your models here.
from .models import (
 PageNames, Blog, PageSkin, BlogNames, RegNames, ProfileNames)


admin.site.register(PageNames)
admin.site.register(Blog)
admin.site.register(PageSkin)
admin.site.register(BlogNames)
admin.site.register(RegNames)
admin.site.register(ProfileNames)
