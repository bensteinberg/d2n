from flask import Flask, jsonify
import sys
import socket
import requests
import xml.etree.ElementTree as etree

app = Flask(__name__)


@app.route("/")
def root():
    return "Hello, world!"

@app.route("/<domain>")
def lookup(domain):
    try:
        return jsonify({'domain': domain, 'orgs': domain2orgs(domain)})
    except:
        error = "%s" % sys.exc_info()[0]
        return jsonify({'domain': domain, 'error': error})


def domain2orgs(domain):
    """Turns a domain name into a list of ARIN orgs"""
    ip = socket.gethostbyname_ex(domain)[2][0]
    url = "https://whois.arin.net/rest/nets;q=%s?showDetails=true&showARIN=false&showNonArinTopLevelNet=false&ext=netref2" % (ip,)
    r = requests.get(url)

    if r.status_code == requests.codes.ok:
        orgs = []
        root = etree.fromstring(r.text)
        for org in root.findall('{https://www.arin.net/whoisrws/core/v1}net/{https://www.arin.net/whoisrws/core/v1}orgRef'):
            orgs.append(org.text)
        return orgs
    return None


if __name__ == "__main__":
    app.run()
