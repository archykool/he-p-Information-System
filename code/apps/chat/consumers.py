import json
from channels.generic.websocket import AsyncWebsocketConsumer
from chat.models import chat_group,chat_msgs
from users.models import UserProfile

class ChatConsumer(AsyncWebsocketConsumer):
    # 连接到channels
    async def connect(self):
        # if self.user and not self.user.is_authenticated:
        #     return
        #获取当前用户
        self.user = self.scope['user']
        #获取当前聊天组名
        self.chat_group_name = self.scope['url_route']['kwargs']['chat_group_name']
        #获取能被channels处理的组名
        self.group_name = 'chat_{}'.format(self.chat_group_name)

        #指定加入到聊天的通道层
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        if self.user and not self.user.is_authenticated:
            return
        #断开连接
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        #接收文字聊天消息
        if self.user and not self.user.is_authenticated:
            return
        text_data_json = json.loads(text_data)
        text_msg = text_data_json['text_msg']

        #处理用户名
        nickname = "{} {}".format(self.user.username, self.user.nick_name)
        if nickname ==" ":
            nickname = "--"

        #异常处理
        try:
            #获取当前所在的聊天组
            chat = chat_group.objects.get(name=self.chat_group_name)

        except chat_group.DoesNotExist:
            return

        #文字消息存到数据库

        chat_msg_object = chat_msgs.objects.create(user_id=self.user.id, text_msg=text_msg, group_id=chat.id)
        #发送时间
        created_at = chat_msg_object.created_at.strftime('%H:%M:%S %Y/%m/%d')

        #channels向该组成员发送以下信息
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': "chat_msg",
                'text_msg': text_msg,
                'user_id': self.user.id,
                'publisher': nickname,
                'created_at': created_at,
            }
        )

    async def chat_msg(self,event):
        #向channels发送消息
        if self.user and not self.user.is_authenticated:
            return

        user_id = event['user_id']
        text_msg = event['text_msg']
        created_at = event['created_at']
        publisher = event['publisher']

        await  self.send(text_data=json.dumps({
            'user_id': user_id,
            'created_at': created_at,
            'text_msg': text_msg,
            'publisher':publisher,
        }))