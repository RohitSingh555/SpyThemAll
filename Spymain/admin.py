from django.contrib import admin

# Register your models here.
from .models import Models_info, model_assets

admin.site.register(Models_info)
admin.site.register(model_assets)