project made by @TheLastOxygen
educative purposes only.
DISCLAIMER: The grabber will only work if the authenticated phone number is a member of the target group.
 _________   _______    ___        _______    ________   ________   ________   _________   
|\___   ___\|\  ___ \  |\  \      |\  ___ \  |\   ____\ |\   __  \ |\   ____\ |\___   ___\ 
\|___ \  \_|\ \   __/| \ \  \     \ \   __/| \ \  \___| \ \  \|\  \\ \  \___|_\|___ \  \_| 
     \ \  \  \ \  \_|/__\ \  \     \ \  \_|/__\ \  \     \ \   __  \\ \_____  \    \ \  \  
      \ \  \  \ \  \_|\ \\ \  \____ \ \  \_|\ \\ \  \____ \ \  \ \  \\|____|\  \    \ \  \ 
       \ \__\  \ \_______\\ \_______\\ \_______\\ \_______\\ \__\ \__\ ____\_\  \    \ \__\
        \|__|   \|_______| \|_______| \|_______| \|_______| \|__|\|__||\_________\    \|__|
                       ⣀⣤⣴⣾⣿⣿⣿⡄                                     \|_________|
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⡿⠿⠛⢙⣿⣿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣾⣿⣿⠿⠛⠋⠁⠀⠀⠀⣸⣿⣿⠀
⠀⠀⠀⠀⣀⣤⣴⣾⣿⣿⡿⠟⠛⠉⠀⠀⣠⣤⠞⠁⠀⠀⣿⣿⡇⠀
⠀⣴⣾⣿⣿⡿⠿⠛⠉⠀⠀⠀⢀⣠⣶⣿⠟⠁⠀⠀⠀⢸⣿⣿⠀⠀
⠸⣿⣿⣿⣧⣄⣀⠀⠀⣀⣴⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⣼⣿⡿⠀⠀
⠀⠈⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⡇⠀⣀⣄⡀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣠⣾⣿⣿⣿⣦⡀⠀⠀⣿⣿⡏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⡿⠋⠈⠻⣿⣿⣦⣸⣿⣿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⠀⠀⠀⠀⠈⠻⣿⣿⣿⠏⠀⠀⠀⠀


 _,  ,_  _     __  __   _,,_   
 / _  |_)'|\   '|_)'|_) /_,|_)  
'\_|`'| \ |-\  _|_)_|_)'\_'| \  
  _|  '  `'  `'   '       `'  ` .py
 '      

1. Install Python: Make sure you have Python installed on your computer. You can download the latest version of Python from the official Python website and follow the installation instructions for your operating system.
2. Install Telethon: Open a command prompt or terminal and run the following command to install the Telethon library:
   pip install telethon
3. Obtain Telegram API credentials: To use the Telegram API, you need to obtain API credentials. Follow these steps:

Visit the Telegram website (https://my.telegram.org/auth) and log in to your Telegram account.
Under the "API development tools" section, create a new application.
Fill in the required details, such as the application name and platform.
Once created, you will receive an API ID and API hash. Make a note of these credentials.
Obtain the group invite link: In order to retrieve the member IDs of a Telegram group, you need the invite link of the group. This link allows the script to access the group information.

4.Update the script with your credentials and input: Open a text editor and copy the "grabber" code into a new file. Replace the api_id and api_hash variables with the credentials obtained in step 3. Also, replace the invite_link variable with the actual invite link of the group you want to grab member IDs from.
5. Save the script: Save the file with a descriptive name, such as grabber.py, in a location of your choice.
6. Run the script: Open a command prompt or terminal, navigate to the directory where you saved the script, and run the following command:
    python grabber.py
7. Wait for the script to finish: The script will connect to the Telegram API, retrieve the member IDs, and save them to the specified output file. Wait for the script to complete its execution. Once finished, you will see a message indicating the successful saving of the member IDs.
8. Access the member IDs: After the script finishes running, you can open the specified output file (e.g., member_ids.txt) using a text editor to access the retrieved member IDs. Each ID will be on a separate line.

Remember to use the "grabber" code responsibly and in compliance with Telegram's terms of service and any applicable regulations.


  _,  _,,  ,  ,_   _,,_   
 (_, /_,|\ |  | \,/_,|_)  
  _)'\_ |'\| _|_/'\_'| \  
 '     `'  `'       `'  ` .py

1. Update the sender code with your credentials and input: Open a text editor and copy the "sender" code into a new file. Replace the api_id and api_hash variables with the credentials obtained in step 3. Additionally, update the phone_number variable with your Telegram account's phone number.
2. Prepare the contact IDs: Use the grabber generated text file (e.g., contact_ids.txt) and enter the Telegram IDs of the contacts you want to send messages to, each ID on a separate line. Ensure that you have the appropriate permissions to send messages to these contacts.
3. Save the script: Save the file with a descriptive name, such as sender.py, in a location of your choice.
4. Run the script: Open a command prompt or terminal, navigate to the directory where you saved the script, and run the following command:
    python sender.py
5. Wait for the script to finish: The script will connect to the Telegram API, send the specified message to the contacts listed in the contact_ids.txt file, and display a confirmation message for each successful message sent. Wait for the script to complete its execution.

Remember to use the "sender" code responsibly and in compliance with Telegram's terms of service and any applicable regulations.



Privacy and Security Notice:
Telethon, the library used in this code, may request your Telegram API credentials and phone number for authentication purposes. Please note that the author of this repository and the Telethon library itself do not have access to your credentials or any other personal data.
The credentials you provide, including the API ID, API hash, and phone number, are used solely for the purpose of authenticating your access to the Telegram API. These credentials are securely stored on your local machine and are not transmitted or shared with any external parties.
We prioritize the privacy and security of our users. We strongly recommend that you exercise caution and avoid sharing your API credentials and phone number with anyone, including third-party applications or services.
If you have any concerns or questions regarding the privacy and security practices associated with this code or the Telethon library, please don't hesitate to reach out to the author or refer to the official documentation of Telethon for further information.
Remember to review and comply with the terms of service and privacy policy of Telegram when using their services or interacting with their API.

Disclaimer: The creator of this code explicitly disclaims any responsibility for misuse or illegal activities conducted using this code. 
The code is provided for educational and illustrative purposes only, focusing on API manipulation. Users are solely responsible for their actions and are advised to comply with relevant laws and regulations.
