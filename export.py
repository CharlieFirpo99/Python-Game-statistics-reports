
# Export functions
from reports import *

exp_file = 'reports.txt'

def output():
    with open(exp_file, 'w'):
        pass


def question(line):
    with open(exp_file, mode='a') as expfile:
        expfile.write(str(line) + '\n')

output()

question('How many games are in the file?:')
answer = count_games(txt_file)
question(answer)

question('Is there a game from a given year?:')
answer = decide(txt_file,2000)
question(answer)

question('Which was the latest game?:')
answer = get_latest(txt_file)
question(answer)

question('How many games do we have by genre?:')
answer = count_by_genre(txt_file,"First-person shooter")
question(answer)

question('What is the line number of the given game (by title)?:')
answer = get_line_number_by_title(txt_file,"Counter-Strike")
question(answer)

question('What is the alphabetical ordered list of the titles?:')
answer = sort_abc(txt_file)
question(answer)

question('What are the genres?:')
answer = get_genres(txt_file)
question(answer)
