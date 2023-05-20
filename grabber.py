from telethon.sync import TelegramClient

# Isert your API credentials
api_id = 'insert your api id here'
api_hash = 'insert your api hash here'

def get_group_member_ids(invite_link):
    with TelegramClient('session_name', api_id, api_hash) as client:
        # Get the entity from the invite link
        entity = client.get_entity(invite_link)

        # Get the list of members in the group
        members = client.get_participants(entity)

        # Extract the user IDs from the member list
        member_ids = [str(member.id) for member in members]

        return member_ids

def save_ids_to_file(member_ids, filename):
    with open(filename, 'w') as file:
        file.write('\n'.join(member_ids))

def main():
    invite_link = 'insert your link here'  # Replace with your target group's link
    output_file = 'member_ids.txt'  # The file containing all the grabbed IDs

    member_ids = get_group_member_ids(invite_link)
    save_ids_to_file(member_ids, output_file)
    print(f"Member IDs saved to '{output_file}' file.")

if __name__ == '__main__':
    main()