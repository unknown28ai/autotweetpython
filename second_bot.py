import requests
import time

# Function to send a message to the second Botpress chat API
def send_message_to_second_bot(text, conversation_id="1"):
    url = "https://chat.botpress.cloud/5e9a433b-423a-454a-aa6f-a9b190523c5d/messages"  # Replace with your actual second bot's URL
    
    payload = {
        "payload": {
            "type": "text",
            "text": text
        },
        "conversationId": conversation_id
    }
    
    headers = {
        "accept": "application/json",
        "x-user-key": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjIiLCJpYXQiOjE3MzA1MzgyMzZ9.1_SMonz48yX61GEdRJvbywbmBV3hF7s2LLgD2FRhhSs"  # Replace with your actual user key for the second bot
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("Message sent to second bot successfully!")
    else:
        print("Failed to send message to second bot:", response.text)

# Function to retrieve messages from the second Botpress chat API
def get_messages_from_second_bot(conversation_id="1"):
    url = f"https://chat.botpress.cloud/5e9a433b-423a-454a-aa6f-a9b190523c5d/conversations/{conversation_id}/messages"  # Replace with your actual second bot's URL
    
    headers = {
        "accept": "application/json",
        "x-user-key": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjIiLCJpYXQiOjE3MzA1MzgyMzZ9.1_SMonz48yX61GEdRJvbywbmBV3hF7s2LLgD2FRhhSs"  # Replace with your actual user key for the second bot
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        messages = response.json().get('messages', [])
        if messages:
            bot_response = messages[0]['payload']['text']
            print("Second bot's response:", bot_response)
            return bot_response
        else:
            print("No messages in the conversation.")
    else:
        print("Failed to retrieve messages from second bot:", response.text)

def main():
    # Read the response from the first bot's temporary file
    try:
        with open("first_bot_response.txt", "r") as f:
            first_bot_response = f.read().strip()
            print("Response received from first bot:", first_bot_response)
            time.sleep(2)  # Delay before sending to the second bot
            
            # Send the first bot's response to the second bot
            send_message_to_second_bot(first_bot_response)
            time.sleep(5)  # Wait for the second bot to respond

            # Retrieve the response from the second bot
            second_bot_response = get_messages_from_second_bot()

            if second_bot_response:
                print("Final response from second bot:", second_bot_response)

    except FileNotFoundError:
        print("Response file not found. Please run the first bot script first.")

if __name__ == "__main__":
    main()