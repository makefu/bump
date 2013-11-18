from flask import Flask, Response, request
from functools import wraps
import sys
import random
import string
import os
storedir = "%s/../store" % os.path.dirname(os.path.abspath(sys.argv[0]))
app = Flask(__name__)
app.config['storedir'] = storedir


def returns_plain(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        r = f(*args, **kwargs)
        return Response(r, content_type='text/plain; charset=utf-8')
    return decorated_function


def usage(host):
    return """Usage:
> echo balls | curl -F "p=<-" {0}
<   http://{0}/q9a1bfljzm
> curl {0}/q9a1bfljzm
<   balls""".format(host)


@returns_plain
@app.route("/", methods=["GET"])
def init():
    #return Response(quicktip+open(sys.argv[0], "r").read(),
    return Response(usage(request.host),
                    content_type="text/plain; charset=utf-8")


@returns_plain
@app.route("/", methods=["POST"])
def store_file():
    #try:
    data = request.form['p']
    key = generate_key()
    store(key, data)
    return u"http://%s/%s\n" % (request.host, key)
    #except Exception as e:
    #    print(e)
    #    return usage(request.host), 401


@returns_plain
@app.route("/<key>", methods=["GET"])
def retrieve_file(key):
    try:
        return retrieve(key)
    except:
        return "'%s' not found! " % key, 404


def store(key, value):
    with open("%s/%s" % (storedir, key), "wb+") as f:
        f.write(bytes(value, "UTF-8"))


def retrieve(key):
    with open("%s/%s" % (storedir, key), "rb+") as f:
        return f.read().decode("UTF-8")


def generate_key():
    s = string.ascii_lowercase+string.digits
    return ''.join(random.sample(s, 10))


if __name__ == "__main__":
    #app.debug = True
    print("Storedir is %s" % storedir)
    try:
        os.mkdir(storedir)
    except:
        pass
    app.run(host='0.0.0.0')
