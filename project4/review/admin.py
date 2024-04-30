from django.contrib import admin
from .models import Review

# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('__str__', 'user', 'review_date', 'is_reply')
#     list_filter = ('review_date', 'user')

#     def is_reply(self, obj):
#         return obj.parent is not None
#     is_reply.short_description = 'Is a Reply'

# admin.site.unregister(Review, ReviewAdmin)