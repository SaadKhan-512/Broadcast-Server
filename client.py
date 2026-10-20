import asyncio
from websockets.asyncio.client import connect
from websockets.exceptions import ConnectionClosed


async def main():
    try:
        async with connect("ws://localhost:8765") as websocket:
            while True:
                message = input("You: ")

                reply = await websocket.recv()

                print("Server Received:", reply)

                await websocket.send(message)



    except ConnectionClosed:
        print("\nConnection closed by the server.")

    except OSError as error:
        print(f"\nCould not connect or the connection failed: {error}")

asyncio.run(main())