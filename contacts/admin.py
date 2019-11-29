from django.contrib import admin

from  .models import Contact,Inbox

# Register your models here.


class ContactAdmin(admin.ModelAdmin):

    list_display = ('id','listing_id', 'name', 'listing', 'email', 'contact_date', 'message','host_email','user_id','host_id','reply')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page =25

admin.site.register(Contact,ContactAdmin)


admin.site.register(Inbox)