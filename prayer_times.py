import urllib3
from bs4 import BeautifulSoup


def get_prayers(): 
	http = urllib3.PoolManager()

	url = 'http://ig.internetplus.biz/prayertimes/en-countryegypt/citycairo.html'
	response = http.request('GET', url) 

	soup = BeautifulSoup(response.data.decode('utf-8'), 'html.parser')

	prayer_time_list = soup.find("div", {"style": "font-weight:bold"}).text.strip().split()
	times = prayer_time_list[5:]

	prayer_names = [times[i] for i in range(len(times)) if i %  2 == 0]
	# there's a dot in the end, remove it 
	prayer_names = prayer_names[:len(prayer_names) -1]

	# now get prayer times on 12 clock system
	prayer_times = [times[i] for i in range(len(times)) if i %  2 != 0]

	times_dict = dict() 

	for i in range(len(prayer_names)): 
		times_dict[prayer_names[i]] = prayer_times[i]


	return times_dict
