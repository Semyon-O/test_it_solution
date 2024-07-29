from rest_framework import viewsets, generics

from ads_api.models import Ads
from ads_api.serializers import AdSerializer


class AdView(generics.RetrieveAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdSerializer