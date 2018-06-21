#!/bin/bash

# Tools spam Happy <3
# Coded By Mr.k3N
# kencyber996@gmail.com

# Bersihkan Layar
clear

#This colour
blue='\e[0;34'
cyan='\e[0;36m'
green='\e[0;34m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'

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
echo -e $white"[#]> Mr.k3N code ... "
sleep 1
exit
}

echo -e $white"               v1 tools for Spam "
echo ""
echo -e $white" ***********************************************"
echo -e $white" #                                                 "
echo -e $white" # $cyan  Toolkit For$red Tools Spam Happy$white                   "
echo -e $white" # $cyan  Tools Recoded by$red Mr.k3N$white        "
echo -e $white" # $cyan  Contact Me In:$red kencyber996@gmail.com$white"
echo -e $white" # $cyan  Mr.k3N_feat_M4$ Hasan                    "
echo -e $white" #                                                 "
echo -e $white" ***********************************************"
echo ""
echo -e $white" 01) santet-online"
echo -e $white" 02) SpazSMS"
echo -e $red" 100) Exit "
echo -e $white""
read -p "[ToolsSpamHappy]> " act;

if [ $act = 1 ] || [ $act = 01 ]
then
clear
echo -e $red" Installing santet-online "
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
echo -e $red" Installing SpazSMS "
sleep 1
apt update && apt upgrade
apt install python2 
apt install git
https://github.com/Gameye98/SpazSMS
echo -e $red" N I C E "
fi

if [ $act = 100 ] || [ $act = 100  ]
then
echo " Thanks For Using My Tools "
sleep 1
echo " Happy Spam :v"
sleep 1
exit
fi
