#! /usr/bin/bash
curl -O "https://covid.ourworldindata.org/data/ecdc/full_data.csv" && grep -rl 'Swaziland' full_data.csv | xargs sed -i 's/Swaziland/Eswatini/g'
grep -rl Macedonia full_data.csv | xargs sed -i 's/Macedonia/"North Macedonia"/g'
FILENAME1=/home/oracle/full_data.csv
FILENAME2=/home/oracle/data_week11/full_data.csv
FILESIZE1=$(stat -c%s "$FILENAME1")
FILESIZE2=$(stat -c%s "$FILENAME2")
now=$(date +"%b_%d_%Y")
now2=$(date +%Y-%m-%d -d "-7 days")
now3=$(date +%Y-%m-%d -d "-30 days")
if [ "$FILESIZE1" = "$FILESIZE2" ]
then crontab cron-file.txt
else grep ${now2} full_data.csv > /home/oracle/data_week11/covid19-7days_ago.csv && sed -i '1s/^/date,location,new_cases,new_deaths,total_cases,total_deaths\n/' /home/oracle/data_week11/covid19-7days_ago.csv && grep ${now3} full_data.csv > /home/oracle/data_week11/covid19-30days_ago.csv && sed -i '1s/^/date,location,new_cases,new_deaths,total_cases,total_deaths\n/' /home/oracle/data_week11/covid19-30days_ago.csv

mv /home/oracle/data_week11/full_data.csv /home/oracle/data_week11/full_data_24ago.csv
cp full_data.csv /home/oracle/data_week11/full_data.csv
crontab cron-file-6a.txt
rm /home/oracle/Covid19_*.txt
cat /dev/null > /home/oracle/Covid19_"${now}".txt
cd data_week11

python3 covid19.py World "United States" Mexico Russia "United Kingdom" Belgium Germany Italy France Spain Sweden Bangladesh India Pakistan Guatemala Iraq Iran "Saudi Arabia" Qatar Brazil Bolivia Chile Peru "South Africa" Ghana Turkey Kuwait Egypt Oman Philippines Indonesia China > /home/oracle/Covid19_"${now}".txt

fi
exit 0
