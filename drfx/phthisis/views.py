from rest_framework.views import APIView
from rest_framework.response import Response

from drfx.phthisis.test_app.tasks import heartbeat
from drfx.log import logger


class Test2APIView(APIView):
    def get(self, request):
        print(1234567)
        logger.info("123")
        heartbeat.delay()
        logger.info("456")
        return Response(status=200)
