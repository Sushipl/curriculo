from datetime import datetime
from django.shortcuts import render, redirect
from django.template import context
from django.http import HttpResponse
from .models import Avaliacao as Av
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import smtplib
import email.message
from .models import Avaliacao
import os
from dotenv import load_dotenv

@csrf_exempt
def cur(request):
    if request.method == "GET":
        av = Avaliacao.objects.filter(veri=True).all()
        return render(request, 'main.html', context={"av": av})
    if request.method == "POST":
        nome = request.POST.get('nome')
        img = request.POST.get('img')
        texto = request.POST.get('texto')
        reg = Av(nome=nome, texto=texto, img=img, agora=datetime.now())
        reg.save()
        enviar_email(texto)
        return redirect('/cur/')




def enviar_email(texto):  
    corpo_email = texto

    msg = email.message.Message()
    msg['Subject'] = "Verificação de Avaliação"
    msg['From'] = 'pedrobotter2016@gmail.com'
    msg['To'] = 'pedrobotter2016@gmail.com' 
    password = os.environ['EMAIL_HOST_PASSWORD']
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))