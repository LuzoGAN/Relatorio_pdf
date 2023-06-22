from django.shortcuts import render
import io
from django.http import FileResponse
from django.views.generic import View
# Create your views here.

class IndexView(View):

    def get(self, request, *args, **kwargs):
        #Cria um arquivo para receber os dados e gerar o pdf
        buffer = io.BytesIO()

        #Cria o arquivo pdf
        pdf = canvas.Canvas(buffer)

        #Insere coisas no PDF
        pdf.drawString(100, 100, "Luzo Gomes")

        # Quando acabamos de inserri coisas no pdf
        pdf.showPage()
        pdf.save()

        # Por fim, retornamos o buffer para o inicio do arquivo
        buffer.seek(0)

        return FileResponse(buffer, as_attachement=True, filename='relatorio1.pdf')