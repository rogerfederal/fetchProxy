import requests
import json


def check(alive, proxy, apiurl, sema, timeout, testurl):
    try:
        r = requests.get(url=apiurl + '/proxies/' + str(proxy['name']) + '/delay?url='+testurl+'&timeout=' + str(timeout), timeout=10)
        print('\n r ='+str(r))
        response = json.loads(r.text)
        print('\nresponse' + str(response))
        if response['delay'] > 0:
            print('\nproxy' + str(proxy))
            alive.append(proxy)
    except:
        pass
    bar.update(1)
    sema.release()
