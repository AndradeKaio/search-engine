from urllib.parse import urlparse


def get_domain(url):
    try:
        domain = get_sub_domain(url).split('.')
        return domain[-2]+ '.' + domain[-1]
    except:
        print("erro ao obter dominio da url.")
        return ''




def get_sub_domain(url):
    try:
        return urlparse(url).netloc
    except:
        print("erro ao obter sub dominio da url.")
        return ''


