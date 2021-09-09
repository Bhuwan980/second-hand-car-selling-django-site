from django.contrib import admin
from .models import *
from django.utils.html import format_html

# this above example is by using the decorator where teams is register by iteself by decorator and not need to register the teamsadmin
# Register your models here.
# @admin.register(Teams)
# class TeamsAdmin(admin.ModelAdmin):
#     list_display = ("id","image",  "first_name", "designation", "created_date")
#     ordering = ['id']
#     list_display_links = ('first_name', 'designation')

#     def image(self,obj):
#         return format_html('<img src="{0}" style="width: 20px; height:20px;" />'.format(obj.image.url))




class TeamsAdmin(admin.ModelAdmin):
    # for displaying the image in django amdin panel
    def image_tag(self, obj):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(obj.image.url))
    # changing the tiel of imge
    image_tag.short_description = 'Photo'
   
    list_display = ['id','image_tag',  'first_name', 'designation', 'created_date']
    # mkaing clickable link
    list_display_links = ('first_name','designation', 'image_tag')
    ordering = ('id',)

    # for searching
    search_fields = ('first_name', 'last_name', 'designation')
     
    

admin.site.register(Teams, TeamsAdmin)


class CarAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(obj.photo.url))

    list_display = ('image_tag', 'car_title', 'city', 'color', 'model', 'if_featured')
    list_display_links = ('car_title', 'city', 'color', 'model')
    search_fields = ('car_title', 'color', 'model', 'city', 'engine', 'price', 'year')
    list_editable = ('if_featured',)
    list_filter = ('state', 'year', )


admin.site.register(Car, CarAdmin)

admin.site.register(MoreCarImage)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','email', 'state', 'customer_need' )

admin.site.register(Contact, ContactAdmin)