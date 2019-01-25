from django.contrib import admin

from .models import languagecont, example, usage, about, contact

admin.site.register(languagecont)
admin.site.register(example)
admin.site.register(usage)
admin.site.register(about)
admin.site.register(contact)

