import platform
import requests
import random
from colorama import Fore, Style, init
from bs4 import BeautifulSoup
import whois
from faker import Faker
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import time

init(autoreset=True)

fake = Faker()

print(Fore.RED + "DISCLAIMER: Tool is made for educational purposes ONLY. Creator of this tool doesnt take responsibility for what u doin.")
print(Fore.RED + "Dont do anything illegal or unethical." + Fore.LIGHTGREEN_EX)
time.sleep(4)

def google_dork_generator():
    print("\n[Google Dork Generator]")
    target = input("Enter target (email / domain / username): ").strip()

    dorks = [
        f'intext:"{target}"',
        f'site:{target}',
        f'intitle:"index of" "{target}"',
        f'inurl:"{target}"',
        f'filetype:pdf "{target}"',
        f'filetype:xls "{target}"',
        f'"{target}" ext:log',
        f'"{target}" ext:sql',
        f'"{target}" ext:xml',
        f'site:pastebin.com "{target}"',
        f'site:github.com "{target}"',
        f'site:stackoverflow.com "{target}"'
    ]

    print("\n[Generated Google Dorks]")
    for dork in dorks:
        print(f" - {dork}")

    save = input("\nSave dorks to file? (y/n): ").lower()
    if save == "y":
        with open("google_dorks.txt", "w") as f:
            for dork in dorks:
                f.write(dork + "\n")
        print("[Saved to 'google_dorks.txt']")


def phone_number_lookup():
    print("\n[Phone Number Lookup]")
    number = input("Enter phone number (with country code, e.g., +1): ").strip()

    try:
        parsed_number = phonenumbers.parse(number)

        if not phonenumbers.is_valid_number(parsed_number):
            print("Invalid phone number.")
            return

        location = geocoder.description_for_number(parsed_number, 'en')
        sim_carrier = carrier.name_for_number(parsed_number, 'en')
        timezones = timezone.time_zones_for_number(parsed_number)

        print(f"\nLocation: {location}")
        print(f"Carrier: {sim_carrier}")
        print(f"Timezones: {', '.join(timezones)}")
        print("Status: Valid number")
    except Exception as e:
        print(f"Error: {e}")


def whois_lookup(domain):
    try:
        w = whois.whois(domain)

        print(f"Information for domain: {domain}")
        print(f"Domain Name: {w.domain_name}")
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
        print(f"Name Servers: {w.name_servers}")
        print(f"Registrant Contact: {w.registrant_contact}")
        print(f"Administrative Contact: {w.admin_contact}")
        print(f"Technical Contact: {w.tech_contact}")
    except Exception as e:
        print(f"Error retrieving WHOIS data: {e}")

