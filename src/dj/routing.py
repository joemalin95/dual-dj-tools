from channels.routing import ProtocolTypeRouter
from dashboard.routing import websockets
application = ProtocolTypeRouter({
    "websocket": websockets,
})
