from rest_framework.views import APIView
from rest_framework.response import Response

from drfx.phthisis.test_app.tasks import heartbeat


class TestAPIView(APIView):
    def get(self, request):
        heartbeat.delay()
        return Response(status=200)