def check_pwned_email():
    email = input("Enter email to check:  ")

    search_url = f"https://haveibeenpwned.com/search?query={email}"

    response = requests.get(search_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        results = soup.find_all('a', class_='breach-link')
        if results:
            print(f"{email} has been found in the following breaches:\n")
            for result in results:
                breach_name = result.text.strip()
                breach_url = f"https://haveibeenpwned.com{result['href']}"
                print(f"Breached: {breach_name}")
                print(f"Details: {breach_url}\n")
        else:
            print(f"{email} has not been found in any breaches.")
    else:
        print(f"Error accessing Have I Been Pwned: Status code {response.status_code}")

def iplookup():
    lIP = input("IP to check: ")
    url = f"http://demo.ip-api.com/json/{lIP}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,isp,org,asname,query&lang=en"
    response = requests.get(url)
    data = response.json()

    if data.get("status") == "fail":
        print("Error: ", data.get("message", "unknown error"))
    else:
        print(f"IP Address     >  {data.get('query', 'N/A')}")
        print(f"Country code   >  {data.get('countryCode', 'N/A')}")
        print(f"Country        >  {data.get('country', 'N/A')}")
        print(f"Region Code    >  {data.get('region', 'N/A')}")
        print(f"Region name    >  {data.get('regionName', 'N/A')}")
        print(f"City           >  {data.get('city', 'N/A')}")
        print(f"Zip code       >  {data.get('zip', 'N/A')}")
        print(f"ISP            >  {data.get('isp', 'N/A')}")
        print(f"Organization   >  {data.get('org', 'N/A')}")
        print(f"ASN            >  {data.get('asname', 'N/A')}")
        print(f"Location       >  {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}")

def check_social_username(username):
    platforms = {
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Youtube": f"https://www.youtube.com/@{username}",
        "StackOverFlow": f"https://stackoverflow.com/users/{username}"
    }
    print(f"{Fore.CYAN}Checking username presence: {username} on social media platforms:\n")
    for platform, url in platforms.items():
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(f"{Fore.GREEN}[+] Found on {platform}: {url}")
            else:
                print(f"{Fore.RED}[-] Not found on {platform}")
        except requests.RequestException:
            print(f"{Fore.YELLOW}[!] Error while checking {platform}")

def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

def generate_random_user():
    user = {
        "Country: United States of America [USA]\n"
        "First Name": fake.first_name(),
        "Last Name": fake.last_name(),
        "Email": fake.email(),
        "Home City": fake.city(),
        "Country of Origin": fake.country(),
        "Job": fake.job(),
        "Birthdate": fake.date_of_birth(minimum_age=18, maximum_age=63).strftime('%Y-%m-%d'),
        "Company": fake.company(),
    }

    for key, value in user.items():
        print(f"{key}: {value}")

def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        if response.status_code == 200:
            country = data.get("country", "Unknown")
            city = data.get("city", "Unknown")
            org = data.get("org", "Unknown")
            return country, city, org
        else:
            return None
    except requests.RequestException:
        return None

print(Fore.LIGHTGREEN_EX + """
     ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
     ┃ [1] Username Lookup                                  ┃        ###       ###
     ┃ [2] IP Address Generator and Info Lookup             ┃       #####     #####
     ┃ [3] IP Lookup                                        ┃      #################
     ┃ [4] Check if mail was breached                       ┃       ###############
     ┃ [5] Whois                                            ┃        #############
     ┃ [6] USA Citizen generator                            ┃         ###########
     ┃ [7] Google Dork generator                            ┃          #########
     ┃ [8] Phone Number lookup                              ┃           #######
     ┃ [9] Exit                                             ┃            #####
     ┃ [10]Print this message                               ┃             ##
     ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")

while True:
    user_input = input(f""" {Fore.LIGHTGREEN_EX}
    ┏━━━━━━━━━━━━━━━━[{platform.system()}]━━━━━━━━━━━━[User]
    ┗━━►  """)

    if user_input == "1":
        username = input("Enter username: ")
        check_social_username(username)
    elif user_input == "2":
        ip = generate_random_ip()
        print(f"{Fore.CYAN}Generated IP: {ip}")
        country, city, org = get_ip_info(ip)
        if country:
            print(f"{Fore.GREEN}IP Info: Country: {country}, City: {city}, Organization: {org}")
        else:
            print(f"{Fore.RED}Error: Could not fetch IP information.")
    elif user_input == "3":
        iplookup()
    elif user_input == "4":
        check_pwned_email()
    elif user_input == "5":
        domain = input("Enter a domain to look up: ")
        whois_lookup(domain)
    elif user_input == "6":
        generate_random_user()
    elif user_input == "7":
        google_dork_generator()
    elif user_input == "8":
        phone_number_lookup()
    elif user_input == "10" or "help":
        print(Fore.LIGHTGREEN_EX + """
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃ [1] Username Lookup                                  ┃        ###       ###
             ┃ [2] IP Address Generator and Info Lookup             ┃       #####     #####
             ┃ [3] IP Lookup                                        ┃      #################
             ┃ [4] Check if mail was breached                       ┃       ###############
             ┃ [5] Whois                                            ┃        #############
             ┃ [6] USA Citizen generator                            ┃         ###########
             ┃ [7] Google Dork generator                            ┃          #########
             ┃ [8] Phone Number lookup                              ┃           #######
             ┃ [9] Exit                                             ┃            #####
             ┃ [10]Print this message                               ┃             ##
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
    elif user_input == "9" or "exit":
        print(f"{Fore.GREEN}Goodbye!")
        break
    else:
        print(f"{Fore.RED}Invalid option. Please try again.")
