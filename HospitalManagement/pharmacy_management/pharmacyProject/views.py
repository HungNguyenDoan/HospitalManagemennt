from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MedicalSupply, Category
from .serializers import MedicalSupplySerializer, CategorySerializer

class MedicalSupplyCreateAPIView(APIView):
    def post(self, request):
        serializer = MedicalSupplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicalSupplyDetailAPIView(APIView):
    def get(self, request, id):
        try:
            medical_supply = MedicalSupply.objects.get(id=id)
        except MedicalSupply.DoesNotExist:
            return Response({"error": "Medical supply not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MedicalSupplySerializer(medical_supply)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MedicalSupplyUpdateAPIView(APIView):
    def put(self, request, id):
        try:
            medical_supply = MedicalSupply.objects.get(id=id)
        except MedicalSupply.DoesNotExist:
            return Response({"error": "Medical supply not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MedicalSupplySerializer(medical_supply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicalSupplyDeleteAPIView(APIView):
    def delete(self, request, id):
        try:
            medical_supply = MedicalSupply.objects.get(id=id)
        except MedicalSupply.DoesNotExist:
            return Response({"error": "Medical supply not found"}, status=status.HTTP_404_NOT_FOUND)
        medical_supply.delete()
        return Response({"message": "Medical supply deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class MedicalSupplyListByTypeAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        supplies = MedicalSupply.objects.all()
        supply_serializer = MedicalSupplySerializer(supplies, many=True)
        return Response({
            "categories": category_serializer.data,
            "medical_supplies": supply_serializer.data
        }, status=status.HTTP_200_OK)

class MedicalSupplySearchAPIView(APIView):
    def get(self, request):
        supply_type = request.GET.get('type')
        keywords = request.GET.get('keywords')

        if not supply_type or not keywords:
            return Response({"error": "Both type and keywords are required"}, status=status.HTTP_400_BAD_REQUEST)

        supplies = MedicalSupply.objects.filter(
            category__name__icontains=supply_type,
            name__icontains=keywords
        )
        serializer = MedicalSupplySerializer(supplies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
