import csv


def read_table_file(year):
    table_file = f'{year}_table.csv'
    with open(table_file) as f:
        reader = csv.DictReader(f)
        table_list = []
        for row in reader:
            table_list.append(row['Team'])
        return table_list


def clean_results_file(year):
    # Replace 1st column with 1st row
    results_file = f'{year}_results.csv'
    with open(results_file) as f:
        reader = csv.reader(f)
        team_names = next(reader)
        results_by_team_list = [team_names]
        i = 0
        for row in reader:
            i += 1
            team_names[i] = row[0]
            results_by_team_list.append(row)
        return results_by_team_list


def calculate_rating(table, overall_results):
    # column_names = results.pop(0)
    # df = pd.DataFrame(results, columns=column_names)
    opponents = overall_results.pop(0)
    i = 0
    competition_rating = 0
    for team in overall_results:
        team_results = overall_results[i]
        i += 1
        opponent_index = 0
        team_name = team_results[0]
        for result in team_results:

            if not result or result in opponents:
                opponent_index += 1
                continue

            split_result = result.split('-')
            # If opponents higher in league table
            if table.index(opponents[opponent_index]) < table.index(team_name):
                if split_result[0] > split_result[1]:
                    competition_rating += 3
                elif split_result[0] == split_result[1]:
                    competition_rating += 1
            opponent_index += 1
    # Divide by number of games per season
    return round(competition_rating/380, 2)


def main():
    # For each result add the points given to the competitiveness rating and then divide by number of games
    seasons = ['2013', '2014', '2015', '2016', '2017', '2018', '2019']
    for season in seasons:
        table = read_table_file(season)
        results = clean_results_file(season)
        rating = calculate_rating(table, results)
        print(f'Competitiveness Rating for season ending {season} is {rating}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

