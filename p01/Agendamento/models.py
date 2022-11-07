from email.policy import default
from django.db import models

# Create your models here.


class TbEstados(models.Model):
    est_codigo = models.AutoField(primary_key=True)
    est_estado = models.CharField(unique=True, max_length=20)
    def __str__ (self):
         return self.est_estado
    
class TbCidades(models.Model):
    cid_codigo = models.AutoField(primary_key=True)
    cid_cidade = models.CharField(unique=True, max_length=50)
    cid_est_codigo = models.ForeignKey(TbEstados, on_delete=models.CASCADE )
    def __str__ (self):
         return self.cid_cidade
    
class TbBairros(models.Model):
    bai_codigo = models.AutoField(primary_key=True)
    bai_bairro = models.CharField(unique=True, max_length=50)
    bai_cid_codigo = models.ForeignKey(TbCidades, on_delete=models.CASCADE )
    def __str__ (self):
         return self.bai_bairro
    
class TbLocal(models.Model):
    loc_codigo = models.AutoField(primary_key=True)
    loc_logradouro = models.CharField( max_length=150)
    loc_numero = models.IntegerField()
    loc_nomeunidadedeservico = models.CharField(max_length=150)
    loc_bai_codigo = models.ForeignKey(TbBairros, on_delete=models.CASCADE )
    def __str__ (self):
         return self.loc_nomeunidadedeservico

class TbAgendamentosmes(models.Model):
    agm_codigo = models.AutoField(primary_key=True)
    agm_data= models.DateField()
    def __str__(self):
        return str(self.agm_data)
    
       
class TbHorarios(models.Model):
    hor_codigo = models.AutoField(primary_key=True)
    hor_agm_codigo = models.ForeignKey(TbAgendamentosmes, on_delete=models.CASCADE, blank=True, null=True  )
    hor_horariosaida = models.TimeField(default='')
    hor_horarioentrada = models.TimeField(default='')
    hor_loc_codigo = models.ForeignKey(TbLocal, on_delete=models.CASCADE,default='' )
    def __str__(self):
        return str(self.hor_horarioentrada)
    
    
   


    
    

    