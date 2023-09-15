from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Currency
from .serializers import RateSerializer


class RateViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RateSerializer

    def get_queryset(self):
        codes = []
        start_currency = self.request.query_params.get("from")
        codes.append(start_currency)
        queryset = self.queryset.filter(code__in=codes)
        return queryset

    def rates(self, request):
        serializer = self.serializer_class(
            data=self.get_queryset(), many=True, context={"request": request}
        )
        return Response(data=serializer.data)
