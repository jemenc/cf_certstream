import re

def compare_string(key:str=None,url:str=None):
    if key:
        try:
            re.search(str(key),string=url).group()
        except:
            return False
        else:
            return True
    else:
        False

def compare_message(value:dict=dict(),keywords:list=list()) -> tuple|bool:
    url_value = value.get('domains')[0]
    if url_value:
        find_match = [(url_value,key) for key in keywords if compare_string(key=key,url=url_value) ]
        return find_match if len(find_match) > 0 else False
    else:
        return False
    


if __name__ == "__main__":
    result = {'domains': ['docker-s8b4.onrender.com', 'sni.cloudflaressl.com'], 'issuer': 'Cloudflare, Inc.', 'not_after': 'Sat Aug 24 18:59:59 2024', 'not_before': 'Fri Aug 25 19:00:00 2023'}
    keywords = ['abc','cde','ender','dock']

    compare = compare_message(value=result,keywords=keywords)
    print(compare)