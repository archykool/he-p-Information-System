from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.http import JsonResponse

from ..models import chat_msgs
from .serializers import ChatMsgSerializer


class ListChats(APIView):
    """
    View to list all users in the system.
    """

    def get(self, request, format=None, group_id=None):
        """
        Return a list of all chats by a chat group
        """
        queryset = chat_msgs.objects.filter(group_id=group_id)
        queryset = queryset.order_by('-created_at')
        queryset = queryset.select_related('user', 'group')
        queryset = queryset[:50]

        serializer = ChatMsgSerializer(queryset, many=True)

        return JsonResponse(serializer.data[::-1], safe=False)
