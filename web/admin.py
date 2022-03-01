
from django.contrib import admin
from web.models import Customer, Subscribe,Feature,Video,Profile,Marketing,Studio,Blog

# Register your models here.
admin.site.register(Subscribe)

admin.site.register(Customer)

class FeatureAdmin(admin.ModelAdmin):
     list_display=["image","icon","icon_background","title",
    "testimonial_description","testimonial_author",
    "auther_desigination","testimonial_logo","description"]
admin.site.register(Feature,FeatureAdmin)


class VideoAdmin(admin.ModelAdmin):
     list_display=["image","icon","title"]
admin.site.register(Video,VideoAdmin)


class ProfileAdmin(admin.ModelAdmin):
     list_display=["image","icon","discribe","desigination","company"]
admin.site.register(Profile,ProfileAdmin)


class MarketingAdmin(admin.ModelAdmin):
     list_display=["image","title","discribe"]
admin.site.register(Marketing,MarketingAdmin)


class StudioAdmin(admin.ModelAdmin):
     list_display=["icon","image","title","discribe"]
admin.site.register(Studio,StudioAdmin)

class BlogAdmin(admin.ModelAdmin):
     list_display=["image","discribe"]
admin.site.register(Blog,BlogAdmin)