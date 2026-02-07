#!/usr/bin/env python3
"""
Simple Web Services Client - Command Line Version
Clean and simple interface for multiple free public APIs
"""

import requests
import json
from datetime import datetime
import random

class SimpleWebServicesClient:
    def __init__(self):
        self.services = {
            "1": ("🌤️ Weather", self.get_weather),
            "2": ("💭 Quote", self.get_quote), 
            "3": ("🧠 Random Fact", self.get_fact),
            "4": ("😂 Programming Joke", self.get_joke),
            "5": ("💰 Crypto Price", self.get_crypto),
            "6": ("🎲 All Services Demo", self.demo_all),
            "0": ("🚪 Exit", self.exit_app)
        }
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("🌟 Simple Web Services Client")
        print("="*50)
        
        for key, (name, _) in self.services.items():
            print(f"  {key}. {name}")
        
        print("="*50)
    
    def get_weather(self):
        """Get weather using wttr.in API"""
        print("\n🌤️ Weather Service")
        print("-" * 30)
        
        city = input("Enter city name: ").strip()
        if not city:
            print("❌ Please enter a valid city name")
            return
        
        try:
            print("🔄 Fetching weather data...")
            
            # Get simple weather info
            url = f"https://wttr.in/{city}?format=3"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                weather = response.text.strip()
                print(f"\n✅ Weather in {city.title()}:")
                print(f"   {weather}")
                
                # Get more details
                url_detail = f"https://wttr.in/{city}?format=4"
                detail_response = requests.get(url_detail, timeout=10)
                
                if detail_response.status_code == 200:
                    print(f"   {detail_response.text.strip()}")
                
            else:
                print(f"❌ Could not get weather for '{city}'")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def get_quote(self):
        """Get inspirational quote"""
        print("\n💭 Inspirational Quote")
        print("-" * 30)
        
        try:
            print("🔄 Fetching quote...")
            
            url = "https://api.quotable.io/random?minLength=30"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                quote = data.get('content', 'No quote found')
                author = data.get('author', 'Unknown')
                
                print(f'\n✨ "{quote}"')
                print(f"   — {author}")
            else:
                print("❌ Could not fetch quote")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def get_fact(self):
        """Get random fact"""
        print("\n🧠 Random Fact")
        print("-" * 30)
        
        try:
            print("🔄 Fetching random fact...")
            
            url = "https://uselessfacts.jsph.pl/random.json?language=en"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                fact = data.get('text', 'No fact found')
                print(f"\n🎯 {fact}")
            else:
                print("❌ Could not fetch fact")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def get_joke(self):
        """Get programming joke"""
        print("\n😂 Programming Joke")
        print("-" * 30)
        
        try:
            print("🔄 Fetching joke...")
            
            url = "https://official-joke-api.appspot.com/jokes/programming/random"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data:
                    joke = data[0] if isinstance(data, list) else data
                    setup = joke.get('setup', 'No setup')
                    punchline = joke.get('punchline', 'No punchline')
                    
                    print(f"\n🎭 {setup}")
                    print(f"💥 {punchline}")
            else:
                print("❌ Could not fetch joke")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def get_crypto(self):
        """Get cryptocurrency price"""
        print("\n💰 Cryptocurrency Prices")
        print("-" * 30)
        
        cryptos = ["bitcoin", "ethereum", "dogecoin", "litecoin", "ripple"]
        print("Available cryptocurrencies:")
        for i, crypto in enumerate(cryptos, 1):
            print(f"  {i}. {crypto.title()}")
        
        try:
            choice = input("\nEnter number (1-5) or cryptocurrency name: ").strip().lower()
            
            if choice.isdigit() and 1 <= int(choice) <= 5:
                crypto = cryptos[int(choice) - 1]
            elif choice in cryptos:
                crypto = choice
            else:
                crypto = choice if choice else "bitcoin"
            
            print(f"🔄 Fetching {crypto} price...")
            
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd&include_24hr_change=true"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if crypto in data:
                    price_data = data[crypto]
                    price = price_data.get('usd', 0)
                    change = price_data.get('usd_24h_change', 0)
                    
                    change_emoji = "📈" if change > 0 else "📉"
                    print(f"\n💰 {crypto.title()}: ${price:,.2f}")
                    print(f"{change_emoji} 24h Change: {change:.2f}%")
                else:
                    print(f"❌ No data found for '{crypto}'")
            else:
                print("❌ Could not fetch crypto data")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def demo_all(self):
        """Demonstrate all services"""
        print("\n🎲 All Services Demo")
        print("=" * 30)
        
        # Weather for a random city
        cities = ["London", "Tokyo", "New York", "Paris", "Sydney"]
        city = random.choice(cities)
        
        try:
            print(f"\n1. 🌤️ Weather in {city}:")
            url = f"https://wttr.in/{city}?format=3"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"   {response.text.strip()}")
            
            print(f"\n2. 💭 Random Quote:")
            url = "https://api.quotable.io/random?maxLength=100"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                print(f'   "{data.get("content", "No quote")}" — {data.get("author", "Unknown")}')
            
            print(f"\n3. 🧠 Random Fact:")
            url = "https://uselessfacts.jsph.pl/random.json?language=en"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                fact = data.get('text', 'No fact')[:100] + "..." if len(data.get('text', '')) > 100 else data.get('text', 'No fact')
                print(f"   {fact}")
            
            print(f"\n4. 💰 Bitcoin Price:")
            url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if 'bitcoin' in data:
                    price = data['bitcoin'].get('usd', 0)
                    change = data['bitcoin'].get('usd_24h_change', 0)
                    emoji = "📈" if change > 0 else "📉"
                    print(f"   ${price:,.2f} ({emoji} {change:.2f}%)")
            
            print(f"\n✅ Demo completed!")
            
        except Exception as e:
            print(f"❌ Demo error: {e}")
    
    def exit_app(self):
        """Exit the application"""
        print("\n👋 Thanks for using the Web Services Client!")
        return False
    
    def run(self):
        """Main application loop"""
        print("🚀 Starting Web Services Client...")
        
        while True:
            self.display_menu()
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice in self.services:
                service_name, service_func = self.services[choice]
                
                if service_func() is False:  # Exit condition
                    break
                    
                input("\n⏎ Press Enter to continue...")
            else:
                print("❌ Invalid choice. Please try again.")

def main():
    """Main entry point"""
    client = SimpleWebServicesClient()
    client.run()

if __name__ == "__main__":
    main()
