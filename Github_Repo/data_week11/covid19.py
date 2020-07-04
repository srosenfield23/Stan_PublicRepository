from csv import reader
import sys
import datetime as dt
def parse_cmd_args(args):
    country_list = args[1:]
    return country_list
def read_data(filename):
    opened_file = open(filename)
    read_file = reader(opened_file)
    data = list(read_file)
    data_dict = {'header': data[0], 'data': data[1:]}
    return data_dict
def extract_data_covid19(country, data_dict):
    country_data = []
    for row in data_dict['data']:
        if row[1] == country:
            country_data.append(row)

    current_date  = dt.datetime.strptime(country_data[-1][0], '%Y-%m-%d')
    final_date = current_date.strftime("%B %d, %Y")

    new_cases = int(country_data[-1][2])
    new_deaths = int(country_data[-1][3])
    total_cases = int(country_data[-1][4])
    total_deaths = int(country_data[-1][5])

    weekly_cases = round(float(country_data[-1][6]))
    weekly_deaths = round(float(country_data[-1][7]))
    biweekly_cases = round(float(country_data[-1][8]))
    biweekly_deaths = round(float(country_data[-1][9]))

    print("This is Covid19 data for: "+final_date)

    print("New cases are:            ".format(row)+('{:,}'.format(new_cases)))
    print("Weekly cases are:     ".format(row)+('{:,}'.format(weekly_cases)))
    print("Biweekly cases are:   ".format(row)+('{:,}'.format(biweekly_cases)))
    print('Total cases are:       '.format(row)+('{:,}'.format(total_cases)))

    print('==========================')

    print("New deaths are:              ".format(row)+('{:,}'.format(new_deaths)))
    print("Weekly deaths are:        ".format(row)+('{:,}'.format(weekly_deaths)))
    print("Biweekly deaths are:     ".format(row)+('{:,}'.format(biweekly_deaths)))
    print("Total deaths are:          ".format(row)+('{:,}'.format(total_deaths)))

    print('==============================')

