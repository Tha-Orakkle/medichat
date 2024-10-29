from annotated_types import doc
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import json


from . import doc_collection, model



class chatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        await self.accept()
        print("You are connected")


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )
        print("You are disconnected")


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print("DATA:", text_data_json)
        title, body = await self.search_document(text_data_json['message'])
        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'title': title,
                'message': body
            }
        )


    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'type': event['type'],
            'title': event['title'],
            'message': event['message']
         }))


    @sync_to_async
    def search_document(self, query):
        query_embedding = model.encode(query)

        result = doc_collection.query(
            query_embeddings=[query_embedding],
            n_results=1
        )
        result_data = result['metadatas'][0][0]
        return result_data['title'], result_data['body']
