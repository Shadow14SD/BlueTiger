import requests
from colorama import Fore

def brute_force_directories(url, wordlist_path):
    print(Fore.CYAN + f"\n*** Brute-forcing des répertoires pour {url} ***\n")
    try:
        with open(wordlist_path, 'r') as file:
            for line in file:
                directory = line.strip()
                full_url = f"{url}/{directory}"
                response = requests.get(full_url)
                if response.status_code == 200:
                    print(Fore.GREEN + f"Répertoire trouvé: {full_url}")
                else:
                    print(Fore.RED + f"Répertoire {full_url} non trouvé (Code: {response.status_code})")
    except FileNotFoundError:
        print(Fore.RED + f"Erreur: Wordlist non trouvée au chemin {wordlist_path}")
    except Exception as e:
        print(Fore.RED + f"Erreur inattendue: {e}")
