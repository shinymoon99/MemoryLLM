from poe_api_wrapper import AsyncPoeApi
import asyncio
tokens = {
}

async def main():
    client = await AsyncPoeApi(tokens=tokens).create()
    message = "Explain quantum computing in simple terms"
    async for chunk in client.send_message(bot="gpt3_5", message=message):
        print(chunk["response"], end='', flush=False)
        
asyncio.run(main())