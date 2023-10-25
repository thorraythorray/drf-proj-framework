from rest_framework.views import APIView
from rest_framework.response import Response

from drfx.phthisis.test_app.tasks import heartbeat
from drfx.log import logger
from workers.celeryconfig import CeleryQueue


class TestAPIView(APIView):
    def get(self, request):
        logger.info("123")
        heartbeat.apply_async(queue='traffic', args=(1, {"a":2}))
        logger.info("456")
        return Response(status=200)
