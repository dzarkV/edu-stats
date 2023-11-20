#!/bin/bash

YELLOW='\033[33m'
RED='\033[31m'
GREEN='\033[32m'
RESET='\033[0m'

# Solicita al usuario el nombre del canal de Slack
    echo -e "${YELLOW}This script will allow you to obtain the configuration files necessary to run the project.${RESET}"
    echo ""
    echo "Enter the name of the Slack channel:"
    read channel
# Comprueba el argumento de entrada
if [ "$(echo $channel | base64)" == "dmVyK3RlY2hmZWxsb3dzCg==" ]; then
    # Define la URL desde la que se descargarán los archivos (URLs con fecha de expiración)
    url1="U2FsdGVkX19DQeW5DYxlAA5LwbRHk3NWmFJzcynNa4A4U1oVE2ejWZ/8b/qXwd+nCySSw6/BBdMkgMq8WS1SRSXIwQyImMEGn3DLcHlck+8o9PznBpPUhksRScNx3twdPZpFpMXZAc3AJoRLt4wfpF2MqSkFnxhnSuckbkrrySdgk+DyQAAms5a/iYTPOLbStrTIORpBbuB3YO1RTlzhTXSQUUnmOOxOAW4CjsQIz1lpblDldQ3WAPPhT68cI7PI7UK7UvSPxntjsUyvaIVOS1htjAFwacLyBropWSWjnfY="
    url2="U2FsdGVkX1+dmodhTSYJxj2lA3RHcV/9fT+OnkH1jSylTAUSgfum837UcMRGTLAnCyKZNX61mZXxuiNF5TWqQ0ivINFcbMc03StoyS3Kbdge/PNcKG6WMrCsSdFsUg4la4t3b7BSAwqBKQTGV/DkZSfqxm8ahLb2nEQrHFut2qBONmRKhQb+ktibSNWHbkDnbz4UT+anvgL6LheKZUPyIsX9IGudjR2pP+7A8l3Z0G9wPetbuwDRvbXEKGA4pIoyvQPt/Xla+CFdedcbvzB3GMueZ99ACRkob3kr+tIYfYt3q8Y4uPgNw+FHKPjdgAefVo4jm5GXYtFUir3fa0XDag=="

    # Descarga el archivo de la URL
    if [ "$(command -v curl)" ]; then
        echo -e "${GREEN}Downloading files with curl...${RESET}"
        curl -o be-edu-stats/data_source/.env "$(echo $url1 | openssl enc -aes128 -pbkdf2 -a -d -k $channel)" 
        curl -o be-edu-stats/data_source/bqprojectworldbankeducation-9ad27c9d0bbf.json "$(echo $url2 | openssl enc -aes128 -pbkdf2 -a -d -k $channel)"
    else
        echo -e "${RED}cURL not found. Please install cURL and run the script again.${RESET}"
    fi

else
    echo "The argument is not valid. Please enter the name of the community channel."
fi
