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

#-- python3 covid19.py World "United States" Mexico Russia "United Kingdom" Belgium Germany Italy France Spain Sweden Bangladesh India Pakistan Guatemala Iraq Iran "Saudi Arabia" Qatar Brazil Bolivia Chile Peru "South Africa" Ghana Turkey Kuwait Egypt Oman Philippines Indonesia China > /home/oracle/Covid19_"${now}".txt

python3 covid19.py Afghanistan Albania Algeria Andorra Angola Anguilla "Antigua and Barbuda" Argentina Armenia Aruba Australia Austria Azerbaijan Bahamas Bahrain Bangladesh Barbados Belarus Belgium Belize Benin Bermuda Bhutan Bolivia "Bosnia and Herzegovina" Botswana Brazil "British Virgin Islands" Brunei Bulgaria "Burkina Faso" Burundi Cambodia Cameroon Canada "Cape Verde" "Cayman Islands" "Central African Republic" Chad Chile China Colombia Comoros Congo "Costa Rica" "Cote d'Ivoire" Croatia Cuba Curacao Cyprus "Czech Republic" "Democratic Republic of Congo" Denmark Djibouti Dominica "Dominican Republic" Ecuador Egypt "El Salvador" "Equatorial Guinea" Eritrea Estonia Eswatini Ethiopia "Faeroe Islands" >> /home/oracle/Covid19_"${now}".txt &&

python3 covid19.py "Falkland Islands" Fiji Finland France "French Polynesia" Gabon Gambia Georgia Germany Ghana Gibraltar Greece Greenland Grenada Guam Guatemala Guernsey Guinea Guinea-Bissau Guyana Haiti Honduras Hungary Iceland India Indonesia Iran Iraq Ireland "Isle of Man" Israel Italy Jamaica Japan Jersey Jordan Kazakhstan Kenya Kosovo Kuwait Kyrgyzstan Laos Latvia Lebanon Lesotho Liberia Libya Liechtenstein Lithuania Luxembourg "North Macedonia" Madagascar Malawi Malaysia Maldives >> /home/oracle/Covid19_"${now}".txt &&

python3 covid19.py Mali Malta Mauritania Mauritius Mexico Moldova Monaco Mongolia Montenegro Montserrat Morocco Mozambique Myanmar Namibia Nepal Netherlands "New Caledonia" "New Zealand" Nicaragua Niger Nigeria "Northern Mariana Islands" Norway Oman >> /home/oracle/Covid19_"${now}".txt &&

python3 covid19.py Pakistan Palestine Panama "Papua New Guinea" Paraguay Peru Philippines Poland Portugal "Puerto Rico" Qatar Romania Russia Rwanda "Saint Kitts and Nevis" "Saint Lucia" "Saint Vincent and the Grenadines" "San Marino" "Sao Tome and Principe" >> /home/oracle/Covid19_"${now}".txt &&

python3 covid19.py "Saudi Arabia" Senegal Serbia Seychelles "Sierra Leone" Singapore "Sint Maarten (Dutch part)" Slovakia Slovenia Somalia "South Africa" "South Korea" "South Sudan" Spain "Sri Lanka" Sudan Suriname Sweden Switzerland Syria Taiwan Tajikistan Tanzania >> /home/oracle/Covid19_"${now}".txt &&

python3 covid19.py Thailand Timor Togo "Trinidad and Tobago" Tunisia Turkey "Turks and Caicos Islands" Uganda Ukraine "United Arab Emirates" "United Kingdom" "United States" "United States Virgin Islands" Uruguay Uzbekistan Vatican Venezuela Vietnam >> /home/oracle/Covid19_"${now}".txt &&

cp /home/oracle/data_week11/covid19_with_footers.py /home/oracle/data_week11/covid19.py &&

python3 covid19.py "Western Sahara" World Yemen Zambia Zimbabwe >> /home/oracle/Covid19_"${now}".txt

fi
exit 0
