from dataclasses import dataclass
from environs import Env


@dataclass
class Bots:
    bot_token: str
    admin_id: int
    redis_pass: str


@dataclass
class Settings:
    bots: Bots


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            admin_id=env.int('ADMIN_ID'),
            bot_token=env.str('BOT_TOKEN'),
            redis_pass=env.str('REDIS_PASS')
        )
    )


settings = get_settings('input')
