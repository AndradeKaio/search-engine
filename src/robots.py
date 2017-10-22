from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser
from domain_resolver import *
# Dictionary to save parsed robots.txt files
ROBOTS = dict()

def robot_check(url):
    """Check whether we're allowed to fetch this URL from this site"""
    netloc = urlparse(url).netloc
    
    #netloc = get_domain(url)
    #print(netloc)
    if netloc not in ROBOTS:
        robotsurl = urljoin(url, '/robots.txt')
        #print(robotsurl)
        ROBOTS[netloc] = RobotFileParser(robotsurl)

        ROBOTS[netloc].read()

    return ROBOTS[netloc].can_fetch('*', url)