import requests
import sys
import re

def github(username=None):
    if username is None:
        username = sys.argv[1] if len(sys.argv) > 1 else input("Enter GitHub username: ")

    url = f"https://msii.xyz/api/github-kullanici-bilgi?username={username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if 'login' in data:
            print("Login:", data['login'])
            print("Name:", data['name'])
            print("Bio:", data['bio'] if data['bio'] else "No bio available")
            print("Public Repositories:", data['public_repos'])
            print("Followers:", data['followers'])
            print("Following:", data['following'])
        else:
            print("User not found!")
    else:
        print(f"API Error: {response.status_code}")

def steam(game_name=None):
    if game_name is None:
        game_name = sys.argv[1] if len(sys.argv) > 1 else input("Enter the game name: ")

    url = f"https://msii.xyz/api/steam-oyun-bilgi?oyunadi={game_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if 'ad' in data:
            print("Game Name:", data['ad'])
            print("Description:", data['açıklama'])
            print("Developers:", ", ".join(data['geliştiriciler']))
            print("Publishers:", ", ".join(data['yayıncılar']))
            print("Genres:", ", ".join(data['türler']))
            print("Release Date:", data['çıkış_tarihi'])
            print("Price:", data['fiyat'])
            print("Metacritic Score:", data['metacritic_puanı'])
            print("User Reviews Score:", data['kullanıcı_yorumları']['yorum_puanı'])
            print("Total Positive Reviews:", data['kullanıcı_yorumları']['toplam_olumlu'])
            print("Total Negative Reviews:", data['kullanıcı_yorumları']['toplam_olumsuz'])
            print("Total Reviews:", data['kullanıcı_yorumları']['toplam_yorum'])

            # Clean system requirements by removing HTML tags
            system_requirements = data['minimum_sistem_gereksinimleri']
            system_requirements_cleaned = re.sub(r'<[^>]*>', '', system_requirements)
            print("Minimum System Requirements:", system_requirements_cleaned)

            # Clean supported languages by removing HTML tags
            supported_languages = data['desteklenen_diller']
            supported_languages_cleaned = re.sub(r'<[^>]*>', '', supported_languages)
            print("Supported Languages:", supported_languages_cleaned)
        else:
            print("Game not found!")
    else:
        print(f"API Error: {response.status_code}")

def random_person():
    url = "https://msii.xyz/api/rastgele-kisi"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        person = data['results'][0]

        print("Name:", f"{person['name']['title']} {person['name']['first']} {person['name']['last']}")
        print("Gender:", person['gender'])
        print("Location:", f"{person['location']['street']['number']} {person['location']['street']['name']}, "
                           f"{person['location']['city']}, {person['location']['state']}, {person['location']['country']}, "
                           f"Postcode: {person['location']['postcode']}")
        print("Email:", person['email'])
        print("Username:", person['login']['username'])
        print("Date of Birth:", person['dob']['date'])
        print("Phone:", person['phone'])
        print("Cell:", person['cell'])
        print("Nationality:", person['nat'])
        print("Profile Picture:", person['picture']['large'])
    else:
        print(f"API Error: {response.status_code}")

def npm_info(package_name=None):
    if package_name is None:
        package_name = sys.argv[1] if len(sys.argv) > 1 else input("Enter the NPM package name: ")

    url = f"https://msii.xyz/api/npm-bilgi?paketadi={package_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("Package Name:", data['name'])
        print("Latest Version:", data['latestVersion'])
        print("Description:", data['description'])
        print("Repository:", data['repository'])
        print("License:", data['license'])
    else:
        print(f"API Error: {response.status_code}")

# Example usage:
# github("r00tww")
# steam("Half-Life")
# random_person()
# npm_info("msiapi")
