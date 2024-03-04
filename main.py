from asyncio import run

import global_vars
from modules.bot import main as start
from modules.logger import Logger


Logger.load_config()

if __name__ == "__main__":
    run(start(global_vars.bot, global_vars.dp))
