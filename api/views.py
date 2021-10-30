from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from django.conf import settings
from api.QRCodeGenerator import generateQRCode


class QRCodeGeneratorAPIView(APIView):

    def post(self, request, format=None):
        try:
            data = request.data
            if 'text' in data:
                text = data['text']
                if 'size' in data:
                    size = data['size']
                else:
                    size = 200
                code_url = generateQRCode(settings.BASE_DIR, text, size)
                return Response({'code_url': 'media/'+code_url}, status=HTTP_200_OK)
            else:
                return Response({'error': 'text is required'}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)