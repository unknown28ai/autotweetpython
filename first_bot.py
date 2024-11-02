import requests
import time

# Function to send a message to the first Botpress chat API
def send_message_to_first_bot(text, conversation_id="1"):
    url = "https://chat.botpress.cloud/6bc6d0fe-1e0a-44c3-8c7e-ac086179efee/messages"
    
    payload = {
        "payload": {
            "type": "text",
            "text": text
        },
        "conversationId": conversation_id
    }
    
    headers = {
        "accept": "application/json",
        "x-user-key": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjIiLCJpYXQiOjE3MzA1MzczODl9.EayLuZsw0aBdpyrb2c877DUsG7UeWpnMJCmTRt-s7Co",  # Replace with your actual user key
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("Message sent to first bot successfully!")
    else:
        print("Failed to send message to first bot:", response.text)

# Function to retrieve messages from the first Botpress chat API
def get_messages_from_first_bot(conversation_id="1"):
    url = f"https://chat.botpress.cloud/6bc6d0fe-1e0a-44c3-8c7e-ac086179efee/conversations/{conversation_id}/messages"
    
    headers = {
        "accept": "application/json",
        "x-user-key": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjIiLCJpYXQiOjE3MzA1MzczODl9.EayLuZsw0aBdpyrb2c877DUsG7UeWpnMJCmTRt-s7Co"  # Replace with your actual user key
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        messages = response.json().get('messages', [])
        if messages:
            bot_response = messages[0]['payload']['text']
            print("First bot's response:", bot_response)
            return bot_response
        else:
            print("No messages in the conversation.")
    else:
        print("Failed to retrieve messages from first bot:", response.text)

def main():
    first_bot_initial_message = "hey"
    send_message_to_first_bot(first_bot_initial_message)
    time.sleep(5)  # Wait for the first bot to respond

    first_bot_response = get_messages_from_first_bot()
    
    if first_bot_response:
        # Write the response to a temporary file for the second bot to read
        with open("first_bot_response.txt", "w") as f:
            f.write(first_bot_response)
        print("First bot's response written to file.")

if __name__ == "__main__":
    main()