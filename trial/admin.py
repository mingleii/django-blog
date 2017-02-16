from django.contrib import admin

# Register your models here.
from smallsite import settings
from trial.models import UploadFile


class UploadFileAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "file_url", "ctime", "utime")
    list_per_page = 20

    def file_url(self, obj):
        return u'<a target="_blank" href="{0}"> {1} </a>'.format(
            obj.file.url, obj.get_file_url())

    file_url.short_description = u"文件下载地址"
    file_url.allow_tags = True

admin.site.register(UploadFile, UploadFileAdmin)