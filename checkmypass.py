import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code} check the api and try again!")
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    # Check password if it exists in API response.
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5)
    return get_password_leaks_count(response, tail)


def main(args):
    message = ""
    for _ in args:
        count = pwned_api_check(args)
        if count:
            message = f"{args} was found {count} times.... you should probably change your password!"
            break
        else:
            message = f"{args} was not found. Carry on!"
            break
    return message 

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
