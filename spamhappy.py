#!/bin/bash


# Tools spam Happy <3

# Coded By MzHasan

# zaini.hasan13@gmail.com


# Bersihkan Layar

clear


#This colour

blue='\e[0;34'

cyan='\e[0;36m'

green='\e[0;34m'

white='\e[1;37m'

red='\e[1;31m'

yellow='\e[1;33m'


figlet SpamHappy | lolcat

###################################################

# CTRL C

###################################################

trap ctrl_c INT

ctrl_c() {

clear

echo -e $red"[#]> (Ctrl + C ) Detected, Trying To Exit ... "

sleep 1

echo ""

echo -e $yellow"[#]> Thank You For Using My Tools ... "

sleep 1

echo ""

echo -e $white"[#]> Mz Hasan code ... "

sleep 1

exit

}


echo -e $white" v1 tools for Spam "

echo ""

echo -e $white" ***********************************************"

echo -e $white" # "

echo -e $white" # $cyan Toolkit For$red Tools Spam Happy$white "

echo -e $white" # $cyan Tools Coded by$red Mz Hasan$white "

echo -e $white" # $cyan Contact Me In:$red zaini.hasan13@gmail.com$white"

echo -e $white" # $cyan tools spam update 2019 "

echo -e $white" # "

echo -e $white" ***********************************************"

echo ""

echo -e $white" 01) santet-online"

echo -e $white" 02) SpazSMS"

echo -e $white" 03) Prank"

echo -e $white" 04) semut"

echo -e $white" 05) LITESPAM"

echo -e $red" 100) Exit "

echo -e $white""

read -p "[ToolsSpamHappy]> " act;


if [ $act = 1 ] || [ $act = 01 ]

then

clear

echo -e $blue" Installing santet-online "

sleep 1

apt update && apt upgrade

apt install python2

apt install git

git clone https://github.com/Gameye98/santet-online

echo -e $red" N I C E "

fi


if [ $act = 2 ] || [ $act = 02 ]

then

clear

echo -e $blue" Installing SpazSMS "

sleep 1

apt update && apt upgrade

apt install python2 

apt install git

git clone https://github.com/Gameye98/SpazSMS.git

echo -e $red" N I C E "

fi

if [ $act = 3 ] || [ $act = 3 ]

then

clear

echo -e $blue" Installing prank "

apt update && apt upgrade

apt install python2 

apt install git

git clone https://github.com/siputra12/prank.git

echo -e $blue" N I C E"

fi

if [ $act = 4 ] || [ $act = 4 ]

then

clear

echo -e $blue" Installing semut "

apt update && apt upgrade

apt install python

apt install git

git clone https://github.com/joss24242/semut

echo -e $blue" N I C E"

fi

if [ $act = 5 ] || [ $act = 5 ]

then

clear

echo -e $blue" Installing LITESPAM "

apt update && apt upgrade

git clone https://github.com/4L13199/LITESPAM.git

fi

if [ $act = 100 ] || [ $act = 100 ]

then

echo " Thanks For Using My Tools "

sleep 1

echo " Happy Spam :v"

sleep 1

exit

fi


    