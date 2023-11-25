import configparser
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Setting:
    api_token: str
    api_secret: str
    plug_device_ids: list[str]


def parse_to_list_str(raw: str) -> list[str]:
    return list(map(lambda elem: elem.strip(), raw.split(',')))


def load_ini(filepath: str) -> dict:
    config = configparser.ConfigParser()
    config.read(filepath)
    default = config['DEFAULT']
    return {
        'api_token': default['API_TOKEN'],
        'api_secret': default['API_SECRET'],
        'plug_device_ids': parse_to_list_str(default['PLUG_DEVICE_IDS'])
    }


def load_settings() -> Setting:
    p = Path(__file__).resolve().parent.parent / 'settings.ini'
    ini_dict = load_ini(p.as_posix())
    return Setting(**ini_dict)
