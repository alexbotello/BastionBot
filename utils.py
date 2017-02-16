import requests
from bs4 import BeautifulSoup
from overwatch import Overwatch


def get_average_stats(battletag):
    """Gather average Overwatch Stats for Bastion Bot"""

    average = Overwatch(battletag=battletag, mode='quickplay',
                        filter='featured')
    results = average.get_results()
    descr, stats = parse(results)

    for i in range(len(descr)):
        yield descr[i], stats[i]


def get_average_comp(battletag):
    """ Gather average competitive Overwatch stats """

    average = Overwatch(battletag=battletag, mode='competitive',
                        filter='featured')
    results = average.get_results()
    descr, stats = parse(results)

    for i in range(len(descr)):
        yield descr[i], stats[i]


def get_most_stats(battletag):
    """ Gather most in game/best Overwatch stats """

    most = Overwatch(battletag=battletag, mode='quickplay', hero='all',
                     filter='best')
    results = most.get_results()
    descr, stats = parse(results)

    for i in range(len(descr)):
        yield descr[i], stats[i]


def get_most_comp(battletag):
    """ Gather most in game/best competitive Overwatch stats """

    most = Overwatch(battletag=battletag, mode='competitive', hero='all',
                     filter='best')
    results = most.get_results()
    descr, stats = parse(results)

    for i in range(len(descr)):
        yield descr[i], stats[i]


def most_played(battletag):
    """ Gather the data for heroes most played """

    play = Overwatch(battletag=battletag, mode='quickplay', hero='all',
                     filter='played')
    results = play.get_results()
    descr, stats = parse(results)

    for i in range(len(descr)):
        yield descr[i], stats[i]


def most_played_comp(battletag):
    """ Gather the data for heroes most played in comp """

    play = Overwatch(battletag=battletag, mode='competitive', hero='all',
                     filter='played')
    results = play.get_results()
    descr, stats = parse(results)

    for i in range(len(descr)):
        yield descr[i], stats[i]


def get_hook(battletag):
    """ Gathers those mad hook stats"""

    roadhog = Overwatch(battletag=battletag, mode='quickplay', hero='roadhog',
                        filter='hero specific')
    results = roadhog.get_results()
    descr, stats = parse(results)

    for i in range(len(descr)):
        yield descr[i], stats[i]


def get_dva(battletag):
    """ Gather Dva Self-Destruct Stats"""

    dva = Overwatch(battletag=battletag, mode='quickplay', hero='dva',
                    filter='miscellaneous')
    results = dva.get_results()
    descr, stats = parse(results)

    for i in range(len(descr)):
        yield descr[i], stats[i]

def get_sr(battletag):
    """ Grabs Skill Rating Image URL"""

    response = requests.get('https://playoverwatch.com/en-us/career/pc/us/' + battletag.replace("#", '-'))
    soup = BeautifulSoup(response.content, 'html.parser')
    block = soup.find('div', {'class': 'competitive-rank'})
    image = block.find('img')['src']
    return image



def parse(value_list):
    """ Separates data from a list and returns two lists """
    text = []
    nums = []
    length = len(value_list)
    # Separate all text into a new list
    for i in range(0, length, 2):
        text.append(value_list[i])
    # Separate all numbers into a new list
    for j in range(1, length, 2):
        nums.append(value_list[j])

    return text, nums
