import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed
connected_clients = set()

async def handle_client(websocket):
    connected_clients.add(websocket)
    print(f"Client connected! Total Clients: {len(connected_clients)}")

    try:
        async for message in websocket:
            print("Client says:", message)
            # await websocket.send(message)

            for client in connected_clients.copy():
                if client != websocket:
                    try:
                        await client.send(message)
                    except ConnectionClosed:
                        connected_clients.discard(client)

    finally:
        connected_clients.discard(websocket)
        print("Client Disconnected.")

async def main():
    async with serve(handle_client, "localhost", 8765):
        print("WebSocket server is running!")
        await asyncio.Future()

asyncio.run(main())