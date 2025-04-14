import json
import urllib.parse


def json_to_url_json(json_data):
    """
    Convert a Python dictionary (JSON) to a URL-encoded JSON string.

    Args:
        json_data (dict): The JSON data as a Python dictionary.

    Returns:
        str: URL-encoded JSON string.
    """
    # Convert dict to JSON string
    json_string = json.dumps(json_data)

    # URL encode the JSON string
    url_encoded_json = urllib.parse.quote(json_string)

    return url_encoded_json


if __name__ == "__main__":
    # Example JSON data
    sample_json = {
        "transactions": [
            {
                "amount": "-9.99",
                "title": "Ride H2O",
                "category": "Travel",
                "subcategory": "Lyft",
                "date": "2025-04-10",
            },
            {
                "amount": "-10.99",
                "title": "Ride O2H",
                "category": "Travel",
                "subcategory": "Lyft",
                "date": "2025-04-10",
            },
        ]
    }

    encoded = json_to_url_json(sample_json)
    print("URL-encoded JSON:")
    print(encoded)
