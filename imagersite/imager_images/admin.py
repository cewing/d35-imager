from django.contrib import admin
from django.core.urlresolvers import reverse

from .models import Photo, Album


class PhotoInAlbumForPhotosInline(admin.TabularInline):
    model = Album.photos.through

    min_num = 1
    extra = 0
    verbose_name = 'album'


class PhotoInAlbumForAlbumsInline(PhotoInAlbumForPhotosInline):
    model = Album.photos.through
    verbose_name = 'photo'


class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInAlbumForAlbumsInline, )
    list_display = [
        'owner', '__str__', 'date_created', 'date_modified', 'published', 'count'
    ]
    list_display_links = ['__str__', ]
    readonly_fields = ['date_created', 'date_modified']

    def owner(self, obj):
        owner = obj.user
        url = reverse('admin:auth_user_change', args=(owner.pk,))
        name = owner.get_full_name() or owner.username
        link = '<a href="{}">{}</a>'.format(url, name)
        return link
    owner.short_description = 'Owner'
    owner.allow_tags = True

    def count(self, obj):
        return obj.photos.count()
    count.short_description = '# of Photos'

class PhotoAdmin(admin.ModelAdmin):
    inlines = (PhotoInAlbumForPhotosInline, )
    list_display = [
        'owner', '__str__', 'date_uploaded', 'date_modified','published'
    ]
    list_display_links = ['__str__', ]
    readonly_fields = ['date_uploaded', 'date_modified', 'date_published']

    def owner(self, obj):
        owner = obj.user
        url = reverse('admin:auth_user_change', args=(owner.pk,))
        name = owner.get_full_name() or owner.username
        link = '<a href="{}">{}</a>'.format(url, name)
        return link
    owner.short_description = 'Owner'
    owner.allow_tags = True

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
