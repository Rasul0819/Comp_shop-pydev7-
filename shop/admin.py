from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


admin.site.register(models.Category)
admin.site.register(models.Company)

@admin.register(models.Product)
class CustomProductAdmin(admin.ModelAdmin):

    list_display = ['image_show','model_name','category_name',
                    'company_name','count','date','price','sale_off',]
    list_filter = ['price','count','company_name','category_name',]
    list_display_links=['model_name','count']
    list_editable = ['price','sale_off']
    def image_show(self,obj):
        if obj.image1:
            return mark_safe(f"<img src={obj.image1.url} width=60 />")
        return None
    image_show.__name__='Картинка'

