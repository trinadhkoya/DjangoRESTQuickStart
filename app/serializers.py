from rest_framework import serializers
from .models import Stock


class StockSerializer(serializers.ModelSerializer):
    # with the modelserializer ,we are sending json Object

    class Meta:
        model = Stock
        fields = ('ticker', 'open', 'close', 'volume')
        # i heart coded the all the data which is to be passed as a JSON object.But you can do with the below too
        # fields='__all__'
