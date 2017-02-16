from django.contrib import admin

from blog.forms import ArticleAdminForm
from blog.models import Article, Category, Tag

class ArticleAdmin(admin.ModelAdmin):
    fields = ("title", "picture", "abstract", "content", "status", "user_auth",
              "topped", "category", "tags", "author")
    list_display = ("title_display", "category", "author_name", "status",
                    "user_auth", "topped", "ctime", "utime")
    search_fields = ("author__username", "title")
    list_filter = ("ctime", "utime", "author", "category")
    list_editable = ("status", )
    list_per_page = 20

    # form = ArticleAdminForm

    def title_display(self, obj):
        if len(obj.title) > 30:
            return obj.title[:30] + " ......"
        return obj.title

    title_display.short_description = "标题"

    def author_name(self, obj):
        return obj.author.username

    author_name.short_description = "作者"

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        if not obj.author:
            obj.author = request.user
        obj.save()


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
