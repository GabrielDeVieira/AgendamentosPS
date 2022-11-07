from django.contrib import admin
from .models import TbEstados, TbCidades, TbBairros, TbHorarios, TbLocal,  TbAgendamentosmes


admin.site.register(TbEstados)
admin.site.register(TbCidades)
admin.site.register(TbBairros)
admin.site.register(TbLocal)
admin.site.register(TbHorarios)

admin.site.register(TbAgendamentosmes)
# Register your models here.
