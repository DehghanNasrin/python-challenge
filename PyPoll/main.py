import os
import csv


def election_analysis():

    csvPath = os.path.join('Resources', 'election_data.csv')
    total_votes = 0
    candidates = {}

    with open(csvPath) as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')

        next(csvReader)
        for row in csvReader:
            total_votes += 1
            candidate_name = row[2]
            if candidate_name not in candidates:
                candidates.update({candidate_name: 1})
            else:
                candidates[candidate_name] += 1

    print('Election Results')
    print('----------------------------')
    print(f'Total Votes: {total_votes}')
    print('----------------------------')

    winner = ""
    greatest_votes = 0
    for cand in candidates.keys():
        percentage = (candidates[cand] / total_votes)
        print(f'{cand}:', '{:.3%}'.format(percentage), f'({candidates[cand]})')
        if candidates[cand] > greatest_votes:
            greatest_votes = candidates[cand]
            winner = cand
    print('----------------------------')
    print(f'Winner: {winner}')
    print('----------------------------')

    csvwriter = open('analysis\\analysis.txt', 'w')

    print('Election Results', file= csvwriter)
    print('----------------------------', file= csvwriter)
    print(f'Total Votes: {total_votes}', file= csvwriter)
    print('----------------------------', file= csvwriter)

    winner = ""
    greatest_votes = 0
    for cand in candidates.keys():
        percentage = (candidates[cand] / total_votes)
        print(f'{cand}:', '{:.3%}'.format(percentage), f'({candidates[cand]})', file=csvwriter)
        if candidates[cand] > greatest_votes:
            greatest_votes = candidates[cand]
            winner = cand
    print('----------------------------', file= csvwriter)
    print(f'Winner: {winner}', file= csvwriter)
    print('----------------------------', file= csvwriter)


election_analysis()
