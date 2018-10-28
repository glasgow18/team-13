from django.contrib import admin
from chatbot.models import Service, Tag, Location


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','description','link',)

    def name(self,obj):
        return obj.user.name

    def desciption(self,obj):
        return obj.user.description

    def link(self,obj):
        return obj.user.link

    def tag(self,obj):
        return obj.user.tag

    def location(self,obj):
        return obj.user.location


class TagAdmin(admin.ModelAdmin):
    list_display = ("tag",)

    def tag(self,obj):
        return obj.user.tag


class LocationAdmin(admin.ModelAdmin):
    list_display = ("location",)

    def location(self,obj):
        return obj.user.location


# Models Registration

admin.site.register(Service, ServiceAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Location, LocationAdmin)
