import aiohttp
import chainlit as cl

# Base URL for FastAPI
BASE_URL = "http://localhost:8080"


@cl.on_message
async def main(message: cl.Message):
    # メッセージ内容を取得
    content = message.content

    if content.startswith("create "):
        # Create a new item
        try:
            _, name, description = content.split(" ", 2)
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{BASE_URL}/items/", json={"name": name, "description": description}
                ) as response:
                    response.raise_for_status()
                    item = await response.json()
                    await cl.Message(
                        content=(
                            f"Item created! ID: {item['id']}, Name: {item['name']}, "
                            f"Description: {item['description']}"
                        )
                    ).send()
        except Exception as e:
            await cl.Message(content=f"Error creating item: {e}").send()

    elif content.startswith("get "):
        # Retrieve an item by ID
        try:
            _, item_id = content.split(" ", 1)
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{BASE_URL}/items/{item_id}") as response:
                    response.raise_for_status()
                    item = await response.json()
                    await cl.Message(
                        content=f"Item retrieved! ID: {item['id']}, Name: {item['name']}, Description: {item['description']}"
                    ).send()
        except Exception as e:
            await cl.Message(content=f"Error retrieving item: {e}").send()

    else:
        await cl.Message(content="Invalid command. Use 'create <name> <description>' or 'get <id>'.").send()
