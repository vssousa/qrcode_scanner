# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils import timezone
from .models import QRCode

def index(request):
    if request.method == "POST":
        return add(request)
    else:
        return render(request, 'scanner/qrcode.html')

def add(request):
    qrcodeMessage = request.POST['message']
    # result
    databaseMessage = None
    errorMessage = None

    try:
        qrcode = QRCode.objects.get(message=qrcodeMessage)
        errorMessage = "QR code '" + qrcodeMessage + "' already exists in our database."
    except QRCode.DoesNotExist:
        newCode = QRCode(message=qrcodeMessage, pub_date=timezone.now())
        newCode.save()
        databaseMessage = "QR code '" + qrcodeMessage + "' was saved in our database."

    return render(request, 'scanner/qrcode.html', {
        'database_message': databaseMessage,
        'error_message': errorMessage
    })