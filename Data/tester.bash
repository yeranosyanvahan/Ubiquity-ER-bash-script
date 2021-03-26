
if test -z "$1"  || test -z "$2"  || test -z "$3"; then 
help
fi

if test "$1" != "add" && test "$1" != "delete" || (test "$2" != "tariff" && test "$2" != "customer" && test "$2" != "suspend"); then
help
fi


if test "$2" = "customer" && ! valid_ip $4; then

echo "Invalid IP address $4 for tariff plan $3"
echo "If you want tariff plan to be $3 $4 use quotes: \"$3 $4\""
exit 1

fi


if test "$2" = "suspend" && ! valid_ip $3; then

echo "Invalid IP address $3 to suspend"
exit 1

fi

if test "$2" = "tariff"  && test "$1" = "add" && $(! [[ "$4" =~ ^[0-9]+$ ]] || ! [[ "$5" =~ ^[0-9]+$ ]]); then

echo "Invalid Download speed $4 mbit and Upload speed $5 mbit"
exit 1
fi

if test "$2" = "customer" && ! test -z "$5" || ! test -z "$6" ; then
echo -e "\ntoo many arguments entered\n"
exit 1
fi

if test "$2" = "tariff" && test "$1" = "delete" && ! test -z "$4"  ; then
echo -e "\ntoo many arguments entered\n"
exit 1
fi

if test "$2" = "suspend" && ! test -z "$4"  ; then
echo -e "\ntoo many arguments entered\n"
exit 1
fi
