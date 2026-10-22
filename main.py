import time
import webbrowser
from urllib.parse import urlencode


def show_welcome():
    """Display the program's welcome message."""
    print("Welcome to the Search Summary!")


def get_search_term():
    """Ask for a search term and return it without surrounding spaces."""
    return input("Enter a search term: ").strip()


def simulate_data_retrieval(search_term):
    """Show progress and return example results for the search term."""
    # Show progress and pause briefly to imitate a data retrieval process.
    print(f'\nSearching for "{search_term}"...')
    time.sleep(1)
    print("Retrieving data...")
    time.sleep(1)

    # These sample results are simulated; no external service is contacted.
    return [
        f"Overview of {search_term}",
        f"Recent updates about {search_term}",
        f"Related topics for {search_term}",
    ]


def display_summary(search_term, results):
    """Print the search term and each result in a readable summary."""
    # Display a summary and number each example result.
    print("\nSummary")
    print(f'Search term: "{search_term}"')
    print(f"Results found: {len(results)}")
    for number, result in enumerate(results, start=1):
        print(f"{number}. {result}")


def ask_to_open_google(search_term):
    """Ask whether to open a Google search, and open it if the user agrees."""
    # Ask whether the user wants to see Google results for the same search term.
    answer = input(
        f'\nWould you like me to google {search_term} for you? (y/n): '
    ).strip().lower()

    if answer != "y":
        return

    # Google displays results in the browser; this script does not fetch them.
    search_url = "https://www.google.com/search?" + urlencode(
        {"q": search_term, "num": 5}
    )
    print("Opening Google results in your browser...")
    if not webbrowser.open(search_url):
        print("Could not open a browser. Please try this search URL:")
        print(search_url)


def main():
    """Run the search summary program from start to finish."""
    show_welcome()
    search_term = get_search_term()

    # Stop early if the user only pressed Enter or entered spaces.
    if not search_term:
        print("Please enter a search term.")
        return

    results = simulate_data_retrieval(search_term)
    display_summary(search_term, results)
    ask_to_open_google(search_term)


# Run main() only when this file is started directly.
if __name__ == "__main__":
    main()
