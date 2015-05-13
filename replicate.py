import requests, vlermv

DIR = '~/.spacestatus'

@vlermv.cache(DIR, 'directory')
def get_directory(date):
    url = 'http://spacestatus.bastinat0r.de/spaces/_design/all/_view/json'
    return requests.get(url)

@vlermv.cache(DIR, 'hackerspace')
def get_hackerspace(date, name):
    dt = datetime.datetime.fromordinal(date.toordinal()).timestamp()
    url = 'http://spacestatus.bastinat0r.de/%s/_design/space/_view/all?endkey=%f'
    return requests.get(url % (name, dt))

def main():
    import sys, csv, datetime
    today = datetime.date.today()
    for hackerspace in get_directory(today):
        for reading in get_hackerspace(hackerspace, today):
            pass

if __name__ == '__main__':
    main()
