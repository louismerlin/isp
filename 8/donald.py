import csv
from collections import Counter

TARGET_EMAIL = 'donald.trump@whitehouse.gov' # Hope I don't get flagged by the CIA for this 😅

# Exercise 1.1

print('\033[1mExercise 1.1:\033[0m')

def reverse_find(value, appears_in, find_in, index):
    appears_in_reader = csv.reader(appears_in)
    find_in_reader = csv.reader(find_in)
    appears_in.seek(0)
    appearances = [row for row in appears_in_reader if row[index] == value]
    private_reviews_that_match = []
    for appearance in appearances:
        find_in.seek(0)
        private_reviews_that_match.append([row for row in find_in_reader if row[2] == appearance[2]])
    possible_values= [item[index] for sublist in private_reviews_that_match for item in sublist]
    found_value = max(set(possible_values), key=possible_values.count)
    return found_value

with open('anon_data/com402-1.csv', 'r') as com402, open('anon_data/imdb-1.csv', 'r') as imdb:
    donald_hash = reverse_find(TARGET_EMAIL, imdb, com402, 0)
    print('Target Hash :', donald_hash)
    com402_reader = csv.reader(com402)
    com402.seek(0)
    movie_hashes = [movie_hash for (email_hash, movie_hash, _, _) in com402_reader if email_hash == donald_hash]
    movie_titles = [reverse_find(movie_hash, com402, imdb, 1) for movie_hash in movie_hashes]
    print('Movies reviewed privately :')
    print(' | '.join(movie_titles))

# Exercise 1.2

print('\n\033[1mExercise 1.2:\033[0m')

with open('anon_data/com402-2.csv', 'r') as com402, open('anon_data/imdb-2.csv', 'r') as imdb:
    com402_reader = csv.reader(com402)
    imdb_reader = csv.reader(imdb)
    com402_list = [x for x in com402_reader]
    imdb_list = [x for x in imdb_reader]
    com402_counts = Counter([x[1] for x in com402_list]).most_common()
    imdb_counts = Counter([x[1] for x in imdb_list]).most_common()
    movie_translation = dict()
    for i in range(len(com402_counts)):
        movie_translation[com402_counts[i][0]] = imdb_counts[i][0]
    public_reviews_donald = set([movie for (email, movie, _, _) in imdb_list if email == TARGET_EMAIL])
    for email_hash in set([x[0] for x in com402_list]):
        movie_reviews = set([movie_translation[x[1]] for x in com402_list if x[0] == email_hash])
        if public_reviews_donald.issubset(movie_reviews):
            print('Target Hash :', email_hash)
            print('Movies reviewed privately :')
            print(' | '.join(movie_reviews))
            break

# Exercise 1.3

print('\n\033[1mExercise 1.3:\033[0m')

print('TODO')
