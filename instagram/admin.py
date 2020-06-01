from django.contrib import admin
from .models import Images, Profiles, Comments

# Register your models here.
admin.site.register(Profiles)
admin.site.register(Images)
admin.site.register(Comments)
