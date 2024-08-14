# Scrabbly

Scrabbly is a simple Python script that helps you find words from the Official Scrabble Players Dictionary (OSPD) that match a given pattern of letters and spaces.

## Project Structure
- `notes/`: Contains a link to the OSPD word list.
- [`ospd.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fsully%2FDevelopment%2Fsullivan%2Fscrabbly%2Fospd.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/sully/Development/sullivan/scrabbly/ospd.txt"): The Official Scrabble Players Dictionary word list.
- [`scrabbly.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fsully%2FDevelopment%2Fsullivan%2Fscrabbly%2Fscrabbly.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/sully/Development/sullivan/scrabbly/scrabbly.py"): The main script that processes the word list and finds matching words.

## Usage

To run the script, use the following command:

```sh
python scrabbly.py <letters> <pattern>
```
* `<letters>`: A string of letters you have.
* `<pattern>`: A string representing the pattern of letters and spaces (_ for spaces).

## Output
The script will print the matching words and the total number of matches.

### Example Output
```sh
Results:
hello
jolly
Total Matches: 2
```

## Notes
The word list used in this project is sourced from the Official Scrabble Players Dictionary (OSPD). For more information, visit OSPD Word List.