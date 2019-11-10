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
        print('\n') # adds a new (empty) line between rows
        
    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))

# print(stats_header)
# print('\n')
# explore_data(stats, 0, 3, True)
print(stats_header)
print('\n')
for team in stats:
    name = team[1]
    if name == 'Detroit Red Wings':
        
        print(team)

# print(stats[1:5])