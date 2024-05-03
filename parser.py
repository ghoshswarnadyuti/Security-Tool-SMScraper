from bs4 import BeautifulSoup

def parse_profile(html_content):
    """Parses HTML and extracts basic profile information."""
    soup = BeautifulSoup(html_content, 'html.parser')

    profile_data = {}

    # Placeholder: Extract elements based on the specific social media platform
    profile_data['name'] = soup.find('title').text  # Example
    profile_data['bio'] = soup.find('meta', attrs={'name': 'description'})['content']  # Example

    return profile_data