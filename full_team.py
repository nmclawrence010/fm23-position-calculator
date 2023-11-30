import position_calculator
import csv

filename = 'csvs/brighton.csv'
uid_list = []
def get_player_uids(team_name):
    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            if team_name in row[5]:
                player_uid = row[2]
                uid_list.append(player_uid)
    #uid_list = uid_list.reverse()
    return uid_list.reverse()

def calculate_full_team():
    for item in uid_list:
        position_calculator.calculate_best_position(item, filename)


if __name__ == "__main__":
    get_player_uids("Brighton")
    calculate_full_team()
