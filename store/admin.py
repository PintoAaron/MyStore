from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html,urlencode
from .models import User,Item,Category


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username', 'email','location', 'phone','post_items']
    list_per_page = 10
    search_fields = ['username']
    list_filter = ['location']
    
    @admin.display(ordering='total_items')
    def post_items(self,customer):
        url = (reverse('admin:store_item_changelist') + '?' + urlencode({'seller__id':str(customer.id)}))
        return format_html('<a href="{}">{}</a>',url,customer.total_items)
        
        
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(total_items = Count('items'))
        


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title','item_count']
    
    @admin.display(ordering='total_count')
    def item_count(self,category):
        url = (reverse('admin:store_item_changelist') + '?' + urlencode({'category__id':str(category.id)}))
        return format_html('<a href="{}">{}</a>',url,category.total_count)
    
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(total_count = Count('items'))
    
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','price','item_seller','condition','item_category','date_posted']
    list_per_page = 10 
    search_fields = ['name']
    list_filter = ['category','condition']
    list_select_related = ['seller','category']
    
    def item_seller(self,item):
        url = (reverse('admin:store_user_changelist') + '?' + urlencode({'user__id':str(item.seller.id)}))
        return format_html('<a href="{}">{}</a>',url,item.seller.username)
    
    
    def item_category(self,item):
        url = (reverse('admin:store_category_changelist') + '?' + urlencode({'category__id':str(item.category.id)}))
        return format_html('<a href="{}">{}</a>',url,item.category.id)



