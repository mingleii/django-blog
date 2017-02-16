import os

from django.db import models

# Create your models here.
from smallsite import settings


class UploadFile(models.Model):
    name = models.CharField(u"名称", max_length=255, blank=True)
    file = models.FileField(u"文件", upload_to="upload/")
    remark = models.CharField(u"备注", max_length=255, blank=True, default="")
    ctime = models.DateTimeField("创建时间", auto_now_add=True)
    utime = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        verbose_name = "文件上传"
        verbose_name_plural = "文件上传"

    def get_file_url(self):
        return settings.SITE_HOST + self.file.url

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name
        super(UploadFile, self).save(*args, **kwargs)