# 定期実行するスクリプト

from modules.load_settings import load_settings
from modules.call_api import get_status
from modules.repository import save_plug_status


def get_plug_status_and_save(device_id: str):
    status = get_status(device_id)
    ok = status.get('statusCode') == 100 and status.get('message') == 'success'
    if ok:
        body: dict = status['body']
        save_plug_status(body)


settings = load_settings()
for device_id in settings.plug_device_ids:
    get_plug_status_and_save(device_id)
