from django.contrib import admin
from .models import Image

class CustomImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)

    def get_search_results(self, request, queryset, search_term):
        if search_term:
            queryset, use_distinct = super().get_search_results(request, queryset, search_term)
            return queryset, use_distinct
        return super().get_search_results(request, queryset, search_term)

admin.site.register(Image, CustomImageAdmin)
