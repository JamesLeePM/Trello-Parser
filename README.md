# Trello Board Parser

A Python script to convert Trello board JSON exports into an Excel spreadsheet for easier analysis.

## Features

- Extracts card titles, labels, and label colors
- Shows card assignments (who's working on what)
- Includes card creation dates and last update times
- Preserves column (list) information
- Includes direct links to cards
- Exports everything to an easy-to-read Excel file

## Prerequisites

You need Python 3.x installed on your system along with the following packages:

```
bash
pip3 install pandas openpyxl
```

## How to Use

1. **Export Your Trello Board**
   - Open your Trello board
   - Click "Show Menu" (three dots) in the top right
   - Select "More"
   - Click "Print and Export"
   - Choose "Export as JSON"
   - Save the JSON file

2. **Run the Parser**
   ```bash
   python3 trello_parser.py -i your_board.json -o output.xlsx
   ```

   Arguments:
   - `-i` or `--input`: Your Trello JSON file (required)
   - `-o` or `--output`: Output Excel file name (optional, defaults to 'trello_analysis.xlsx')

## Output

The script creates an Excel file with the following columns:
- Title: Card name
- Labels: All labels assigned to the card
- Label Colors: Colors of the assigned labels
- Assigned To: Team members assigned to the card
- Column: Which list/column the card is in
- Created: When the card was created
- Last Updated: When the card was last modified
- Link: Direct URL to the card in Trello

## Troubleshooting

If you encounter any issues:
1. Make sure your JSON file is complete and not corrupted
2. Verify you have write permissions in the directory
3. Ensure all required Python packages are installed
4. Check that the JSON file is in the same directory as the script (or provide the full path)

## License

This tool is open-source and free to use.





