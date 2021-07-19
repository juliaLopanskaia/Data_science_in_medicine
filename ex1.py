from sys import argv

script_name, hours, wager, bonus = argv

print(int(hours) * int(wager) + int(bonus))
