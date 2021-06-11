from django.contrib import admin

# Register your models here.


class NRMAdmin(admin.ModelAdmin):
    def get_search_description(self):
        try:
            desc = self.search_description
        except AttributeError:
            return ""
        return desc

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["search_description"] = self.get_search_description()
        return super().changelist_view(
            request,
            extra_context=extra_context,
        )
