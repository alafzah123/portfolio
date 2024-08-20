from django.contrib import admin
from .models import Client,ImageMedia,Project,Testimonial
# Register your models here.

admin.site.register(Client)
admin.site.register(ImageMedia)
admin.site.register(Testimonial)
admin.site.register(Project)