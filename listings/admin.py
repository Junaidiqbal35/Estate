from django.contrib import admin


from .models import Listing, Comment
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
        list_display  = ('id','title', 'is_published', 'price' , 'list_date' , 'host_id' ,)
        list_display_links = ('id','title')
        list_filter = ('host_id',)
        list_editable = ('is_published',)
        search_fields = ('title','address','city','state','zipcode','price',)
        list_per_page = 25

admin.site.register(Listing, ListingAdmin)

admin.site.register(Comment)

