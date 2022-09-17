def summary(filename, summarize_by):
    from collections import Counter
    import json

    try:
        # open the file
        with open(filename) as f:
            # parse filename
            loaded_json = json.load(f)

            for i in loaded_json:
                for key, value in i.items():
                    if key == summarize_by:
                        '''
                        if value is None:
                            cnt[None] += 1

                        elif hash(value) is False:
                            cnt['unhashable'] += 1'''

                        count_value = dict(Counter(value))
                        print (count_value)

                    else: # key != summarize_by or summarize not in i.keys()
                        cnt[None] += 1

            loaded_json.close()


    except FileNotFoundError:
        return f'Error in decoding JSON.'

        #summary_dict = {}
        #summary_dict[summarize_by] = count
        #return summary_dict
