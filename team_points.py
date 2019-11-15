from csv import reader

opened_file = open('data_files/nhl_team_stats.csv')
read_file = reader(opened_file)
stats = list(read_file)
stats_header = stats[0]
stats = stats[1:]


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(row)
        print('\n')  # adds a new (empty) line between rows

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))


# print(stats_header)
# print('\n')
# explore_data(stats, 0, 3, True)
print(stats_header)
print('\n')


def team_data(team):
    array = []
    for name in stats:
        if name[1] == team:
            array.append(name)
    return array

team_freq = {}

for row in stats:
    team = row[1]
    if team in team_freq:
        team_freq[team] += 1
    else:
        team_freq[team] = 1
print(team_freq)

def total_goals(year):
    goals = 0
    for name in stats:
        if name[2] == year:
            goals += float(name[11])
    return goals

print(total_goals("2018-19"))




