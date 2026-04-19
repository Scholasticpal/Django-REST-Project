from rest_framework import generics
from .models import Asset
from .serializer import AssetSerializer


class AssetList(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
