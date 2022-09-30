from channels.consumer import AsyncConsumer,SyncConsumer
from channels.exceptions import StopConsumer
import time
import json

#Real time data sending and receiving example with front end means browser
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('This is websocket connected!!!')
        print("Checking in events: ",event)
        self.send({
            "type":'websocket.accept'
        })
    
    # def websocket_receive(self,event):
    #     print('Message Received from client!!!')
    #     print("Checking in events: \n",event['text'])
    #     for i in range(20):
    #         self.send({
    #         "type":'websocket.send',
    #         "text":str(i),
    #         })
    #         time.sleep(1)

    def websocket_receive(self,event):
        print('Message Received from client!!!')
        print("Checking in events: \n",event['text'])
        for i in range(20):
            self.send({
            "type":'websocket.send',
            "text":json.dumps({'count':i}),
            })
            time.sleep(1)


    def websocket_disconnect(self,event):
        print('WebSocket disconnected!!!')
        raise StopConsumer()
    
#asyncConsumer
import asyncio
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('This is websocket connected!!!')
        print("Checking in events: ",event)
        await self.send({
            "type":'websocket.accept'
        })
    
    async def websocket_receive(self,event):
        print('Message Received from client!!!')
        print("Checking in events: \n",event['text'])
        for i in range(10):
            await self.send({
            "type":'websocket.send',
            "text":str(i),
            })
            await asyncio.sleep(1)
    
    async def websocket_disconnect(self,event):
        print('WebSocket disconnected!!!')
        raise StopConsumer()
    


