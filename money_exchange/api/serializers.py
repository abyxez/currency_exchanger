from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Currency
from .nums import CURRENCY_DICT
from .services import get_exchange_list_xrates


class RateSerializer(ModelSerializer):
    result = SerializerMethodField()

    class Meta:
        model = Currency
        fields = ("result",)
        read_only_fields = ("__all__",)

    def get_result(self, obj):
        request = self.context.get("request")
        curr_to_convert_code = request.query_params.get("from")
        curr_converted_code = request.query_params.get("to")
        if curr_converted_code == curr_converted_code:
            return 1
        value = request.query_params.get("value")

        rates_dict = dict(get_exchange_list_xrates(curr_to_convert_code, value)[1])
        if curr_converted_code:
            currency_value = CURRENCY_DICT[curr_converted_code]
            result = rates_dict[currency_value]
            return result

        return rates_dict
