import requests


API_KEY = 'c1cbfef241c537b7afd21462'

def get_exchange_rate(base, target):
    try:
        
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base}"
        print(f"Requesting: {url}") 
        response = requests.get(url)
        print(f"Status code: {response.status_code}")  
        data = response.json()
        print(f"Response data keys: {data.keys()}")  

        if response.status_code == 200 and "conversion_rates" in data:
            rate = data["conversion_rates"].get(target.upper())  
            if rate:
                print(f"1 {base} = {rate:.2f} {target.upper()}")
            else:
                print(f"Target currency '{target.upper()}' not found in response.")
                print(f"Available currencies: {list(data['conversion_rates'].keys())[:10]}...")  
        else:
            print(f"Could not fetch exchange rates. Response: {data}")
    except Exception as e:
        print(f"Error fetching exchange rate: {e}")

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Weather in {city}: {response.text}")
        else:
            print("Could not fetch weather information.")
    except Exception as e:
        print(f"Error fetching weather: {e}")

if __name__ == "__main__":
    target = input("Enter the target currency: ")
    get_exchange_rate("EUR", target=target)
    city = input("What place would you like the weather for? ")
    get_weather(city)
