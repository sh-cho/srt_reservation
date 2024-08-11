""" Quickstart script for InstaPy usage """

# imports
import asyncio
import telegram
from srt_reservation.main import SRT
from srt_reservation.util import parse_cli_args


async def main(cli_args):
    user_id = cli_args.user_id
    user_pw = cli_args.user_pw
    dpt_stn = cli_args.dpt
    arr_stn = cli_args.arr
    dpt_dt = cli_args.dt
    dpt_tm = cli_args.tm

    telegram_bot_token = cli_args.telegram_bot_token
    telegram_chat_id = cli_args.telegram_chat_id

    bot = None
    if telegram_bot_token is not None and telegram_chat_id is not None:
        bot = telegram.Bot(token=telegram_bot_token)

        # # simple check
        # async with bot:
        #     print(await bot.get_me())
        #     await bot.send_message(chat_id=telegram_chat_id, text="Hello, World!")

    srt = SRT(dpt_stn, arr_stn, dpt_dt, dpt_tm, tg_bot=bot, tg_chat_id=telegram_chat_id)
    await srt.run(user_id, user_pw)


if __name__ == "__main__":
    cli_args = parse_cli_args()
    asyncio.run(main(cli_args))
