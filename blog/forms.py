from django import forms
from .models import Article, Tag
from django.contrib.admin.widgets import FilteredSelectMultiple


class ArticleAdminForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
            queryset=Tag.objects.all(),
            required=False,
            widget=FilteredSelectMultiple(verbose_name='标签', is_stacked=False))

    class Meta:
        model = Article
        exclude = ("author", "views", "likes","ctime", "utime")

    def __init__(self, *args, **kwargs):
        super(ArticleAdminForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['tags'].initial = self.instance.tags.all()

    def save(self, commit=True):
        result = super(ArticleAdminForm, self).save(commit=False)
        if commit:
            result.save()
        if result.pk:
            result.tags = self.cleaned_data['tags']
            self.save_m2m()
        return result
