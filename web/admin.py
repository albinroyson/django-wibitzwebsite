
from django.contrib import admin
from web.models import Customer, Subscribe,Feature

# Register your models here.
admin.site.register(Subscribe)

admin.site.register(Customer)

class FeatureAdmin(admin.ModelAdmin):
     list_display=["image","icon","icon_background","title",
    "testimonial_description","testimonial_author",
    "auther_desigination","testimonial_logo","description"]

    
admin.site.register(Feature)