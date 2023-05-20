from telethon.sync import TelegramClient, utils
from telethon.tl.types import InputPeerUser
import time

# Telegram API credentials
api_id = 'insert your api id here'
api_hash = 'insert your api hash here'
phone_number = 'insert your phone number here (with prefix)'

def send_message(phone_number, message, contact_ids):
    client = TelegramClient('session_name', api_id, api_hash)
    client.start(phone_number)

    for contact_id in contact_ids:
        entity = InputPeerUser(int(contact_id), 0)  # User entity creation
        client.send_message(entity, message)  # Message sending
        print("Message sent to:", contact_id)
        time.sleep(1)  # Add 1 second delay

    client.disconnect()

def main():
    message = 'Hello, world!' # Insert your personalized message here
    with open('member_ids.txt', 'r') as file: #Change the name of the .txt file based on the file that you want to read
        contact_ids = [line.strip() for line in file]

    send_message(phone_number, message, contact_ids)

if __name__ == '__main__':
    main()
