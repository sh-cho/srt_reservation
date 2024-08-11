#!/bin/bash
set -a && source .env && set +a

python quickstart.py --user_id $SRT_ID --user_pw $SRT_PASSWORD --dpt $SRT_DEPARTURE --arr $SRT_ARRIVAL --dt $SRT_DATE --tm $SRT_DEPARTURE_HOUR_AFTER --telegram_bot_token=$TELEGRAM_BOT_TOKEN --telegram_chat_id=$TELEGRAM_CHAT_ID
