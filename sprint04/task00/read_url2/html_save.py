'''
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
'''






'''

def html_save(URL, file_path):
    import re
    import requests
    from helper import print_stdout, print_stderr

    found1 = re.search(r'https://w{3}.[A-Za-z0-9]+.[a-z/]+/', URL)
    found2 = re.search('https://[a-zA-Z0-9.]+', URL)
    found3 = re.search('http://[a-zA-Z0-9.:/]+', URL)



    if found1 or found2 or found3:
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
            try:
                print_stdout(f"Sending the request to the '{URL}'.")
                print_stdout(f"Request to the '{URL}' has been sent.")
                print_stdout(f"<Response [{x.status_code}]>.")
                print_stderr('Request failed')

            except:
                print_stdout(f"Sending the request to the '{URL}'.")
                print_stderr('an error just occured')

            except TimeoutError as a:
                print (a)
                print_stdout(f"Sending the request to the '{URL}'.")
                print_stderr('an error just occured')

            except urllib3.exceptions.NewConnectionError as e:
                print (e)
                print_stdout(f"Sending the request to the '{URL}'.")
                print_stderr('an error just occured')


            except urllib3.exceptions.MaxRetryError as i:
                print (i)
                print_stdout(f"Sending the request to the '{URL}'.")
                print_stderr('an error just occured')


            except requests.exceptions.ConnectionError as o:
                print (o)
                print_stdout(f"Sending the request to the '{URL}'.")
                print_stderr('an error just occured')


    else:
        print_stderr('wrong URL was inputed')



'''




def html_save(URL, file_path):
    import re
    import requests
    from helper import print_stdout, print_stderr

    found1 = re.search(r'https://w{3}.[A-Za-z0-9]+.[a-z/]+/', URL)
    found2 = re.search('https://[a-zA-Z0-9.]+', URL)
    found3 = re.search('http://[a-zA-Z0-9.:/]+', URL)



    if found1 or found2 or found3:
        #the required first parameter of the 'get' method is the 'url':



        try:
            x = requests.get(URL)
            #x.raise_for_status()

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
                print_stdout(f"Sending the request to the '{URL}'.")
                print_stdout(f"Request to the '{URL}' has been sent.")
                print_stdout(f"<Response [{x.status_code}]>.")
                print_stderr('Request failed')

        except requests.exceptions.RequestException as zex:
            print_stdout(f"Sending the request to the '{URL}'.")
            print_stderr(zex)


    else:
        print_stderr('The site URL format is invalid.')

