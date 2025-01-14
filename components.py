# components.py

def fetch_data(api_url):
    # Component A: Fetch data from API
    if not api_url.startswith("http"):
        raise ValueError("Invalid API URL")
    return {"data": [1, 2, 3]}  # Simulating API response

def process_data(data):
    # Component B: Process data
    if not isinstance(data, dict) or "data" not in data:
        raise ValueError("Invalid data format")
    return [x * 2 for x in data["data"]]

def display_data(processed_data):
    # Component C: Display data
    if not processed_data:
        return "No data to display"
    return f"Processed Data: {', '.join(map(str, processed_data))}"
