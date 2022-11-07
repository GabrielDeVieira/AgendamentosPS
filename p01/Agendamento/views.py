from django.shortcuts import HttpResponse, render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.mixins import LoginRequiredMixin
from Agendamento.models import TbAgendamentosmes, TbLocal, TbHorarios, TbBairros, TbEstados,TbCidades
from Agendamento.form import TbAgendamentosmesForm, TbEstadosForm, TbCidadesForm, TbBairrosForm, TbLocalForm, TbHorariosForm




def cadastro(request):
    if request.method =="GET":
        return render(request, 'pages-sign-up.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user1 = User.objects.filter(username=username).first()
        if user1:
            return HttpResponse("Ja existe um usuário com esse nome")
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()    
        return HttpResponse("Cadastrado")

def login(request):
    if request.method =="GET":
        return render(request, 'pages-sign-in.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            return redirect("/inicio")
        else:
            return HttpResponse("Usuário ou senha invalidos")
        
def inicio(request):
    if request.user.is_authenticated:
        return render(request,'Menu.html')
    else:
        return HttpResponse("É preciso estar logado")

def usesof (request):
    if request.user.is_authenticated:
        return render(request,'pages-profile.html')
    else:
        return HttpResponse("É preciso estar logado")   
     
def agendamentos(request):
    if request.user.is_authenticated:
        return render(request,'agendamentos.html')
    else:
        return HttpResponse("É preciso estar logado")
    
def agendamentosdia (request):
    
    if request.user.is_authenticated:
        return render(request,'agendadia.html')
    else:
        return HttpResponse("É preciso estar logado")
    
def localdetrabalho(request):
    if request.user.is_authenticated:
        return render(request,'localdetrabalho.html')
    else:
        return HttpResponse("É preciso estar logado")

#Visualçização tabelas

def viTbLocal(request):
    infor = TbLocal.objects.all()
    bair = TbBairros.objects.all()
    cida = TbCidades.objects.all()
    estados = TbEstados.objects.all()
    parametros = {"locais": infor,
                  "bairros": bair,
                  "cidades": cida,
                  "estados": estados
                  }
    return render(request, "localdetrabalho.html", parametros)

def viTbAgendamentos(request):
    agendamentos = TbAgendamentosmes.objects.all()
    parametros = {"agendamentosmes": agendamentos,
                  }
    return render(request, "agendamentos.html", parametros)

def viTbAgendamentosdia(request, id):
    age = TbAgendamentosmes.objects.get(pk=id)
    data = age.agm_data
    
    if  age :
        agendamentos = TbHorarios.objects.all().filter(hor_agm_codigo = id)
        
        parametros = { "agendamentosdia": agendamentos,
                      "data": data
                        
                        }
    return render(request, "agendadia.html", parametros)

#CREATE     
def createTbEstados(request):
    formTbEstados = TbEstadosForm(request.POST or None)
    if formTbEstados.is_valid() :
        formTbEstados.save()
        return redirect("/localdetrabalho")    

    pacote = {"formTbEstados": formTbEstados}
    return render(request, "Create/createTbEstados.html", pacote)

def createTbCidades(request):
    formTbCidades = TbCidadesForm(request.POST or None)
    if formTbCidades.is_valid() :
        formTbCidades.save()
        return redirect("/localdetrabalho")    

    pacote = {"formTbCidades": formTbCidades}
    return render(request, "Create/createTbCidades.html", pacote)

def createTbBairros(request):
    formTbBairros = TbBairrosForm(request.POST or None)
    if formTbBairros.is_valid() :
        formTbBairros.save()
        return redirect("/localdetrabalho")    

    pacote = {"formTbBairros": formTbBairros}
    return render(request, "Create/createTbBairros.html", pacote)

def createTbLocal(request):
    formTbLocal = TbLocalForm(request.POST or None)
    if formTbLocal.is_valid() :
        formTbLocal.save()
        return redirect("/localdetrabalho")    

    pacote = {"formTbLocal": formTbLocal}
    return render(request, "Create/createTbLocal.html", pacote)

def createTbHorarios(request):
    formTbHorarios = TbHorariosForm(request.POST or None)
    if formTbHorarios.is_valid() :
        formTbHorarios.save()
        return redirect("/agendamentos")    

    pacote = {"formTbHorarios": formTbHorarios}
    return render(request, "Create/createTbHorarios.html", pacote)



def createTbAgendamentosmes(request):
    formTbAgendamentos = TbAgendamentosmesForm(request.POST or None)
    if formTbAgendamentos.is_valid() :
        formTbAgendamentos.save()
        return redirect("/agendamentos")    

    pacote = {"formTbAgendamentosmes": formTbAgendamentos}
    return render(request, "Create/createTbAgendamentosmes.html", pacote)


#UPDATE

def updateTbEstados(request, id):
    est = TbEstados.objects.get(pk=id)
    formTbEstados = TbEstadosForm(request.POST or None, instance=est)
    if formTbEstados.is_valid() :
        formTbEstados.save()
        return redirect("/localdetrabalho")    

    pacote = {"formTbEstados": formTbEstados}
    return render(request, "Create/createTbEstados.html", pacote)


def updateTbCidades(request, id):
    cid = TbCidades.objects.get(pk=id)
    formTbCidades = TbCidadesForm(request.POST or None, instance=cid)
    if formTbCidades.is_valid() :
        formTbCidades.save()
        return redirect("/localdetrabalho")    

    pacote = {"formTbCidades": formTbCidades}
    return render(request, "Create/createTbCidades.html", pacote)

def updateTbBairros(request, id):
    bai = TbBairros.objects.get(pk=id)
    formTbBairros = TbBairrosForm(request.POST or None, instance=bai)
    if formTbBairros.is_valid() :
        formTbBairros.save()
        return redirect("/localdetrabalho")    

    pacote = {"formTbBairros": formTbBairros}
    return render(request, "Create/createTbBairros.html", pacote)

def updateTbLocal(request, id):
    loc = TbLocal.objects.get(pk=id)
    formTbLocal = TbLocalForm(request.POST or None, instance=loc)
    if formTbLocal.is_valid() :
        formTbLocal.save()
        return redirect("/localdetrabalho")    

    pacote = {"formTbLocal": formTbLocal}
    return render(request, "Create/createTbLocal.html", pacote)

def updateTbHorarios(request, id):
    hor = TbHorarios.objects.get(pk=id)
    formTbHorarios = TbHorariosForm(request.POST or None, instance=hor)
    if formTbHorarios.is_valid() :
        formTbHorarios.save()
        return redirect("")    

    pacote = {"formTbHorarios": formTbHorarios}
    return render(request, "Create/createTbHorarios.html", pacote)



def updateTbAgendamentosmes(request, id):
    age = TbAgendamentosmes.objects.get(pk=id)
    formTbAgendamentos = TbAgendamentosmesForm(request.POST or None, instance=age)
    if formTbAgendamentos.is_valid() :
        formTbAgendamentos.save()
        return redirect("/agendamentos")    

    pacote = {"formTbAgendamentosmes": formTbAgendamentos}
    return render(request, "Create/createTbAgendamentosmes.html", pacote)

# DELETE

def deleteTbCidades(request, id):
    cid = TbCidades.objects.get(pk=id)
    cid.delete()
    return redirect("/localdetrabalho")

def deleteTbEstados(request, id):
    est = TbEstados.objects.get(pk=id)
    est.delete()
    return redirect("/localdetrabalho") 

def deleteTbBairros(request, id):
    est = TbBairros.objects.get(pk=id)
    est.delete()
    return redirect("/localdetrabalho")  

def deleteTbLocal(request, id):
    est = TbLocal.objects.get(pk=id)
    est.delete()
    return redirect("/localdetrabalho")   
 
def deleteTbHorarios(request, id):
    est = TbHorarios.objects.get(pk=id)
    est.delete()
    return redirect("/agendamentos")

 
def deleteTbAgendamentosmes(request, id):
    est = TbAgendamentosmes.objects.get(pk=id)
    est.delete()
    return redirect("/agendamentos")  
# Create your views here.
