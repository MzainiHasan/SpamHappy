#!/bin/bash

# Tools SpamHappy 💥
# Coded by MzHasan | zaini.hasan13@gmail.com

# ============ SETUP WARNA ============
blue='\e[0;34m'
cyan='\e[0;36m'
green='\e[0;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'

# ============ CTRL+C Handler ============
trap ctrl_c INT
ctrl_c() {
    clear
    echo -e "$red[#]> (Ctrl + C) Detected, Trying To Exit ..."
    sleep 1
    echo -e "$yellow[#]> Thank You For Using My Tools ..."
    sleep 1
    echo -e "$white[#]> MzHasan Code ..."
    sleep 1
    exit
}

# ============ TAMPILAN AWAL ============
clear
command -v figlet >/dev/null && figlet SpamHappy | lolcat || echo -e "$cyan*** SpamHappy ***"
echo -e "$white v1.2 Tools for Spam"
echo ""
echo -e "$white***********************************************"
echo -e "$white# $cyan Toolkit for$red SpamHappy$white"
echo -e "$white# $cyan Coded by$red MzHasan$white"
echo -e "$white# $cyan Contact:$red zaini.hasan13@gmail.com$white"
echo -e "$white# $cyan Update 2020"
echo -e "$white***********************************************"
echo ""
echo -e "$white 01) KANG-NEWBIE"
echo -e "$white 02) SpazSMS"
echo -e "$white 03) Prank"
echo -e "$white 04) Semut"
echo -e "$white 05) LITESPAM"
echo -e "$red  100) Exit"
echo ""

read -p "[ToolsSpamHappy]> " act

case $act in
    1|01)
        clear
        echo -e "$blue Installing KANG-NEWBIE..."
        apt update && apt upgrade -y
        apt install -y python git
        git clone https://github.com/KANG-NEWBIE/SpamSms.git
        echo -e "$red N I C E"
        ;;
    2|02)
        clear
        echo -e "$blue Installing SpazSMS..."
        apt update && apt upgrade -y
        apt install -y python2 git
        git clone https://github.com/Gameye98/SpazSMS.git
        echo -e "$red N I C E"
        ;;
    3|03)
        clear
        echo -e "$blue Installing Prank..."
        apt update && apt upgrade -y
        apt install -y python2 git
        git clone https://github.com/siputra12/prank.git
        echo -e "$blue N I C E"
        ;;
    4|04)
        clear
        echo -e "$blue Installing Semut..."
        apt update && apt upgrade -y
        apt install -y python git
        git clone https://github.com/joss24242/semut
        echo -e "$blue N I C E"
        ;;
    5|05)
        clear
        echo -e "$blue Installing LITESPAM..."
        apt update && apt upgrade -y
        git clone https://github.com/4L13199/LITESPAM.git
        echo -e "$blue N I C E"
        ;;
    100)
        echo -e "$green Thanks for using my tools!"
        sleep 1
        echo -e "$yellow Happy Spamming! :v"
        sleep 1
        exit
        ;;
    *)
        echo -e "$red Invalid option!"
        ;;
esac
