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
            if response.status_code == 404:
                print('Podaj prawidłową nazwę:')
            return response
        except requests.exceptions.HTTPError:
            print("HTTP Error:", 'Problem z połaczneniem spróbuj pożniej.')
            exit()
        except requests.exceptions.ConnectionError:
            print("Error Connecting:", 'Problem z połaczneniem spróbuj pożniej.')
            exit()
        except requests.exceptions.Timeout:
            print("Timeout Error:", 'Problem z połaczneniem spróbuj pożniej.')
            exit()
        except requests.exceptions.RequestException:
            print("Som return response.json()ething Else:", 'Problem z połaczneniem spróbuj pożniej.')


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
        if user_choice.isnumeric() or user_choice != '':
            if user_choice == '1':
                end_of_address = 'all'
                conn = Connection(Connection.start_of_address + end_of_address)
                countries = conn.get_result()
                for country in countries.json():
                    print(country['name'])
            elif user_choice == '2':
                country_name = input('Podaj nazwe państwa do wyświtlenia informacji(po angelsku): ')
                end_of_address = 'name/' + country_name.lower()
                conn = Connection(Connection.start_of_address + end_of_address)
                country_information = conn.get_result()
                if country_information.status_code == 200:
                    for information in country_information.json():
                        for key, value in information.items():
                            print(f'{key}: {value}')
            elif user_choice == '3':
                country_name = input('Podaj nazwe państwa do wyświtlenia informacji(po angelsku): ')
                end_of_address = 'name/' + country_name.lower()
                conn = Connection(Connection.start_of_address + end_of_address)
                country_information = conn.get_result()
                if country_information.status_code == 200:
                    for information in country_information.json():
                        print(f'Nazwa kraju {information["name"]}\n'
                              f'Stolica: {information["capital"]}\n'
                              f'Waluta: {information["currencies"]}\n'
                              f'Języki {information["languages"]}')
            elif user_choice == 'q':
                exit()
