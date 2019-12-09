import requests


class Connection:

    headers = {
        'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
        'x-rapidapi-key': "ee1dd1f7ddmsh6134f2fe527589cp1fbe9ejsn3f151400b8e7"
    }

    start_of_address = "https://restcountries-v1.p.rapidapi.com/"

    def __init__(self, url):
        self.url = url

    def get_result(self):
        try:
            response = requests.get(self.url, headers=Connection.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as httpErr:
            print("Http Error:", httpErr)
        except requests.exceptions.ConnectionError as connErr:
            print("Error Connecting:", connErr)
        except requests.exceptions.Timeout as timeOutErr:
            print("Timeout Error:", timeOutErr)
        except requests.exceptions.RequestException as reqErr:
            print("Something Else:", reqErr)


if __name__ == '__main__':
    print('           Baza wiedzy na temat państw')
    while True:
        print("""
           Podaj numer zapytania do wykonia(Aby zakończyć wprowadz "q"):

           1 - Wypisze nazwy wszystkich państw z bazy.
           2 - Wypisze wszystkie inforamcje z bazy dla konkretnego państwa( w drugi kroku trzeba podać nazwe państwa)
           3 - Wypisze nazwe, stolice, walutę, jezyk dla konkretneg państwa(w drugi kroku trzeba podać nazwe państwa)
           """)
        user_choice = input(f'Podaj numer zapytania (Aby zakończyć wprowadz "q"): ')
        if user_choice.isnumeric():
            if user_choice == '1':
                end_of_address = 'all'
                conn = Connection(Connection.start_of_address + end_of_address)
                countries = conn.get_result()
                for country in countries:
                    print(country['name'])
            elif user_choice == '2':
                country_name = input('Podaj nazwe państwa do wyświtlenia informacji(po angelsku): ')
                end_of_address = 'name/' + country_name.lower()
                conn = Connection(Connection.start_of_address + end_of_address)
                country_information = conn.get_result()
                for information in country_information:
                    for key, value in information.items():
                        print(f'{key}: {value}')
            elif user_choice == '3':
                country_name = input('Podaj nazwe państwa do wyświtlenia informacji(po angelsku): ')
                end_of_address = 'name/' + country_name.lower()
                conn = Connection(Connection.start_of_address + end_of_address)
                country_information = conn.get_result()
                for information in country_information:
                    print(f'Nazwa kraju {information["name"]}\n'
                          f'Stolica: {information["capital"]}\n'
                          f'Waluta: {information["currencies"]}\n'
                          f'Języki {information["languages"]}')
        elif user_choice == 'q':
            break


