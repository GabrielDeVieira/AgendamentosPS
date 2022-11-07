from django.forms import ModelForm
from Agendamento.models import TbLocal, TbHorarios, TbBairros, TbEstados,TbCidades, TbAgendamentosmes



class TbEstadosForm(ModelForm):
    class Meta:
        model = TbEstados
        fields = ["est_codigo", "est_estado",]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['est_estado'].widget.attrs.update(  {'class': 'form-control'})
        
class TbCidadesForm(ModelForm):
    class Meta:
        model = TbCidades
        fields = ["cid_codigo", "cid_cidade", "cid_est_codigo"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['cid_cidade'].widget.attrs.update(  {'class': 'form-control'})
        self.fields['cid_est_codigo'].widget.attrs.update(  {'class': 'form-control'})
        
class TbBairrosForm(ModelForm):
    class Meta:
        model = TbBairros
        fields = ["bai_codigo", "bai_bairro", "bai_cid_codigo"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['bai_bairro'].widget.attrs.update(  {'class': 'form-control'})
        self.fields['bai_cid_codigo'].widget.attrs.update(  {'class': 'form-control'})
        
class TbLocalForm(ModelForm):
    class Meta:
        model = TbLocal
        fields = ["loc_codigo", "loc_logradouro", "loc_numero", "loc_nomeunidadedeservico","loc_bai_codigo"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['loc_logradouro'].widget.attrs.update(  {'class': 'form-control'})
        self.fields['loc_numero'].widget.attrs.update(  {'class': 'form-control'})
        self.fields['loc_nomeunidadedeservico'].widget.attrs.update(  {'class': 'form-control'})
        self.fields['loc_bai_codigo'].widget.attrs.update(  {'class': 'form-control'})
class TbAgendamentosmesForm(ModelForm):
    class Meta:
        model = TbAgendamentosmes
        fields = ["agm_codigo", "agm_data"]      
        
        
class TbHorariosForm(ModelForm):
    class Meta:
        model = TbHorarios
        fields = ["hor_codigo", "hor_agm_codigo" ,"hor_horarioentrada", "hor_horariosaida", "hor_loc_codigo"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['hor_agm_codigo'].widget.attrs.update(  {'class': 'form-control'})
        self.fields['hor_horarioentrada'].widget.attrs.update(  {'class': 'form-control'})
        self.fields['hor_horariosaida'].widget.attrs.update(  {'class': 'form-control'})
        self.fields['hor_loc_codigo'].widget.attrs.update(  {'class': 'form-control'})
        

        
        
        



