# Step 1: Read the CSV file
def read_csv(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    header = lines[0].strip().split(',')
    data = [line.strip().split(',') for line in lines[1:]]
    return header, data

header, data = read_csv('pe8_data.csv')

# Step 2: Find Eastern Conference teams with Home PCT lower than Away PCT
eastern_teams = []
for row in data:
    if row[0] == 'Eastern':
        home_record = row[7].split('-')
        away_record = row[8].split('-')
        home_pct = int(home_record[0]) / (int(home_record[0]) + int(home_record[1]))
        away_pct = int(away_record[0]) / (int(away_record[0]) + int(away_record[1]))
        if home_pct < away_pct:
            eastern_teams.append(row[1])

print("Eastern Conference teams with Home win-loss percentage lower than Away win-loss percentage:")
print(eastern_teams)

# Step 3: Calculate the average difference of PF minus PA for each conference
pf_minus_pa = {'Eastern': [], 'Western': []}
for row in data:
    conference = row[0]
    pf = float(row[5])
    pa = float(row[6])
    pf_minus_pa[conference].append(pf - pa)

average_pf_minus_pa = {conf: sum(diff) / len(diff) for conf, diff in pf_minus_pa.items()}
higher_average_conference = max(average_pf_minus_pa, key=average_pf_minus_pa.get)
print("\nConference with higher average PF minus PA:")
print(higher_average_conference)

# Step 4: Ranking teams based on performance against other conference's teams
# For demonstration purposes, we add mock inter-conference win-loss records
for row in data:
    # Mock values for inter-conference wins and losses
    inter_w = float(row[3])  # Pretend the win-loss percentage also reflects inter-conference wins
    inter_l = float(row[4])  # Pretend the games back also reflects inter-conference losses
    row.append(inter_w)
    row.append(inter_l)

# Sort teams based on inter-conference win percentage
ranked_teams = sorted(data, key=lambda x: int(x[9]) / (int(x[9]) + int(x[10])), reverse=True)

print("\nRanking of teams based on performance against other conference's teams:")
print([team[1] for team in ranked_teams])

