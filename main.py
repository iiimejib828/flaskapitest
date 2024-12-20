from flask import Flask, render_template
import requests

app = Flask(__name__)

# Function to fetch 5 random quotes from ZenQuotes API
def fetch_random_quotes():
    url = "https://zenquotes.io/api/random"
    quotes = []
    try:
        for _ in range(5):
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP request errors
            data = response.json()
            # Extract quote and author
            if data and isinstance(data, list):
                quote = data[0].get("q", "No quote found")
                author = data[0].get("a", "Unknown")
                quotes.append(f"{quote} - {author}")
            else:
                quotes.append("Unable to fetch quote at the moment.")
        return quotes
    except requests.RequestException as e:
        return [f"Error fetching quote: {str(e)}"]

@app.route('/')
def home():
    quotes = fetch_random_quotes()
    return render_template("index.html", quotes=quotes)

if __name__ == "__main__":
    app.run(debug=True)
