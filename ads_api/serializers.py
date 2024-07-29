from rest_framework import serializers

from ads_api.models import Ads


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ('id', 'title', 'author', 'amount_of_watches', 'position')