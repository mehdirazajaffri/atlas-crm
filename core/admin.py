from django.contrib import admin

admin.site.site_header = "Atlas Admin"
admin.site.site_title = "Atlas Admin"


class BaseAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    actions_on_bottom = True
    actions_on_top = False
    list_per_page = 50
    empty_value_display = "N/A"
    ordering = ("-updated_at",)
