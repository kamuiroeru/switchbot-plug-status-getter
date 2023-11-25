from typing import Final
import time
import hashlib
import hmac
import base64
import uuid
import requests

from modules.load_settings import load_settings


def generate_request_header() -> dict[str, str]:
    """SwitchBot のAPIを叩くための Request Header を作る
    FYI: https://github.com/OpenWonderLabs/SwitchBotAPI#python-3-example-code

    Returns:
        dict[str, str]: _description_
    """
    api_header = {}
    settings = load_settings()
    token = settings.api_token
    secret = settings.api_secret
    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = "{}{}{}".format(token, t, nonce)

    string_to_sign = bytes(string_to_sign, "utf-8")
    secret = bytes(secret, "utf-8")

    sign = base64.b64encode(
        hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest()
    )
    # print("Authorization: {}".format(token))
    # print("t: {}".format(t))
    # print("sign: {}".format(str(sign, "utf-8")))
    # print("nonce: {}".format(nonce))

    # Build api header JSON
    api_header["Authorization"] = token
    api_header["Content-Type"] = "application/json"
    api_header["charset"] = "utf8"
    api_header["t"] = str(t)
    api_header["sign"] = str(sign, "utf-8")
    api_header["nonce"] = str(nonce)

    return {
        "Authorization": token,
        "Content-Type": "application/json",
        "charset": "utf8",
        "t": str(t),
        "sign": str(sign, "utf-8"),
        "nonce": str(nonce),
    }


BASE_URL: Final[str] = "https://api.switch-bot.com"
HEADERS = generate_request_header()


def get_devices() -> dict:
    path = "/v1.1/devices/"
    r = requests.get(BASE_URL + path, headers=HEADERS, timeout=6.0)
    if r.status_code == 200:
        return r.json()
    else:
        return {}

def get_status(device_id: str) -> dict:
    path = f"/v1.1/devices/{device_id}/status"
    r = requests.get(BASE_URL + path, headers=HEADERS, timeout=6.0)
    if r.status_code == 200:
        return r.json()
    else:
        return {}


def get_command(device_id: str) -> dict:
    path = f"/v1.1/devices/{device_id}/commands"
    r = requests.post(BASE_URL + path, headers=HEADERS, timeout=6.0)
    if r.status_code == 200:
        return r.json()
    else:
        return {}
