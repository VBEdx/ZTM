import sys

import requests
import hashlib

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Status code {response.status_code}, check API and try again')

    return response


def get_pass_leak_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())

    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # check password if exists in API response
    # the API allows to search by first 5 hash chars
    # it returns the tails of hash key
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    head, tail =sha1password[:5], sha1password[5:]
    response = request_api_data(head)
    print(head)
    return get_pass_leak_count(response, tail)

def multi_password_check(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'Password {password} has {count} password leaks')
    print('password check complete')

if __name__ == '__main__':
    my_list_of_password = sys.argv[1:]
    sys.exit(multi_password_check(my_list_of_password))

