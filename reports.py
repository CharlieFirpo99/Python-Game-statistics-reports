# Report functions
import operator

txt_file = 'game_stat.txt'


def count_games(txt_file):
    with open(txt_file, mode='r') as text_input:
        return len(text_input.readlines())

def decide(txt_file,year):
    y = str(year)
    with open(txt_file, mode='r') as text_input:
        for line in text_input:
            if y in line:
                return True
            else:
                continue
            
def get_latest(txt_file):
    list = open(txt_file).readlines()
    dict = {}
    for line in list:
        line = line.split('\t')
        dict[line[0]] = line[2]
    return max(dict.items(), key=operator.itemgetter(1))[0]

def count_by_genre(txt_file,genre):
    g = str(genre)
    i = 0
    with open(txt_file, mode='r') as text_input:
        for line in text_input:
            if g in line:
                i += 1
        return i

def get_line_number_by_title(txt_file,title):
    t = str(title)
    with open(txt_file, mode='r') as text_input:
        for num, line in enumerate(text_input, 1):
            if t in line:
                return num

def sort_abc(txt_file):
    list = open(txt_file).readlines()
    dict = {}
    for line in list:
        line = line.split('\t')
        dict[line[0]] = line[2]
    sortedTitle = sorted(dict.keys(), key=lambda x:x.lower())
    return sortedTitle

def get_genres(txt_file):
    list = open(txt_file).readlines()
    dict = {}
    nodup = {}
    for line in list:
        line = line.split('\t')
        dict[line[0]] = line[3]

    for key,value in dict.items():
        if value not in nodup.values():
            nodup[key] = value
    sortedGenres = sorted(nodup.values(), key=lambda x:x.lower())
    return sortedGenres

def when_was_top_sold_fps(txt_file):
    pass


