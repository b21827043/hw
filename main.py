#Foreign exchange rates API with currency conversion

import sys
import requests

def requestFunc(url):
    get_request = requests.get(url)
    return get_request.json()

if len(sys.argv) == 2:
    try: 
        request1 = requestFunc("https://api.exchangeratesapi.io/latest?base="+sys.argv[1])
        int1 = 0         
        for currency,rate in request1["rates"].items():
            print(currency,rate)
            int1 += 1
            if int1 == 10 :
                break
    except requests.exceptions.ConnectionError:
        print("Ağınızda bir problem var.")
    except:
        print('Programı " python3 main.py -[currency] " şeklinde çalıştırın. Örnek : python3 main.py USD')
elif len(sys.argv) == 3:
    if len(sys.argv[1]) == 3:
        try: 
            request2 = requestFunc("https://api.exchangeratesapi.io/latest?base=USD")
            ratio = request2["rates"][sys.argv[1]]/request2["rates"][sys.argv[2]]
            print(ratio)
        except requests.exceptions.ConnectionError:
            print("Ağınızda bir problem var.")
        except:
            print('Programı " python3 main.py -[currency1] -[currency2] " şeklinde çalıştırın. Örnek : python3 main.py TRY USD')
    else:
        try:
            request3 = requestFunc("https://api.exchangeratesapi.io/"+sys.argv[1]+"?base="+sys.argv[2])
            for currency,rate in request3["rates"].items():
                print(currency,rate)
        except requests.exceptions.ConnectionError:
            print("Ağınızda bir problem var.")
        except:
            print('Programı " python3 main.py -[date(Y-M-D)] -[currency] "  şeklinde çalıştırın. Örnek : python3 main.py 2010-10-10 USD')

else : 
    print("""	Girdiğiniz para biriminin anlık diğer para birimlerine oranı için: 
Programı " python3 main.py -[currency] " şeklinde çalıştırın. Örnek : python3 main.py USD
	2 Para biriminin birbirlerine oranları için:
Programı " python3 main.py -[currency1] -[currency2] " şeklinde çalıştırın. Örnek : python3 main.py TRY USD
	Girdiğiniz para biriminin istediğiniz tarihteki diğer para birimlerine oranı için :  
Programı " python3 main.py -[date(Y-M-D)] -[currency] "  şeklinde çalıştırın. Örnek : python3 main.py 2010-10-10 USD
          """)
