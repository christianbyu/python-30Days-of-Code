#!/bin/bash
echo "+=================+"
echo "|   No  | Program |"
echo "+=================+"
echo "|   1   | Update  |"
echo "|   2   | Upgrade |"
echo "|   3   | Remove  |"
echo "+=================+" 

echo "Masukan Pilihan : "
read value

case $value in
 1) sudo apt update
 ;;
 2) sudo apt upgrade
 ;;
 3) sudo apt autoremove
 ;;
esac




