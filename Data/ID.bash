#!/bin/bash
WAN=${@: -1}

getid () {
#sort
sort -n ./tmp/$1 > /tmp/tmp.txt
rm ./tmp/$1
mv /tmp/tmp.txt ./tmp/$1

#count
id=2
lines=`cat ./tmp/$1`
for line in $lines; do
        if [ $id -eq $(($line)) ]
        then
        id=$(($id+1))
        fi
done
echo $id >> ./tmp/$1
return $id
}

ls /opt/vyatta/config/active/traffic-control/advanced-queue/root/queue > ./tmp/queue.txt
ls /opt/vyatta/config/active/traffic-control/advanced-queue/leaf/queue >> ./tmp/queue.txt
ls /opt/vyatta/config/active/traffic-control/advanced-queue/branch/queue >> ./tmp/queue.txt
ls /opt/vyatta/config/active/traffic-control/advanced-queue/filters/match > ./tmp/filter.txt
ls /opt/vyatta/config/active/firewall/modify/Modify/rule > ./tmp/rules.txt
ls /opt/vyatta/config/active/firewall/name/$WAN/rule > ./tmp/wrules.txt
rm ./tmp/marks.txt
touch ./tmp/marks.txt
lines=`cat ./tmp/rules.txt`
for line in $lines; do
        echo "$(cat /opt/vyatta/config/active/firewall/modify/Modify/rule/$line/modify/mark/node.val) " >> ./tmp/marks.txt
done


ID=""

for i in $(seq 1 $1); do
        getid queue.txt
	ID+="$? "
done
for i in $(seq 1 $2); do
        getid filter.txt
	ID+="$? "

done
for i in $(seq 1 $3); do
        getid rules.txt
	ID+="$? "
done
for i in $(seq 1 $4); do
        getid marks.txt
	ID+="$? "
done
for i in $(seq 1 $5); do
        getid wrules.txt
	ID+="$? "
done
echo $ID > ./Data/ID.txt

