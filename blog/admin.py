from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'intro',
        'body',
        'image',
    )

    exclude = ('slug',)


admin.site.register(Post, PostAdmin)
