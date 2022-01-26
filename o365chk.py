import requests
import json
import argparse


def make_requests(target):
    params = {
        'login': 'username@' + str(target),
        'json': '1'
    }

    url = 'https://login.microsoftonline.com/getuserrealm.srf'

    try:
        r = requests.get(url, params=params)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
        raise SystemExit(errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        raise SystemExit(errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        raise SystemExit(errt)
    except requests.exceptions.RequestException as err:
        print("Uh-oh: Something Bad Happened", err)
        raise SystemExit(err)

    r = r.json()

    return r


def get_status(response_json):

    x = json.dumps(response_json)

    x = json.loads(x)

    return x


def convert_indent(indent):
    try:
        return int(indent)
    except ValueError as errv:
        print('You need to enter a number')
        print(errv)
        quit()


def main():

    parser = argparse.ArgumentParser(description='Checks to see if an O365 instance is associated with a domain.')
    parser.add_argument('-d', '--domain', help='Specifies the domain to be checked', required=True)
    parser.add_argument('-i', '--indent', help='You can change the number of indents', default=4)
    args = parser.parse_args()

    domain = args.domain
    number_of_indent = convert_indent(args.indent)

    data = make_requests(domain)

    result = get_status(data)

    print(json.dumps(result, indent=number_of_indent, sort_keys=True))

    with open("result.json", "w") as outfile:
        json.dump(result, outfile)



main()