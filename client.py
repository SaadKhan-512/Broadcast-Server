import asyncio
from websockets.asyncio.client import connect
from websockets.exceptions import ConnectionClosed

# Function for receiving message
async def receive_messages(websocket):
    try:
        while True:
            message = await websocket.recv()
            print(f"Received: {message}\n")
    except ConnectionClosed:
        print("\nConnection to server closed.")

# Function for sending message
async def send_messages(websocket):
    while True:
        message = await asyncio.to_thread(input, "You: ")
        await websocket.send(message)

# Main Function
async def main():
    try:
        async with connect("ws://localhost:8765") as websocket:
            await asyncio.gather(
                send_messages(websocket),
                receive_messages(websocket)
            )

    except ConnectionClosed:
        print("\nConnection closed by the server.")

    except OSError as error:
        print(f"\nCould not connect or the connection failed: {error}")

asyncio.run(main())