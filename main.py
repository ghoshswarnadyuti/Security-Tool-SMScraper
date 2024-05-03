import nltk
import web_scraper
import parser
import analyzer
import report_generator

def main():
    profile_url = input("Enter social media profile URL: ")
    html_content = web_scraper.fetch_profile_html(profile_url)

    if html_content:
        profile_data = parser.parse_profile(html_content)
        if profile_data['bio']:
            analyzed_words = analyzer.analyze_text(profile_data['bio'])
            print(f"Analyzed words from bio: {analyzed_words}")
        report_generator.generate_report(profile_data)

if __name__ == "__main__":
    main()
