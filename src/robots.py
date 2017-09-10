from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser
from domain_resolver import *
# Dictionary to save parsed robots.txt files
ROBOTS = dict()

def robot_check(url):
    """Check whether we're allowed to fetch this URL from this site"""
    
    #netloc = urlparse(url).netloc
    #print(get_domain(url))
    netloc = get_domain(url)
    print(netloc)
    if netloc not in ROBOTS:
        robotsurl = urljoin(url, '/robots.txt')
        print(robotsurl)
        ROBOTS[netloc] = RobotFileParser(robotsurl)

        ROBOTS[netloc].read()

    return ROBOTS[netloc].can_fetch('*', url)

		

'''
	def robots_resolver(self, url):
		result = {"Allowed":[], "Desallowed": []}

		data = self.get_urls(url + "/robots.txt")

		user_agent = False

		for line in data.split('\n'):
			if line.startswith('User-agent'):
				if line.split(': ')[1] == '*':
					user_agent = True
				else:
					user_agent = False
			elif user_agent == True:		
				if line.startswith('Allow'):
					result['Allowed'].append(line.split(': ')[1])
				elif line.startswith('Disallow'):
					result['Desallowed'].append(line.split(': ')[1])


		return result
print(robot_check("https://desktop.github.com/"))'''