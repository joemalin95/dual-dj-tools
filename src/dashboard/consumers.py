# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'dj'
        self.room_group_name = 'dj'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        transitioning = text_data_json['transitioning']
        print(transitioning)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'transitioning': transitioning
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        transitioning = event['transitioning']

        print(transitioning)
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'transitioning': transitioning
        }))
