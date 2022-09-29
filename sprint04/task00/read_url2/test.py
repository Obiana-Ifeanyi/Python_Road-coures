
def html_save(URL, file_path):
    import re
    import requests
    from helper import print_stdout, print_stderr

    url_pattern = re.compile(r'https://w{3}.[A-Za-z0-9]+.[a-z/]+/')
    url_found = re.search(url_pattern, URL)

    if url_found:
        #the required first parameter of the 'get' method is the 'url':
        x = requests.get(URL)
        if x:
            #print (x.text)
            f = open(file_path, 'wt')
            f.write(x.text)
            f.close()

            print_stdout(f"Sending the request to the '{URL}'.")
            print_stdout(f"Request to the '{URL}' has been sent.")
            print_stdout(f"<Response [{x.status_code}]>.")
            print_stdout('Parsing page data.')
            print_stdout('Page data has been parsed.')
            print_stdout(f"Saving page data to '{file_path}'.")
            print_stdout('Page data has been saved.')


        else:
            print_stderr('Request failed')        #<module_name>.<function(x.write)>

    else:
        print_stderr('wrong URL was inputed')
