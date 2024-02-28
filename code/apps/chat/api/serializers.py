from rest_framework import serializers

from ..models import chat_msgs
#序列化聊天消息

class ChatMsgSerializer(serializers.ModelSerializer):
    text_msg = serializers.CharField(default=None)
    created_at = serializers.DateTimeField(format="%H:%M:%S %Y/%m/%d")
    #获取发布者姓名
    publisher = serializers.SerializerMethodField()
    #
    # def get_publisher(self,obj):
    #     return "{}".format(obj.user.username)
    # publisher_full_name = serializers.SerializerMethodField()
    #
    def get_publisher(self, obj):
        return "{} {}".format(obj.user.username, obj.user.nick_name)

    class Meta:
        model = chat_msgs
        fields = ('id', 'user_id', 'group_id', 'text_msg', 'created_at','publisher')
