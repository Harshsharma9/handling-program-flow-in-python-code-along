# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

#print(data) 
 
# Code starts here

#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
def get_deliveries_faced_first_inning(batsman,data):
    count = 0
    first_inning_deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery_faced in first_inning_deliveries:
        for delivery_number,delivery_info in delivery_faced.items():
            if delivery_info['batsman'] == batsman:
                count += 1
    return count 
print(get_deliveries_faced_first_inning('SC Ganguly',data)) 

#  Who was man of the match and how many runs did he scored ?
player_of_match = data['info']['player_of_match'][0]
runs = 0
first_inning_deliveries = data['innings'][0]['1st innings']['deliveries']
for delivery_faced in first_inning_deliveries:
    for delivery_number,delivery_info in delivery_faced.items():
         if delivery_info['batsman'] == player_of_match:
            runs += (delivery_info['runs']['batsman'])

print(runs)    

#  Which batsman played in the first inning?
batsmen_list = []
first_inning_deliveries = data['innings'][0]['1st innings']['deliveries']
for delivery_faced in first_inning_deliveries:
    for delivery_number,delivery_info in delivery_faced.items():
        if delivery_info['batsman'] in batsmen_list:
            pass
        else:
            batsmen_list.append(delivery_info['batsman'])
print(batsmen_list)

# Which batsman had the most no. of sixes in first inning ?
sixes = [  ]
first_inning_deliveries = data['innings'][0]['1st innings']['deliveries']
for delivery_faced in first_inning_deliveries:
    for delivery_number,delivery_info in delivery_faced.items():
        if delivery_info['runs']['batsman'] == 6:
           sixes.append(delivery_info['batsman'])

batsman_sixes = Counter(sixes)
print(batsman_sixes)
max_value = 0
print(max(batsman_sixes,key=batsman_sixes.get))

# Find the names of all players that got bowled out in the second innings.
second_inning_bowled_out = []
second_inning_deliveries = data['innings'][1]['2nd innings']['deliveries']
for delivery_faced in second_inning_deliveries:
    for delivery_number,delivery_info in delivery_faced.items():
        try:
            if delivery_info['wicket']['kind'] == 'bowled':
               second_inning_bowled_out.append(delivery_info['batsman'])
        except:
            pass

print(second_inning_bowled_out)       



# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
extras_first_innings = [delivery_info
                        for deliveries in first_inning_deliveries
                        for delivery_number, delivery_info in deliveries.items()
                        if 'extras' in delivery_info]

extras_second_innings = [delivery_info
                        for deliveries in second_inning_deliveries
                        for delivery_number, delivery_info in deliveries.items()
                        if 'extras' in delivery_info]

difference = len(extras_second_innings) - len(extras_first_innings)
print(difference)


# Code ends here


