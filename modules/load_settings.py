import configparser
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Setting:
    api_token: str
    api_secret: str


def load_ini(filepath: str) -> dict[str, str]:
    config = configparser.ConfigParser()
    config.read(filepath)
    default = config['DEFAULT']
    return {
        'api_token': default['API_TOKEN'],
        'api_secret': default['API_SECRET'],
    }


def load_settings() -> Setting:
    p = Path(__file__).resolve().parent.parent / 'settings.ini'
    ini_dict = load_ini(p.as_posix())
    return Setting(**ini_dict)
