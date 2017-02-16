from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from collections import defaultdict
from crum import get_current_request

class ArticleManage(models.Manager):
    def archive(self):
        date_list = Article.objects.datetimes('ctime', 'month', order='DESC')
        date_dict = defaultdict(list)
        for d in date_list:
            date_dict[d.year].append(d.month)
        return sorted(date_dict.items(), reverse=True)  # 模板不支持defaultdict


class Article(models.Model):
    STATUS_CHOICES = (
        (False, '草稿'),
        (True, '发布'),
    )
    AUTHORITY_CHOICES = (
        (0, '全员可见'),
        (1, '仅登录可见')
    )
    title = models.CharField('标题', max_length=200)
    author = models.ForeignKey(User, verbose_name="作者", blank=True, null=True,
                               help_text="不填默认为当前用户")
    picture = models.FileField("预览图片", upload_to="blog/img", blank=True, null=True)
    abstract = models.CharField('摘要', max_length=54, blank=True, null=True)
    content = RichTextField('正文')
    status = models.BooleanField('文章状态', default=False, choices=STATUS_CHOICES)
    user_auth = models.SmallIntegerField('阅读权限', default=0,
                                         choices=AUTHORITY_CHOICES)
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)
    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)
    ctime = models.DateTimeField("创建时间", auto_now_add=True)
    utime = models.DateTimeField("更新时间", auto_now=True)

    objects = ArticleManage()

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"
        ordering = ("-id",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'article_id': self.pk})

    def get_picture_url(self):
        return reverse('media', kwargs={'path': self.picture})

    # def save(self, from_web=False, *args, **kwargs):
    #     if not from_web:
    #         request = get_current_request()
    #         self.author = request.user
    #     super(Article, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    ctime = models.DateTimeField("创建时间", auto_now_add=True)
    utime = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"


class Tag(models.Model):
    name = models.CharField('标签名', max_length=20)
    ctime = models.DateTimeField("创建时间", auto_now_add=True)
    utime = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"
