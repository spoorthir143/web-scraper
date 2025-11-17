import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    url = "https://www.bbc.com/news"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print("Failed to fetch webpage.")
            return

        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.find_all("h2")

        with open("headlines.txt", "w", encoding="utf-8") as file:
            for h in headlines:
                text = h.get_text(strip=True)
                if text:
                    file.write(text + "\n")

        print("Headlines saved to headlines.txt")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    scrape_headlines()
