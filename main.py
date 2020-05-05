import requests
import hashlib
import sys

def leak_count(hashes, hash_to_check):
    hashes = (lines.split(':') for lines in hashes.text.splitlines())
    for hash in hashes:
        if hash[0] == hash_to_check:
            return f'This password is leaked {hash[1]} number of times'
    return 'THIS ONE IS SECURE'

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError
    return response

def pwned_api_check(password):

    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head, tail = sha1[:5], sha1[5:]
    return leak_count(request_api_data(head), tail)

def main(args):

    print(f'{password} status is:')
    print(pwned_api_check(password), '\n')


if __name__ == "__main__":
    with open('enter_your_PW_here.txt') as file:
        list_of_passwords = file.readlines()
        for pw in list_of_passwords:
            password = pw.replace('\n', '')
            main(password)
    sys.exit()