if __name__ == '__main__':
    country_list = parse_cmd_args(sys.argv)
    data_dict = read_data('full_data.csv')
    data_dict_old = read_data('full_data_24ago.csv')
    data_dict_7day_prior = read_data('covid19-7days_ago.csv')
    data_dict_14day_prior = read_data('covid19-14days_ago.csv')
    data_dict_30day_prior = read_data('covid19-30days_ago.csv')

    data_dict_population = read_data('2020_population.csv')
    for i in country_list:
        print('Stats for {}:'.format(i))
        extract_data_covid19(i, data_dict)
        for c in data_dict_population['data']:
            if c[0] == i:
                population=int(c[1])
                population_mil=(population) / 1000000
                population_100thou=(population) / 100000
                population_10thou=(population) / 10000
                print('{} Population: '.format(i)+('{:,}'.format(population)))
        print('==============================')

        country_data = []
        for row in data_dict['data']:
            if row[1] == i:
                country_data.append(row)

        country_data_old = []
        for row in data_dict_old['data']:
            if row[1] == i:
                country_data_old.append(row)

        country_data_7day_prior = []
        for row in data_dict_7day_prior['data']:
            if row[1] == i:
                country_data_7day_prior.append(row)

        country_data_14day_prior = []
        for row in data_dict_14day_prior['data']:
            if row[1] == i:
                country_data_14day_prior.append(row)

        country_data_30day_prior = []
        for row in data_dict_30day_prior['data']:
            if row[1] == i:
                country_data_30day_prior.append(row)

        double_total_cases_30days_ago = int(country_data_30day_prior[-1][4]) * 2

        total_lives_lost = int(country_data[-1][5]) - int(country_data_7day_prior[-1][5])
        delta_cases_week = int(country_data[-1][4]) - int(country_data_7day_prior[-1][4])

        new_vs_old_cases = int(country_data[-1][2]) - int(country_data_old[-1][2])
        new_vs_7day_prior_cases = int(country_data[-1][2]) - int(country_data_7day_prior[-1][2])

        if int(country_data_old[-1][2]) != 0:
            if int(country_data[-1][2])  >=  int(country_data_old[-1][2]):
                change_new_cases = round(((new_vs_old_cases) / int(country_data_old[-1][2])) * 100,2)
                print('%Increase of new cases over yesterday:  '.format(row)+('{:,}'.format(change_new_cases)),'%')
            if int(country_data_old[-1][2]) > int(country_data[-1][2]):
                change_new_cases = round(((new_vs_old_cases) / int(country_data_old[-1][2])) * 100,2)
                print('%Decrease of new cases over yesterday:  '.format(row)+('{:,}'.format(change_new_cases)),'%')

        if int(country_data_7day_prior[-1][2]) != 0:
            if int(country_data[-1][2])  >=  int(country_data_7day_prior[-1][2]):
                change_new_cases = round(((new_vs_7day_prior_cases) / int(country_data_7day_prior[-1][2])) * 100,2)
                print('%Increase of new cases over week_ago:   '.format(row)+('{:,}'.format(change_new_cases)),'%')

            if int(country_data_7day_prior[-1][2]) > int(country_data[-1][2]):
                change_new_cases = round(((new_vs_7day_prior_cases) / int(country_data_7day_prior[-1][2])) * 100,2)
                print('%Decrease of new cases over week_ago:  '.format(row)+('{:,}'.format(change_new_cases)),'%')

        if int(country_data[-1][5]) != 0:
            new_death_ratio = int(country_data[-1][3]) / int(country_data[-1][5])
        else:
            new_death_ratio = 0
        if int(country_data_old[-1][5]) != 0:
            old_death_ratio = int(country_data_old[-1][3]) / int(country_data_old[-1][5])
        else:
            old_death_ratio = 0

        if int(country_data_7day_prior[-1][5]) != 0:
            new_death_7day_prior_ratio = int(country_data_7day_prior[-1][3]) / int(country_data_7day_prior[-1][5])
        else:
            new_death_7day_prior_ratio = 0
        if  total_lives_lost == 0:
            new_deaths_over_week_deaths = 0
        else:
            new_deaths_over_week_deaths = int(country_data[-1][3]) / (total_lives_lost)

        current_date  = dt.datetime.strptime(country_data[-1][0], '%Y-%m-%d')
        day_of_week = current_date.strftime("%a")

        Weekly_rates_of_infection = round((int(country_data[-1][2]) / (population_10thou)) * 100,2) - round((int(country_data_7day_prior[-1][2]) / (population_10thou)) * 100,2)

        if round((int(country_data[-1][2]) / (population_10thou)) * 100,2) >= round((int(country_data_7day_prior[-1][2]) / (population_10thou)) * 100,2):
            print('Rise in weekly infection rate:                      ',round((Weekly_rates_of_infection),2),"%")
        if round((int(country_data[-1][2]) / (population_10thou)) * 100,2) < round((int(country_data_7day_prior[-1][2]) / (population_10thou)) * 100,2):
            print('Fall in weekly infection rate:                       ',round((Weekly_rates_of_infection),2),"%")

        print('Rates of infection/10k capita (today):       ',round((int(country_data[-1][2]) / (population_10thou)) * 100,2),"%")
        print('Rates of infection/10k capita (week_ago):',round((int(country_data_7day_prior[-1][2]) / (population_10thou)) * 100,2),"%")

        print('New deaths per 100,000 capita (ideal < .03):',round((int(country_data[-1][3]) / (population_100thou)), 2))

        print('Deaths per 100,000 capita (today):                ',round((int(country_data[-1][5]) / (population_100thou)), 2))
        print('Deaths per 100,000 capita (week_ago):        ',round((int(country_data_7day_prior[-1][5]) / (population_100thou)), 2))

        print("New cases rate (today vs yesterday):          ",round(((int(country_data[-1][2]) / int(country_data[-1][4])) - (int(country_data_old[-1][2]) / int(country_data_old[-1][4]))) * 100, 2),"%")
        print("New cases rate (today vs week_ago):         ",round(((int(country_data[-1][2]) / int(country_data[-1][4])) - (int(country_data_7day_prior[-1][2]) / int(country_data_7day_prior[-1][4]))) * 100, 2),"%")

        print("New death rate (today vs yesterday):          ",round(((new_death_ratio) - (old_death_ratio)) * 100,2),"%")
        print("New death rate (today vs week_ago):         ",round(((new_death_ratio) - (new_death_7day_prior_ratio)) * 100,2),"%")

        print('Fatality rate(total death over total case):      ',round((int(country_data[-1][5]) / int(country_data[-1][4])) * 100, 2),"%")
        print("New deaths over lives lost since last",day_of_week," :   ",round((new_deaths_over_week_deaths) * 100),"%")

        increase_n_total = round((delta_cases_week) / int(country_data_7day_prior[-1][4]) * 100,1)

        if increase_n_total >= 0:
            print("Increase in total cases since last",day_of_week, ":         ".format(row)+('{:,}'.format(increase_n_total)),"%")
        else:
            print("Decrease in total cases since last",day_of_week, ":         ".format(row)+('{:,}'.format(increase_n_total)),"%")

        avg_total_cases_14_days = round((int(country_data[-1][4]) - int(country_data_14day_prior[-1][4])) / 14, 2)

        if avg_total_cases_14_days != 0 and int(country_data[-1][2]) >= 0:
            if int(country_data[-1][2]) >=  0 and (int(country_data[-1][2]) <= (avg_total_cases_14_days)):
                print('Percent of new cases below 14 day avg:      ',round(int(country_data[-1][2]) / (avg_total_cases_14_days) * 100 -100),"%")
            if int(country_data[-1][2]) > 0 and (int(country_data[-1][2]) > (avg_total_cases_14_days)) :
                print('Percent of new cases above 14 day avg:      ',round(int(country_data[-1][2]) / (avg_total_cases_14_days) * 100 -100),"%")

        if avg_total_cases_14_days > 3:
            avg_total_cases_14_days = round((int(country_data[-1][4]) - int(country_data_14day_prior[-1][4])) / 14)

        avg_total_cases_30_days = round((int(country_data[-1][4]) - int(country_data_30day_prior[-1][4])) / 30, 2)
        avg_deaths_30_days = round((int(country_data[-1][5]) - int(country_data_30day_prior[-1][5])) / 30, 2)

        if avg_total_cases_30_days != 0 and int(country_data[-1][2]) >= 0:
            if int(country_data[-1][2]) >=  0 and (int(country_data[-1][2]) <= (avg_total_cases_30_days)):
                print('Percent of new cases below 30 day avg:      ',round(int(country_data[-1][2]) / (avg_total_cases_30_days) * 100 -100),"%")
            if int(country_data[-1][2]) > 0 and (int(country_data[-1][2]) > (avg_total_cases_30_days)) :
                print('Percent of new cases above 30 day avg:      ',round(int(country_data[-1][2]) / (avg_total_cases_30_days) * 100 -100),"%")

        if avg_total_cases_30_days > 3:
            avg_total_cases_30_days = round((int(country_data[-1][4]) - int(country_data_30day_prior[-1][4])) / 30)
        if avg_deaths_30_days > 3:
            avg_deaths_30_days = round((int(country_data[-1][5]) - int(country_data_30day_prior[-1][5])) / 30)

        print('Avg new daily cases in last 14 days:            '.format(row)+('{:,}'.format(avg_total_cases_14_days)))
        print('Avg new daily cases in last 30 days:            '.format(row)+('{:,}'.format(avg_total_cases_30_days)))

        print('Avg new daily deaths in last 30 days:             '.format(row)+('{:,}'.format(avg_deaths_30_days)))

        print("Total lives lost since last",day_of_week,":                       ".format(row)+('{:,}'.format(total_lives_lost)))

        if int(country_data[-1][4]) > (double_total_cases_30days_ago):
            print('Total cases if doubled in last 30 days: **HOT_SPOT')
        else:
            print('Total cases if doubled in last 30 days:       Negative')

        print('\n')

print ("** HOT_SPOT status & location determine by Guam")
print ("   Public Health, in consultation with governor")
print ("   and state surgeon physicians' advisory group.")
print("%s: %s" % ("(Source",
"https://www.postguam.com/news/local/epidemiologist-philippines-not-the-only-hot-spot/article_67e9e650-aac2-11ea-adb8-db95d33c4632.html)"))
print('\n')

print ('*** As stated by Dr Christopher Murray, director of')
print ('      the Institute for Health Metrics and Evaluation')
print ('      (IHME): He defined the end of this “wave” as a')
print ('      ratio of: 0.3 deaths per 1 million people.    ')
print ('      Equivalent to: 0.03 deaths per 100,000 capita.')
print("%s: %s" % ("(Source",
"https://www.theguardian.com/world/2020/apr/07/uk-will-be-europes-worst-hit-by-coronavirus-study-predicts)"))
print('\n')

print ('* New cases rate defined as: the percentage ratio')
print ("   between today's new cases over total cases,")
print ("   minus yesterday's new cases over total cases.")
print('\n')

print ('* Rates of infection defined as: the percentage ratio')
print ("   between today's new cases over 10,000 per capita")
print('\n')

print ('*** Death Rate defined as: the percentage ratio ')
print ("      between today's new deaths over total deaths,")
print ("      minus yesterday's new deaths over total deaths.")
print('\n')

print ('*** Economist Intelligence Unit (EIU) analysts')
print ('      said in a note: Death ratios will depend')
print ('      on the capacity of countries to effectively')
print ('      detect, track, and contain the epidemic.')
print("%s: %s" % ("(Source","https://www.cnbc.com/2020/03/18/coronavirus-will-infect-half-the-global-population-eiu-predicts.html)"))
print('\n')

