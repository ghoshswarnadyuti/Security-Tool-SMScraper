import requests

def fetch_profile_html(url):
    """Fetches HTML content from the social media profile URL."""
    try:
        response = requests.get(url, headers={'User-Agent': 'Your Custom User Agent'})
        response.raise_for_status()  # Check for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching profile: {e}")
        return None