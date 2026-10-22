# Search Summary

A small Python command-line program that asks for a search term, displays a
simulated summary, and offers to open a Google search for that term in your
default web browser.

## Requirements

- Python 3
- A web browser, if you want to open Google results

The project uses only Python's standard library, so no extra packages need to
be installed.

## Run the program

Open a terminal in the project folder and run:

```powershell
python main.py
```

If you use PyCharm, you can also run `main.py` from the IDE.

## How to use it

1. Enter a search term when prompted.
2. The program displays a brief summary with three example results. These
   results are simulated; the program does not retrieve data from a search
   service.
3. After the summary, answer `y` to open a Google search for the term in your
   default browser. Google is asked to show five results per page. Any other
   answer skips opening the browser.

The program opens Google's results page but does not fetch or display the
actual Google results in the terminal.

## How the code is organized

The program is split into small functions, each responsible for one task:

- `show_welcome()` displays the welcome message.
- `get_search_term()` asks for the search term.
- `simulate_data_retrieval()` shows simulated progress and creates example
  results.
- `display_summary()` prints the summary and results.
- `ask_to_open_google()` asks whether to open a Google search.
- `main()` calls these functions in the correct order and handles empty input.

This separation makes each part easier to understand and reuse.
