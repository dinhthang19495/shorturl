from project.models import ReplaceUrl
from flask import Blueprint
from flask import request
from flask import abort
from flask import redirect
import json

shorturl_api_bp = Blueprint("shorturl_api", "shorturl_api")


@shorturl_api_bp.route('/url', methods=["POST"])
def create_url():
    if request.method != "POST":
        abort(400)
    json_obj = request.get_json()

    print(json_obj)

    large = json_obj["longUrl"]

    url_obj = ReplaceUrl.convert_long_to_short(large)

    return json.dumps(url_obj)


@shorturl_api_bp.route('/url/<count>', methods=["GET"])
def return_long_url(count):
    if request.method != "GET":
        abort(400)

    count = ReplaceUrl.URL_TEMPLATE + count
    url_long = ReplaceUrl.convert_short_to_long(count)
    if url_long:
        return redirect(url_long)
    else:
        return "You Are Short"
