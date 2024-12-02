from django.shortcuts import render, redirect
from django.http import HttpResponse
from Gestion.models import alumnos, maestros, administrativos
from django.conf import settings
from django.core.mail import send_mail

def search_person(request):
    return render(request, "buscar_persona.html")

def buscar_todos(request):
    query = request.GET.get('nombre', '')  
    resultados_alumnos = []
    resultados_administrativos = []
    resultados_maestros = []

    if query:
        resultados_alumnos = alumnos.objects.filter(nombre__icontains=query)
        resultados_administrativos = administrativos.objects.filter(nombre__icontains=query)
        resultados_maestros = maestros.objects.filter(nombre__icontains=query)

    return render(
        request,
        'buscar_persona.html',
        {
            'query': query,
            'resultados_alumnos': resultados_alumnos,
            'resultados_administrativos': resultados_administrativos,
            'resultados_maestros': resultados_maestros,
        }
    )

def registro_personas(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        area = request.POST.get("area")

        if area == "alumnos":
            carrera = request.POST.get("carrera")
            cuatrimestre = request.POST.get("cuatrimestre")
            telefono = request.POST.get("telefono_alumno")
            alumnos.objects.create(nombre=nombre, carrera=carrera, cuatrimestre=cuatrimestre, telefono=telefono)

        elif area == "administrativos":
            departamento = request.POST.get("departamento")
            telefono = request.POST.get("telefono_admin")
            administrativos.objects.create(nombre=nombre, departamento=departamento, telefono=telefono)

        elif area == "maestros":
            materia = request.POST.get("materia")
            telefono = request.POST.get("telefono_maestro")
            maestros.objects.create(nombre=nombre, materia=materia, telefono=telefono)

        return redirect("registro_personas")

    return render(request, "registro_personas.html")

def enviar_correo(request):
    if request.method == "POST":
        destinatario = request.POST.get("destinatario")
        asunto = request.POST.get("asunto")
        mensaje = request.POST.get("mensaje")
        remitente = settings.EMAIL_HOST_USER

        try:
            send_mail(asunto, mensaje, remitente, [destinatario])
            return HttpResponse("Correo enviado exitosamente.")
        except Exception as e:
            return HttpResponse(f"Error al enviar el correo: {str(e)}")
    return render(request, "enviar_correos.html")
