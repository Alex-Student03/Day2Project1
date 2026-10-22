import time
import webbrowser
from urllib.parse import urlencode


def main():
    # Greet the user and ask what they would like to search for.
    print("Welcome to the Search Summary!")
    search_term = input("Enter a search term: ").strip()

    # Stop early if the user only pressed Enter or entered spaces.
    if not search_term:
        print("Please enter a search term.")
        return

    # Show progress and pause briefly to imitate a data retrieval process.
    print(f'\nSearching for "{search_term}"...')
    time.sleep(1)
    print("Retrieving data...")
    time.sleep(1)

    # Create example results using the search term.
    # These are simulated; the script does not contact an external service.
    results = [
        f"Overview of {search_term}",
        f"Recent updates about {search_term}",
        f"Related topics for {search_term}",
    ]

    # Display a summary and number each example result.
    print("\nSummary")
    print(f'Search term: "{search_term}"')
    print(f"Results found: {len(results)}")
    for number, result in enumerate(results, start=1):
        print(f"{number}. {result}")

    # Ask whether the user wants to see Google results for the same search term.
    answer = input(
        f'\nWould you like me to google {search_term} for you? (y/n): '
    ).strip().lower()

    # Open Google's results page, requesting five results per page.
    # Google displays the results in the browser; this script does not fetch them.
    if answer == "y":
        search_url = "https://www.google.com/search?" + urlencode(
            {"q": search_term, "num": 5}
        )
        print("Opening Google results in your browser...")
        if not webbrowser.open(search_url):
            print("Could not open a browser. Please try this search URL:")
            print(search_url)


# Run main() only when this file is started directly.
if __name__ == "__main__":
    main()
