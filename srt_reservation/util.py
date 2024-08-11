import argparse

def parse_cli_args():

    parser = argparse.ArgumentParser(description='')

    parser.add_argument("--user_id", help="User ID", type=str, metavar="1234567890")
    parser.add_argument("--user_pw", help="User Password", type=str, metavar="abc1234")
    parser.add_argument("--dpt", help="Departure Station", type=str, metavar="동탄")
    parser.add_argument("--arr", help="Arrival Station", type=str, metavar="동대구")
    parser.add_argument("--dt", help="Departure Date", type=str, metavar="20220118")
    parser.add_argument("--tm", help="Departure Time", type=str, metavar="08, 10, 12, ...")

    parser.add_argument("--telegram_bot_token", help="Telegram bot token", type=str, metavar="1234567890:ABCDEFG")
    parser.add_argument("--telegram_chat_id", help="Telegram chat id", type=str, metavar="1234567890")

    parser.add_argument("--num", help="no of trains to check", type=int, metavar="2", default=2)
    parser.add_argument("--reserve", help="Reserve or not", type=bool, metavar="2", default=False)

    args = parser.parse_args()

    return args
