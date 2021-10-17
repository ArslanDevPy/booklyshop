from django.contrib import admin
from shop.models import Book, Author, Category, OrderDetails, Order, Tag
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.utils import timezone


@admin.action(description='Change Status to Active')
def status_active(modeladmin, request, queryset):
    queryset.update(status=True, update_at=timezone.now())
    messages.success(request, "Status Change")


@admin.action(description='Change Status to Deactive')
def status_deactive(modeladmin, request, queryset):
    queryset.update(status=False, update_at=timezone.now())
    messages.success(request, "Status Change")


admin.site.register(Tag)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_image', 'status', 'create_at', 'update_at']
    search_fields = ['title']
    readonly_fields = ('create_at', 'update_at')
    actions = [status_active, status_deactive]
    list_filter = ['status']
    fieldsets = ((_("Author Information"), {'fields': ('title', 'description', 'img')}),
                 (_('Advanced options'), {
                     'classes': ('collapse',),
                     'fields': ('status', 'slug', 'create_at', 'update_at'),
                 }),)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.readonly_fields = ('slug', 'create_at', 'update_at')
        return super().change_view(request, object_id, form_url, extra_context)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'create_at', 'update_at']
    search_fields = ['title', 'category', 'author__title', 'ISBN', 'price', 'discount', 'noPage']
    radio_fields = {"category": admin.HORIZONTAL}
    actions = [status_active, status_deactive]
    readonly_fields = ('create_at', 'update_at')
    list_filter = ['status']
    fieldsets = (
        (_("Book Information"), {'fields': ('title', 'author', 'category', 'ISBN', 'description','tag')}),
        (_('Book Publish'), {'fields': ('year',)}),
        (_('Important Part'), {'fields': ('price', 'discount', 'noPage'), }),
        (_('Image'), {'fields': ('img',), }),
        (_('Advanced options'), {'classes': ('collapse',),
                                 'fields': ('status', 'slug', 'create_at', 'update_at'),
                                 }),
    )

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.readonly_fields = ('slug', 'create_at', 'update_at')
        return super().change_view(request, object_id, form_url, extra_context)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'create_at', 'update_at']
    search_fields = ['title']
    readonly_fields = ('create_at', 'update_at')
    actions = [status_active, status_deactive]
    list_filter = ['status']
    fieldsets = ((_("Category Information"), {'fields': ('title', 'description')}),
                 (_('Advanced options'), {
                     'classes': ('collapse',),
                     'fields': ('status', 'slug', 'create_at', 'update_at'),
                 }),)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.readonly_fields = ('slug', 'create_at', 'update_at')
        return super().change_view(request, object_id, form_url, extra_context)


@admin.register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ['book']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    radio_fields = {"status": admin.HORIZONTAL}
    list_filter = ['status']
    pass
