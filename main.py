'''
>>> JAAR
>>> 09/12/2023
>>> Practicing Fundamentals Program 22
>>> Version 1
'''

'''
>>> Creates a program that asks the user to either create a new csv file or copy an existing csv file.
>>> ToDo: create functions from redundant code in main().
'''

import csv

def user_action()->int :
    '''
    >>> Asks the user to enter a number corresponding to an allowed action. If any other response is entered, the user is prompted to enter a new response.

    >>> Return: (int) action
    '''
    actions = [1, 2]
    print('''
        (1) Create new CSV.
        (2) Copy existing CSV.
    ''')
    while True :
        try :
            action = int(input('Enter response: '))
            if action not in actions :
                raise ValueError
        except ValueError :
            print('Your input was invalid.', end = '\n\t')
        else :
            return action

def user_response(question) :
    '''
    >>> Asks the user to enter either yes or no. Otherwise, prompts the user to enter a new response.
    '''
    while True :
        response = input(f'{question}: ').lower()
        if response != 'yes' and response != 'no' :
            print('Your response was invalid.', end = '\n\t')
        else :
            return response

def int_input(question)->int :
    integer = 0
    while not isinstance(integer, int) or integer < 1:
        try :
            integer = int(input(question))
        except ValueError :
            print('Your input was invalid. ', end = '\n\t')
    return integer

def main() :
    response = 'yes'
    while response == 'yes' :
        action = user_action()
        if action == 1 :
            headers = int_input('Number of headers in CSV file: ')
            headers_list = []
            for _ in range(headers) :
                headers_list.append(input('Enter Header: '))
            print(f'\nHeaders:')
            [print(f'\t{i}: {header}') for i, header in enumerate(headers_list, start = 1)]
            verify = user_response('Do you want to update a header?')
            while verify == 'yes' :
                header = ''
                while header not in range(headers) :
                    try :
                        header = int(input('Which header do you want to update?: ')) - 1
                        if header not in range(headers) :
                            raise ValueError
                    except ValueError :
                        print('Your response was invalid.', end = '\n\t')
                headers_list[header] = input('Updated header: ')
                print(f'\nUpdated headers:')
                [print(f'{i}:  {header}') for i, header in enumerate(headers_list, start = 1)]
                verify = user_response('Do you want to update another header?')
            rows = int_input('Number of rows in CSV file: ')
            csv_data = []
            for i in range(rows) :
                row = {}
                print(f'For row {i + 1}:')
                for j in range(headers) :
                    row[headers_list[j]] = input(f'\t{headers_list[j]}: ')
                # ToDo: Update to allow for user to append potential errors.
                csv_data.append(row)
            print('CSV Data:')
            [print(f'\trow {i + 1}: {key}: {row[key]}') for i, row in enumerate(csv_data) for key in row.keys()]
            # ToDo: Have the row notation printed once with the row header/value printed bellow with a single indent.
            csv_name = f"{input('Enter CSV file name: ')}.csv"
            with open(csv_name, 'w', newline = '') as new_csv :
                csv_writer = csv.DictWriter(new_csv, fieldnames = headers_list)
                csv_writer.writeheader()
                [csv_writer.writerow(row) for row in csv_data]
            print('New CSV  was created.')
        else :
            File_Error = True
            Open_Attempt = 0
            while File_Error and Open_Attempt < 5 :
                file_path = input('Enter file path: ')
                try :
                    with open(file_path, 'r', newline = '') as csv_file :
                        csv_reader = csv.DictReader(csv_file)
                        headers = csv_reader.fieldnames
                        with open('csv_copy.csv', 'w', newline = '') as csv_copy :
                            csv_writer = csv.DictWriter(csv_copy, headers)
                            csv_writer.writeheader()
                            [csv_writer.writerow(row) for row in csv_reader]
                    print('Existing CSV was copied.')
                    File_Error = False
                except FileNotFoundError :
                    Open_Attempt += 1
                    print(f"The file doesn't exist. You have {5 - Open_Attempt} left.")
                    File_Error = True
                    if Open_Attempt == 5 :
                        print('\tYou are all out of attempts!')
        response = user_response('Do you want to take another action?')
    print('DONE')

if __name__ == '__main__' :
    main()