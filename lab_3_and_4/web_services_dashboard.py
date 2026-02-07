#!/usr/bin/env python3
"""
Multi-Service Dashboard - Client Application for Public Web Services
Combines multiple free APIs with a clean GUI interface
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import requests
import json
import threading
from datetime import datetime
import webbrowser

class MultiServiceDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 Multi-Service Dashboard")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f0f0")
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Create main interface
        self.create_widgets()
        
    def create_widgets(self):
        """Create the main GUI interface"""
        # Main title
        title_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        title_frame.pack(fill="x", padx=10, pady=10)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="🌟 Multi-Service Dashboard", 
                              font=("Arial", 20, "bold"), fg="white", bg="#2c3e50")
        title_label.pack(pady=20)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Create tabs
        self.create_weather_tab()
        self.create_quotes_tab()
        self.create_facts_tab()
        self.create_jokes_tab()
        self.create_crypto_tab()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(self.root, textvariable=self.status_var, 
                             relief="sunken", anchor="w", bg="#ecf0f1")
        status_bar.pack(side="bottom", fill="x")
    
    def create_weather_tab(self):
        """Weather service tab using wttr.in"""
        weather_frame = ttk.Frame(self.notebook)
        self.notebook.add(weather_frame, text="🌤️ Weather")
        
        # Input section
        input_frame = tk.Frame(weather_frame, bg="white", relief="raised", bd=2)
        input_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(input_frame, text="City:", font=("Arial", 12, "bold"), bg="white").pack(side="left", padx=10, pady=10)
        
        self.weather_city_var = tk.StringVar(value="London")
        city_entry = tk.Entry(input_frame, textvariable=self.weather_city_var, font=("Arial", 12), width=20)
        city_entry.pack(side="left", padx=5, pady=10)
        
        weather_btn = tk.Button(input_frame, text="🌤️ Get Weather", command=self.get_weather,
                               bg="#3498db", fg="white", font=("Arial", 10, "bold"), relief="flat")
        weather_btn.pack(side="left", padx=10, pady=10)
        
        # Results section
        self.weather_text = scrolledtext.ScrolledText(weather_frame, height=20, font=("Courier", 11))
        self.weather_text.pack(fill="both", expand=True, padx=10, pady=5)
        
    def create_quotes_tab(self):
        """Inspirational quotes tab using quotegarden.io"""
        quotes_frame = ttk.Frame(self.notebook)
        self.notebook.add(quotes_frame, text="💭 Quotes")
        
        # Controls
        controls_frame = tk.Frame(quotes_frame, bg="white", relief="raised", bd=2)
        controls_frame.pack(fill="x", padx=10, pady=10)
        
        quote_btn = tk.Button(controls_frame, text="✨ Get Inspiring Quote", command=self.get_quote,
                             bg="#e74c3c", fg="white", font=("Arial", 12, "bold"), relief="flat")
        quote_btn.pack(pady=15)
        
        # Quote display
        self.quote_text = scrolledtext.ScrolledText(quotes_frame, height=15, font=("Georgia", 12), wrap="word")
        self.quote_text.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Get initial quote
        self.get_quote()
    
    def create_facts_tab(self):
        """Random facts tab using uselessfacts.jsph.pl"""
        facts_frame = ttk.Frame(self.notebook)
        self.notebook.add(facts_frame, text="🧠 Facts")
        
        # Controls
        controls_frame = tk.Frame(facts_frame, bg="white", relief="raised", bd=2)
        controls_frame.pack(fill="x", padx=10, pady=10)
        
        fact_btn = tk.Button(controls_frame, text="🎲 Get Random Fact", command=self.get_fact,
                            bg="#27ae60", fg="white", font=("Arial", 12, "bold"), relief="flat")
        fact_btn.pack(pady=15)
        
        # Fact display
        self.fact_text = scrolledtext.ScrolledText(facts_frame, height=15, font=("Arial", 12), wrap="word")
        self.fact_text.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Get initial fact
        self.get_fact()
    
    def create_jokes_tab(self):
        """Programming jokes tab using official-joke-api"""
        jokes_frame = ttk.Frame(self.notebook)
        self.notebook.add(jokes_frame, text="😂 Jokes")
        
        # Controls
        controls_frame = tk.Frame(jokes_frame, bg="white", relief="raised", bd=2)
        controls_frame.pack(fill="x", padx=10, pady=10)
        
        joke_btn = tk.Button(controls_frame, text="😄 Get Programming Joke", command=self.get_joke,
                            bg="#f39c12", fg="white", font=("Arial", 12, "bold"), relief="flat")
        joke_btn.pack(pady=15)
        
        # Joke display
        self.joke_text = scrolledtext.ScrolledText(jokes_frame, height=15, font=("Arial", 12), wrap="word")
        self.joke_text.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Get initial joke
        self.get_joke()
    
    def create_crypto_tab(self):
        """Cryptocurrency prices tab using coinapi.io free tier"""
        crypto_frame = ttk.Frame(self.notebook)
        self.notebook.add(crypto_frame, text="💰 Crypto")
        
        # Controls
        controls_frame = tk.Frame(crypto_frame, bg="white", relief="raised", bd=2)
        controls_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(controls_frame, text="Cryptocurrency:", font=("Arial", 12, "bold"), bg="white").pack(side="left", padx=10, pady=10)
        
        self.crypto_var = tk.StringVar(value="bitcoin")
        crypto_combo = ttk.Combobox(controls_frame, textvariable=self.crypto_var, 
                                   values=["bitcoin", "ethereum", "dogecoin", "litecoin", "ripple"], 
                                   font=("Arial", 11), width=15)
        crypto_combo.pack(side="left", padx=5, pady=10)
        
        crypto_btn = tk.Button(controls_frame, text="💰 Get Price", command=self.get_crypto_price,
                              bg="#9b59b6", fg="white", font=("Arial", 10, "bold"), relief="flat")
        crypto_btn.pack(side="left", padx=10, pady=10)
        
        # Crypto display
        self.crypto_text = scrolledtext.ScrolledText(crypto_frame, height=20, font=("Courier", 11))
        self.crypto_text.pack(fill="both", expand=True, padx=10, pady=5)
    
    def get_weather(self):
        """Get weather information using wttr.in"""
        def fetch_weather():
            try:
                self.status_var.set("Fetching weather data...")
                city = self.weather_city_var.get().strip()
                
                if not city:
                    self.weather_text.delete(1.0, tk.END)
                    self.weather_text.insert(tk.END, "❌ Please enter a city name")
                    return
                
                # Get detailed weather info
                url = f"https://wttr.in/{city}?format=4"
                response = requests.get(url, timeout=10)
                
                self.weather_text.delete(1.0, tk.END)
                
                if response.status_code == 200:
                    weather_info = response.text.strip()
                    
                    # Also get more detailed info
                    url_detailed = f"https://wttr.in/{city}?T"
                    response_detailed = requests.get(url_detailed, timeout=10)
                    
                    result = f"🌤️ Weather for {city.title()}\n"
                    result += "=" * 40 + "\n\n"
                    result += f"📊 Quick Info: {weather_info}\n\n"
                    
                    if response_detailed.status_code == 200:
                        result += "📋 Detailed Forecast:\n"
                        result += "-" * 30 + "\n"
                        result += response_detailed.text
                    
                    result += f"\n\n🕒 Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                    
                    self.weather_text.insert(tk.END, result)
                else:
                    self.weather_text.insert(tk.END, f"❌ Could not fetch weather for '{city}'\nPlease check the city name and try again.")
                
                self.status_var.set("Weather data loaded")
                
            except Exception as e:
                self.weather_text.delete(1.0, tk.END)
                self.weather_text.insert(tk.END, f"❌ Error fetching weather: {str(e)}")
                self.status_var.set("Error fetching weather")
        
        # Run in background thread
        thread = threading.Thread(target=fetch_weather)
        thread.daemon = True
        thread.start()
    
    def get_quote(self):
        """Get inspirational quote using quotable.io"""
        def fetch_quote():
            try:
                self.status_var.set("Fetching inspirational quote...")
                
                url = "https://api.quotable.io/random?minLength=50"
                response = requests.get(url, timeout=10)
                
                self.quote_text.delete(1.0, tk.END)
                
                if response.status_code == 200:
                    data = response.json()
                    quote = data.get('content', 'No quote found')
                    author = data.get('author', 'Unknown')
                    
                    result = "✨ Inspirational Quote ✨\n"
                    result += "=" * 50 + "\n\n"
                    result += f'"{quote}"\n\n'
                    result += f"— {author}\n\n"
                    result += f"🕒 Retrieved: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                    
                    self.quote_text.insert(tk.END, result)
                else:
                    self.quote_text.insert(tk.END, "❌ Could not fetch quote. Please try again.")
                
                self.status_var.set("Quote loaded")
                
            except Exception as e:
                self.quote_text.delete(1.0, tk.END)
                self.quote_text.insert(tk.END, f"❌ Error fetching quote: {str(e)}")
                self.status_var.set("Error fetching quote")
        
        thread = threading.Thread(target=fetch_quote)
        thread.daemon = True
        thread.start()
    
    def get_fact(self):
        """Get random fact using uselessfacts.jsph.pl"""
        def fetch_fact():
            try:
                self.status_var.set("Fetching random fact...")
                
                url = "https://uselessfacts.jsph.pl/random.json?language=en"
                response = requests.get(url, timeout=10)
                
                self.fact_text.delete(1.0, tk.END)
                
                if response.status_code == 200:
                    data = response.json()
                    fact = data.get('text', 'No fact found')
                    
                    result = "🧠 Random Fact 🧠\n"
                    result += "=" * 40 + "\n\n"
                    result += fact + "\n\n"
                    result += f"🕒 Retrieved: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                    
                    self.fact_text.insert(tk.END, result)
                else:
                    self.fact_text.insert(tk.END, "❌ Could not fetch fact. Please try again.")
                
                self.status_var.set("Fact loaded")
                
            except Exception as e:
                self.fact_text.delete(1.0, tk.END)
                self.fact_text.insert(tk.END, f"❌ Error fetching fact: {str(e)}")
                self.status_var.set("Error fetching fact")
        
        thread = threading.Thread(target=fetch_fact)
        thread.daemon = True
        thread.start()
    
    def get_joke(self):
        """Get programming joke using official-joke-api"""
        def fetch_joke():
            try:
                self.status_var.set("Fetching programming joke...")
                
                url = "https://official-joke-api.appspot.com/jokes/programming/random"
                response = requests.get(url, timeout=10)
                
                self.joke_text.delete(1.0, tk.END)
                
                if response.status_code == 200:
                    data = response.json()
                    if data:
                        joke_data = data[0] if isinstance(data, list) else data
                        setup = joke_data.get('setup', 'No setup found')
                        punchline = joke_data.get('punchline', 'No punchline found')
                        
                        result = "😂 Programming Joke 😂\n"
                        result += "=" * 40 + "\n\n"
                        result += f"{setup}\n\n"
                        result += f"💥 {punchline}\n\n"
                        result += f"🕒 Retrieved: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                        
                        self.joke_text.insert(tk.END, result)
                    else:
                        self.joke_text.insert(tk.END, "❌ No joke data found.")
                else:
                    self.joke_text.insert(tk.END, "❌ Could not fetch joke. Please try again.")
                
                self.status_var.set("Joke loaded")
                
            except Exception as e:
                self.joke_text.delete(1.0, tk.END)
                self.joke_text.insert(tk.END, f"❌ Error fetching joke: {str(e)}")
                self.status_var.set("Error fetching joke")
        
        thread = threading.Thread(target=fetch_joke)
        thread.daemon = True
        thread.start()
    
    def get_crypto_price(self):
        """Get cryptocurrency price using coingecko API"""
        def fetch_crypto():
            try:
                self.status_var.set("Fetching crypto prices...")
                
                crypto = self.crypto_var.get().lower()
                url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd,eur&include_24hr_change=true&include_market_cap=true"
                
                response = requests.get(url, timeout=10)
                
                self.crypto_text.delete(1.0, tk.END)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    if crypto in data:
                        crypto_data = data[crypto]
                        
                        result = f"💰 {crypto.title()} Price Information\n"
                        result += "=" * 50 + "\n\n"
                        
                        if 'usd' in crypto_data:
                            result += f"💵 Price (USD): ${crypto_data['usd']:,.2f}\n"
                        
                        if 'eur' in crypto_data:
                            result += f"💶 Price (EUR): €{crypto_data['eur']:,.2f}\n"
                        
                        if 'usd_24h_change' in crypto_data:
                            change = crypto_data['usd_24h_change']
                            emoji = "📈" if change > 0 else "📉"
                            result += f"\n{emoji} 24h Change: {change:.2f}%\n"
                        
                        if 'usd_market_cap' in crypto_data:
                            result += f"📊 Market Cap: ${crypto_data['usd_market_cap']:,}\n"
                        
                        result += f"\n🕒 Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                        result += "\n\n💡 Data provided by CoinGecko"
                        
                        self.crypto_text.insert(tk.END, result)
                    else:
                        self.crypto_text.insert(tk.END, f"❌ No data found for {crypto}")
                else:
                    self.crypto_text.insert(tk.END, "❌ Could not fetch crypto data. Please try again.")
                
                self.status_var.set("Crypto data loaded")
                
            except Exception as e:
                self.crypto_text.delete(1.0, tk.END)
                self.crypto_text.insert(tk.END, f"❌ Error fetching crypto data: {str(e)}")
                self.status_var.set("Error fetching crypto data")
        
        thread = threading.Thread(target=fetch_crypto)
        thread.daemon = True
        thread.start()

def main():
    """Main application entry point"""
    root = tk.Tk()
    app = MultiServiceDashboard(root)
    
    # Center the window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()

if __name__ == "__main__":
    main()
