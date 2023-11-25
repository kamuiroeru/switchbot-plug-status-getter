from modules.schema.models import PlugStatus
from modules.schema.engine import Session


def save_plug_status(plug_status_body: dict):
    """Switch Bot Plug の status（電圧電流等）を DB に保存する

    Args:
        plug_status_body (dict): apiのレスポンス body Dict. FYI: https://github.com/OpenWonderLabs/SwitchBotAPI#plug-mini-jp-1
    """

    record = PlugStatus(
        device_id = plug_status_body['deviceId'],
        device_type = plug_status_body['deviceType'],
        hub_device_id = plug_status_body['hubDeviceId'],
        power = plug_status_body['power'],
        voltage = plug_status_body['voltage'],
        weight = plug_status_body['weight'],
        electricity_of_day = plug_status_body['electricityOfDay'],
        electric_current = plug_status_body['electricCurrent'],
        version = plug_status_body['version'],
    )
    session = Session()
    session.add(record)
    session.commit()

