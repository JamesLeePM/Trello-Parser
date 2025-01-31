import json
import pandas as pd
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description='Trello JSON parser')
    parser.add_argument('-i', '--input', required=True, help='Input JSON file')
    parser.add_argument('-o', '--output', default='trello_analysis.xlsx', help='Output file name')
    args = parser.parse_args()

    try:
        with open(args.input) as f:
            print(f"Reading file: {args.input}")
            data = json.load(f)
            
        # Debug prints
        print("\nData structure check:")
        print("Keys in data:", list(data.keys()))
        
        # Create mappings
        list_map = {lst['id']: lst['name'] for lst in data.get('lists', [])}
        member_map = {mbr['id']: mbr['fullName'] for mbr in data.get('members', [])}
        label_map = {label['id']: label['name'] for label in data.get('labels', [])}
        
        print("\nMappings created:")
        print(f"Lists found: {len(list_map)}")
        print(f"Members found: {len(member_map)}")
        print(f"Labels found: {len(label_map)}")
        
        # Parse cards
        cards = []
        for card in data.get('cards', []):
            try:
                # Get label info including colors
                label_info = []
                label_colors = []
                for lid in card.get('idLabels', []):
                    label = next((l for l in data.get('labels', []) if l['id'] == lid), None)
                    if label:
                        label_info.append(label.get('name', ''))
                        label_colors.append(label.get('color', ''))

                # Extract creation date from card ID
                card_id = card.get('id', '')
                created_timestamp = int(card_id[:8], 16)  # First 8 chars of ID are hex timestamp
                created_date = pd.to_datetime(created_timestamp, unit='s')

                cards.append({
                    'Title': card['name'],
                    'Labels': ', '.join(label_info),
                    'Label Colors': ', '.join(label_colors),
                    'Assigned To': ', '.join([member_map.get(mid, "Unknown") for mid in card.get('idMembers', [])]),
                    'Column': list_map.get(card.get('idList'), "Unknown"),
                    'Created': created_date,
                    'Last Updated': card.get('dateLastActivity', ''),
                    'Link': f"https://trello.com/c/{card.get('shortLink', '')}"
                })
            except Exception as e:
                print(f"Error processing card: {card.get('name', 'Unknown')}")
                print(f"Error details: {str(e)}")
                continue

        print("Number of cards processed:", len(cards))
        print("Saving to:", args.output)
        pd.DataFrame(cards).to_excel(args.output, index=False)
        print(f"Analysis saved to {args.output}")
    except Exception as e:
        print(f"Error reading file: {str(e)}")

if __name__ == "__main__":
    main()
