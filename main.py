import os
import platform
import requests
from requests.exceptions import RequestException, ProxyError, ConnectTimeout

def clear_screen():
    
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def check_proxy(proxy_line):
    try:
        ip, port, username, password = proxy_line.strip().split(':')
    except ValueError:
        print("❌ Invalid proxy format. Please use: ip:port:username:password")
        return

    proxy_auth = f"{username}:{password}@{ip}:{port}"
    protocols = {
        "HTTP": f"http://{proxy_auth}",
        "HTTPS": f"http://{proxy_auth}",
        "SOCKS4": f"socks4://{proxy_auth}",
        "SOCKS5": f"socks5://{proxy_auth}",
    }

    print(f"🔍 Checking proxy {ip}:{port}...\n")

    for name, proxy_url in protocols.items():
        proxies = {
            "http": proxy_url,
            "https": proxy_url,
        }

        try:
            response = requests.get("https://www.google.com", proxies=proxies, timeout=5)
            if response.status_code == 200:
                print(f"✅ Proxy works using {name} protocol!")
                return
        except (RequestException, ProxyError, ConnectTimeout):
            continue

    print("❌ Proxy does not work with any supported protocol.")


if __name__ == "__main__":
    clear_screen()
    proxy_input = input("📝 Enter your proxy in format ip:port:username:password:\n> ")
    check_proxy(proxy_input)
