from rest_framework import viewsets
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle


from apps.snippets.models import Snippet
from apps.snippets.serializers import SnippetSerializer
from throttle import throttle


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    throttle_classes = [throttle.VisitThrottle]
    serializer_class = SnippetSerializer


@api_view(['GET'])
@throttle_classes([UserRateThrottle])
def example_view(request, format=None):
    content = {
        'status': 'request was permitted'
    }
    return Response(content)
