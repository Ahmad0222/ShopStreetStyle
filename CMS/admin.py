from django.contrib import admin
from .models import FeaturedCollection, Featured, Banner, AvailableBrand, Spotlight
# Register your models here.
admin.site.register(Banner)
admin.site.register(AvailableBrand)
admin.site.register(Spotlight)

class FeaturedCollectionAdmin(admin.ModelAdmin):
    list_display = ('productName', 'category')
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(FeaturedCollection, FeaturedCollectionAdmin)

class FeaturedAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(Featured, FeaturedAdmin)