from django.contrib import admin
# from .models import stock_model , chat
from .models import TutorialCategory ,TutorialSeries ,Tutorial
# Register your models here.



# class Admin(admin.ModelAdmin) :
#     # inlines = [Like_Admin]
#     list_display = ['__str__', 'user']
#     search_fields = ['content','user__username' , 'user__email']
#     class Meta :
#         model = chat

# admin.site.register(chat,Admin)
# admin.site.register(chat)


# admin.site.register(stock_model)

admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Tutorial)
