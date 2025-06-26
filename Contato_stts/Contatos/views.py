from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contato
from .serializers import ContatoSerializer

class ContatoAPIView(APIView):
    # LISTAR TODOS OS CONTATOS (GET)
    def get(self, request):
        contatos = Contato.objects.all()
        serializer = ContatoSerializer(contatos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # CRIAR UM NOVO CONTATO (POST)
    def post(self, request):
        serializer = ContatoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContatoDetalheAPIView(APIView):
    # BUSCAR UM CONTATO ESPECÍFICO (GET)
    def get(self, request, pk):
        try:
            contato = Contato.objects.get(id=pk)
            serializer = ContatoSerializer(contato)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Contato.DoesNotExist:
            return Response(
                {"erro": "Contato não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

    # ATUALIZAR CONTATO (PUT)
    def put(self, request, pk):
        try:
            contato = Contato.objects.get(id=pk)
            serializer = ContatoSerializer(contato, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Contato.DoesNotExist:
            return Response(
                {"erro": "Contato não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

    # DELETAR CONTATO (DELETE)
    def delete(self, request, pk):
        try:
            contato = Contato.objects.get(id=pk)
            contato.delete()
            return Response(
                {"mensagem": "Contato excluído com sucesso"},
                status=status.HTTP_204_NO_CONTENT
            )
        except Contato.DoesNotExist:
            return Response(
                {"erro": "Contato não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )