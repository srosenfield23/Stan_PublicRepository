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

        new_vs_old_cases = int(country_data[-1][2]) - int(country_data_old[-1][2])
        new_vs_7day_prior_cases = int(country_data[-1][2]) - int(country_data_7day_prior[-1][2])

        if int(country_data_old[-1][2]) != 0:
            change_new_cases = (new_vs_old_cases) / int(country_data_old[-1][2]) * 100
            if int(country_data[-1][2])  >=  int(country_data_old[-1][2]):
                if change_new_cases < 100 and change_new_cases >= 0:
                    change_new_cases = round((change_new_cases),2)
                if change_new_cases > 99.99 or change_new_cases < -99.99:
                    change_new_cases = round(change_new_cases)
                print('%Increase of new cases over yesterday:   '.format(row)+('{:,}'.format(change_new_cases)),'%')

            if int(country_data_old[-1][2]) > int(country_data[-1][2]):
                if change_new_cases  < -99.99:
                    change_new_cases = round(change_new_cases)
                if change_new_cases  > -99.99 and change_new_cases < 0:
                    change_new_cases = round((change_new_cases), 2)
                print('%Decrease of new cases over yesterday:  '.format(row)+('{:,}'.format(change_new_cases)),'%')

        if int(country_data_7day_prior[-1][2]) != 0:
            change_new_cases = (new_vs_7day_prior_cases) / int(country_data_7day_prior[-1][2]) * 100
            if int(country_data[-1][2])  >=  int(country_data_7day_prior[-1][2]):
                if change_new_cases < 100 and change_new_cases >= 0:
                    change_new_cases = round((change_new_cases), 2)
                if change_new_cases > 99.99 or change_new_cases < -99.99:
                    change_new_cases = round(change_new_cases)
                print('%Increase of new cases over week_ago:   '.format(row)+('{:,}'.format(change_new_cases)),'%')

            if int(country_data_7day_prior[-1][2]) > int(country_data[-1][2]):
                if change_new_cases  < -99.99:
                    change_new_cases = round(change_new_cases)
                if change_new_cases  > -99.99 and change_new_cases < 0:
                    change_new_cases = round((change_new_cases), 2)
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

        weekly_deaths = round(float(country_data[-1][7]))

        if  weekly_deaths == 0:
            new_deaths_over_week_deaths = 0
        else:
            new_deaths_over_week_deaths = int(country_data[-1][3]) / (weekly_deaths)

        current_date  = dt.datetime.strptime(country_data[-1][0], '%Y-%m-%d')
        day_of_week = current_date.strftime("%a")

        weekly_rates_of_infection = round((int(country_data[-1][2]) / (population_10thou)) * 100,2) - round((int(country_data_7day_prior[-1][2]) / (population_10thou)) * 100,2)

        if round((int(country_data[-1][2]) / (population_10thou)) * 100,2) >= round((int(country_data_7day_prior[-1][2]) / (population_10thou)) * 100,2):
            if weekly_rates_of_infection < 99.99:
                print('Rise in weekly infection rate:                      ',round((weekly_rates_of_infection),2),"%")
            else:
                print('Rise in weekly infection rate:                      ',round((weekly_rates_of_infection)),"%")

        if round((int(country_data[-1][2]) / (population_10thou)) * 100,2) < round((int(country_data_7day_prior[-1][2]) / (population_10thou)) * 100,2):
            if weekly_rates_of_infection >= -100.00:
                print('Fall in weekly infection rate:                       ',round((weekly_rates_of_infection),2),"%")
            else:
                print('Fall in weekly infection rate:                       ',round((weekly_rates_of_infection)),"%")

        rates_of_infection_capita_today = int(country_data[-1][2]) / (population_10thou) * 100
        rates_of_infection_capita_week_ago = int(country_data_7day_prior[-1][2]) / (population_10thou) * 100

        if rates_of_infection_capita_today >= 100.00:
            rates_of_infection_capita_today = round(rates_of_infection_capita_today)
        if rates_of_infection_capita_today < 100.00:
            rates_of_infection_capita_today = round((rates_of_infection_capita_today),2)
        print('Rates of infection/10k capita (today):         ',(rates_of_infection_capita_today),"%")

        if rates_of_infection_capita_week_ago >= 100.00:
            rates_of_infection_capita_week_ago = round(rates_of_infection_capita_week_ago)
        if rates_of_infection_capita_week_ago < 100.00:
            rates_of_infection_capita_week_ago = round((rates_of_infection_capita_week_ago),2)
        print('Rates of infection/10k capita (week_ago):  ',(rates_of_infection_capita_week_ago),"%")

        weekly_cases = float(country_data[-1][6])
        weekly_case_rate_avg_100k = round(((weekly_cases) / 7) / (population_100thou), 2)

        print('Rate of avg weekly cases/100k capita:        '.format(row)+('{:,}'.format(weekly_case_rate_avg_100k)))

        print('Rate of new deaths/100k capita(goal < .03): ',round((int(country_data[-1][3]) / (population_100thou)), 2))

        print('Deaths per 100,000 capita (today):              ',round((int(country_data[-1][5]) / (population_100thou)), 2))
        print('Deaths per 100,000 capita (week_ago):      ',round((int(country_data_7day_prior[-1][5]) / (population_100thou)), 2))

        print("New cases rate (today vs yesterday):         ",round(((int(country_data[-1][2]) / int(country_data[-1][4])) - (int(country_data_old[-1][2]) / int(country_data_old[-1][4]))) * 100, 2),"%")
        print("New cases rate (today vs week_ago):        ",round(((int(country_data[-1][2]) / int(country_data[-1][4])) - (int(country_data_7day_prior[-1][2]) / int(country_data_7day_prior[-1][4]))) * 100, 2),"%")

        print("New death rate (today vs yesterday):         ",round(((new_death_ratio) - (old_death_ratio)) * 100,2),"%")
        print("New death rate (today vs week_ago):        ",round(((new_death_ratio) - (new_death_7day_prior_ratio)) * 100,2),"%")

        print('Fatality rate(total death over total case):     ',round((int(country_data[-1][5]) / int(country_data[-1][4])) * 100, 2),"%")

        print("07-Day ratio of new over weekly deaths:      ",round((new_deaths_over_week_deaths) * 100),"%")

        increase_n_total = round(((weekly_cases) / int(country_data_7day_prior[-1][4])) * 100,1)

        if increase_n_total >= 0:
            print("Increase in total cases since last",day_of_week, ":       ".format(row)+('{:,}'.format(increase_n_total)),"%")
        else:
            print("Decrease in total cases since last",day_of_week, ":       ".format(row)+('{:,}'.format(increase_n_total)),"%")

        biweekly_cases2 = float(country_data[-1][8])
        avg_cases_14_days = round((biweekly_cases2) / 14, 2)
        avg_cases_30_days = round((int(country_data[-1][4]) - int(country_data_30day_prior[-1][4])) / 30, 2)

        if avg_cases_14_days != 0:
            percent_new_cases_14 = (int(country_data[-1][2]) / (avg_cases_14_days) * 100) -100

        if avg_cases_14_days != 0 and int(country_data[-1][2]) >= 0:
            if int(country_data[-1][2]) >=  0 and int(country_data[-1][2]) <= (avg_cases_14_days):
                if percent_new_cases_14 < 100:
                    percent_new_cases_14 = round((percent_new_cases_14), 1)
                else:
                    percent_new_cases_14 = round(percent_new_cases_14)
                print('Percent of new cases below 14 day avg:    ',(percent_new_cases_14)),"%"

            if int(country_data[-1][2]) >= 0 and int(country_data[-1][2]) > (avg_cases_14_days):
                if percent_new_cases_14 < 100 and percent_new_cases_14 >= -100:
                    percent_new_cases_14 = round((percent_new_cases_14), 1)
                else:
                    percent_new_cases_14 = round(percent_new_cases_14)
                print('Percent of new cases above 14 day avg:    ',(percent_new_cases_14)),"%"

        if avg_cases_14_days > 3 or avg_cases_14_days < 3:
           avg_cases_14_days = round((biweekly_cases2) / 14)

        avg_deaths_30_days = round((int(country_data[-1][5]) - int(country_data_30day_prior[-1][5])) / 30, 2)

        if avg_cases_30_days != 0:
            percent_new_cases_30 = (int(country_data[-1][2]) / (avg_cases_30_days) * 100) -100

        if avg_cases_30_days != 0 and int(country_data[-1][2]) >= 0:
            if int(country_data[-1][2]) >=  0 and (int(country_data[-1][2]) <= (avg_cases_30_days)):
                if percent_new_cases_30 < 100:
                    percent_new_cases_30 = round((percent_new_cases_30), 1)
                else:
                    percent_new_cases_30 = round(percent_new_cases_30)
                print('Percent of new cases below 30 day avg:    ',(percent_new_cases_30)),"%"

            if int(country_data[-1][2]) > 0 and (int(country_data[-1][2]) > (avg_cases_30_days)) :
                if percent_new_cases_30 < 100 and percent_new_cases_30 >= -100:
                    percent_new_cases_30 = round((percent_new_cases_30), 1)
                else:
                    percent_new_cases_30 = round(percent_new_cases_30)
                print('Percent of new cases above 30 day avg:    ',(percent_new_cases_30)),"%"

        if avg_cases_30_days > 3:
            avg_cases_30_days = round((int(country_data[-1][4]) - int(country_data_30day_prior[-1][4])) / 30)
        if avg_deaths_30_days > 3:
            avg_deaths_30_days = round((int(country_data[-1][5]) - int(country_data_30day_prior[-1][5])) / 30)

        avg_cases_7_days = round((weekly_cases) / 7)

        print('07-Day average of new daily cases:             '.format(row)+('{:,}'.format(avg_cases_7_days)))

        print('14-Day average of new daily cases:             '.format(row)+('{:,}'.format(avg_cases_14_days)))

        print('30-Day average of new daily cases:             '.format(row)+('{:,}'.format(avg_cases_30_days)))

        print('30-Day average of new daily deaths:               '.format(row)+('{:,}'.format(avg_deaths_30_days)))

        print("7-Day total of lives lost since",day_of_week,":                ".format(row)+('{:,}'.format(weekly_deaths)))

        total_cases = int(country_data[-1][4])
        doubled_cases_30days_ago = int(country_data_30day_prior[-1][4]) * 2
        quadrupled_cases_30days_ago = (doubled_cases_30days_ago) * 2

        print("Today's case total:                                    ".format(row)+('{:,}'.format(total_cases)))
        print('30-Day doubled case total:                      '.format(row)+('{:,}'.format(doubled_cases_30days_ago)))

        if int(country_data[-1][4]) >= (doubled_cases_30days_ago) and int(country_data[-1][4]) < (quadrupled_cases_30days_ago):
            print('30-Day doubled case total? Yes      **HOT_SPOT')
        elif int(country_data[-1][4]) >= (quadrupled_cases_30days_ago):
            print('30-Day quadrupled case total? Yes *SMOKIN_HOT')
        else:
            print('30-Day case total,doubled?           NOT DOUBLED')

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
