from poe_api_wrapper import AsyncPoeApi
import asyncio
import json

tokens = {

}

async def main():
    client = await AsyncPoeApi(tokens=tokens).create()
    
    # Read the original JSON file
    with open('data/downstream_application_code_block.json', 'r') as file:
        data = json.load(file)

    # Create a new list to store processed items
    processed_data = []
    
    i=0
    # Process each item in the data
    for item in data['data']:

        if item['dependency'] == 'torch':
            # i+=1
            # if i>=2:
            #     break
            input_text = f"description:{item['description']},masked_code:{item['masked_code']}"
            print(f"Processing input: {input_text[:100]}...") # Print first 100 chars of input
            response_seq = []
            full_response = ""
            async for chunk in client.send_message(bot="programmerllama3", message=input_text):
                response_seq.append(chunk["response"])

                print(f"len:{str(len(response_seq))} response:{chunk['response']}", end='', flush=False) # Print a dot for each chunk received
            print("\nResponse received.")

            full_response = response_seq[-2]
            # Create a new item with the original data and the response
            processed_item = {
                "input": input_text,
                "output": full_response
            }
            processed_data.append(processed_item)

    # Write the output data to a new JSON file
    with open('poe_api_output.json', 'w') as outfile:
        json.dump(processed_data, outfile, indent=2)

    print("\nAll responses have been processed and saved to 'poe_api_output.json'")

asyncio.run(main())