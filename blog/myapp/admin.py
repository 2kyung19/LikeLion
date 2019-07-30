from django.contrib import admin
from .models import Blog
from .models import Guest
from .models import Gallery
# Register your models here.

admin.site.register(Blog)
admin.site.register(Guest)
admin.site.register(Gallery)