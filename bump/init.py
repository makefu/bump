from flask import Flask, Response, request, send_from_directory
from functools import wraps
import random
import string
import os
app = Flask(__name__)
storedir = os.path.join(app.root_path, 'store')
app.config['storedir'] = storedir
print("Storedir is %s" % storedir)
if not os.path.isdir(storedir):
   os.mkdir(storedir)


def returns_plain(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        r = f(*args, **kwargs)
        return Response(r, content_type='text/plain; charset=utf-8')
    return decorated_function


def usage(host):
    return """Bump Usage:
> echo balls | curl -F "p=<-" {0}
<   http://{0}/q9a1bfljzm
> curl {0}/q9a1bfljzm
<   balls
Source at http://github.com/makefu/bump""".format(host)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


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
    return "http://%s/%s\n" % (request.host, key)
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
        try:
            # py3
            f.write(bytes(value, "UTF-8"))
        except:
            # py2
            f.write(value)


def retrieve(key):
    with open("%s/%s" % (storedir, key), "rb+") as f:
        return f.read().decode("UTF-8")


def generate_key():
    s = string.ascii_lowercase+string.digits
    return ''.join(random.sample(s, 10))


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
