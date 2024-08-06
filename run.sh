#!/bin/bash
set -a && source .env && set +a

python quickstart.py --user $SRT_ID --psw $SRT_PASSWORD --dpt $SRT_DEPARTURE --arr $SRT_ARRIVAL --dt $SRT_DATE --tm $SRT_DEPARTURE_HOUR_AFTER
