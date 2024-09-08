import requests

def get_data(url):
    if url is None:
        return "Error: url can not be empty!"
    try:
        response = requests.get(url)
        if response is not None:
            with open('fixtures.py', 'w') as f:
                f.write(response.text)
                return "Data saved to fixtures.py :)"
    except requests.exceptions.RequestException as e:
        return f"Error occorred: {e}"
if __name__ == "__main__":
    url = "https://intranet-projects-files.s3.amazonaws.com/webstack/fixtures.py"
    print(get_data(url))
