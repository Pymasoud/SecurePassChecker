import requests
import hashlib
import sys
from typing import List

def request_api_data(query_char: str) -> requests.Response:
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code} check the api and try again!")
    return res

def get_password_leaks_count(hashes: requests.Response, hash_to_check: str) -> int:
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return int(count)
    return 0

def pwned_api_check(password: str) -> int:
    # Check password if it exists in API response.
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5)
    return get_password_leaks_count(response, tail)

def check_password(password: str) -> str:
    count = pwned_api_check(password)
    if count:
        message = f"{password} was found {count} times.... you should probably change your password!"
    else:
        message = f"{password} was not found. Carry on!"
    return message

def main(args: List[str]) -> List[str]:
    results = []
    for password in args:
        result = check_password(password)
        results.append(result)
    return results

if __name__ == '__main__':
    if len(sys.argv) > 1:
        results = main(sys.argv[1:])
        for result in results:
            print(result)
    else:
        print("Please provide a password to check.")
