from os import system, name
import csv
from typing import List, Dict, Any, Optional, Union

def clear_screen():
    #windows
    if name == 'nt':
        _ = system('cls')
    #mac and linux
    else:
        _ = system('clear')

#region dataset_tools
def read_dataset(path: str) -> List[Dict[str, any]]:
    '''
    Reads the dataset from the given path into a list of dictionaries.
    '''

    newlist = []
    with open(path, 'r') as file:
        csvFile = csv.DictReader(file)

        for row in csvFile:
            # Convert values, so we can calculate with them.
            row['Performance'] = float(row['Performance'])
            row['FoundationYear'] = int(row['FoundationYear'])
            row['Environment'] = int(row['Environment'])
            row['Social'] = int(row['Social'])
            row['Governance'] = int(row['Governance'])

            newlist.append(row)

    return newlist


def print_dataset(dataset):
    '''
    Prints out a table with the stocks in the given dataset.
    '''

    print('ID    |  Performance    |  Industry        |  Foundation Year   |  Environment    |  Social    |  Governance    |')
    print('------|-----------------|------------------|--------------------|-----------------|------------|----------------|')
    
    for stock in dataset:
        for stock_property in stock:
            #The industry property needs extra space for the long words like: 'entertainment' and 'electronics'
            if stock_property == 'Industry': 
                spaces: int = len(stock_property) + 8
            else:
                spaces: int = len(stock_property) + 4
            spaces = spaces-len(str(stock[stock_property]))

            print(stock[stock_property], end=f'{spaces * " "}|  ')

        print('')
#endregion


#region dataset_modification
def get_best_performing(dataset: List[Dict[str, str]], top_amount: int) -> List[Dict[str, str]]:
    '''
    Returns a list with length of top_amount of the best performing stocks in decending order.
    '''

    top_list: List[Dict[str, str]] = []
    stock_dataset = dataset.copy()

    # Let the user know if there are not enough stocks still in the dataset after the aplied inputs.
    if len(stock_dataset) < top_amount:
        print('There are not enough stocks in the dataset for the specified requirements\n')
        print(f'There are {len(stock_dataset)} stocks, with given input number: {top_amount}\n')
        top_amount = len(stock_dataset)


    for amount in range(top_amount):
        highest_performance: float = float('-inf')
        highest_stock: Dict[str, str] = None

        # Get the highest performing stock.
        for stock in stock_dataset:
            if stock['Performance'] > highest_performance:
                highest_performance = stock['Performance']
                highest_stock = stock
        
        # Add the highest performing stock to the list and remove it from the databese, so it cannot be chosen again.
        top_list.append(highest_stock)
        stock_dataset.remove(highest_stock)

    return top_list

def get_stocks_from_industry(dataset: List[Dict[str, str]], industry) -> List[Dict[str, str]]:
    '''
    Returns a list of all the stocks in the current dataset from the given industry.
    '''

    stock_list = []

    for stock in dataset:
        if stock['Industry'] == industry:
            stock_list.append(stock)

    return stock_list

def get_below_establishment_year(dataset: List[Dict[str, str]], establishment_year: int) -> List[Dict[str, str]]:
    '''
    Returns a list of all stocks in the current dataset that were founded before the given establishment_year.
    '''

    stock_list = []
    
    for stock in dataset:
        if stock['FoundationYear'] <= establishment_year:
            stock_list.append(stock)

    return stock_list

def get_above_ESG_criteria(dataset: List[Dict[str, str]], ESG_criteria: List[int]) -> List[Dict[str, str]]:
    '''
    Returns a list of all the stocks in the current dataset that have scores above the given ESG_criteria.
    '''

    stock_list = []

    for stock in dataset:
        if stock['Environment'] >= ESG_criteria[0] and stock['Social'] >= ESG_criteria[1] and stock['Governance'] >= ESG_criteria[2]:
            stock_list.append(stock)

    return stock_list
#endregion


#region user_input
def ask_user_amount() -> int:
    '''
    Asks the user the amount of stocks he wants in the list and returns it.
    '''

    while True:
        try:
            amount_best_stocks = int(input("How many best stocks do you want (1-100)?\n").strip())

            if amount_best_stocks > 100 or amount_best_stocks <= 0:
                clear_screen()
                print("Input number must be between 1 and below 100")
            else:
                return amount_best_stocks
        
        except ValueError as e:
            clear_screen()
            print('Input must be of type integer.')
        
def ask_user_industry() -> str:
    '''
    Asks the user from what industry he wants the stocks and returns the given industry.
    '''

    want_industry = input('Do you want to specify the industry (yes/no)?\n').strip().lower()
    if want_industry == 'yes' or want_industry == 'y':
        clear_screen()
        print('Available industries: agriculture, clothing, construction, electronics, energy, entertainment, mining.')
        industry_input = input('What is the industry you are looking for?\n').strip().lower()

        if industry_input not in ['agriculture', 'clothing', 'construction', 'electronics', 'energy', 'entertainment', 'mining']:
            print('Invalid industry given.')
            return ask_user_industry()

        return industry_input
    
    return ''

def ask_user_establishment_year() -> int:
    '''
    Asks the user below which establishment year it wants the stocks to be and returns it.
    '''

    want_establishment_year_input = input('Do you want to specify the establishment year (yes/no)?\n').strip().lower()

    if want_establishment_year_input == 'yes' or want_establishment_year_input == 'y':
        
        print('')
        while True:
            try:
                establishment_year_input = int(input("What is the establishment year you are looking for (1800-2020)?\n").strip())

                if establishment_year_input > 2020 or establishment_year_input < 1800:
                    clear_screen()
                    print("Input number must be above 1800 and below 2020")
                else:
                    return establishment_year_input
                
            except ValueError as e:
                clear_screen()
                print('Input must be of type integer.')
    else:
        return -1
    
def ask_user_ESG_criteria() -> List[int]:
    '''
    Asks the user what ESG criteria he wants and returns the given values in a list.
    '''

    want_ESG_criteria = input('Do you want to specify the Environment, Social and Governance scores (yes/no)?\n').strip().lower()

    if want_ESG_criteria == 'yes' or want_ESG_criteria == 'y':
        
        print('')
        while True:
            try:
                environment_score_input = int(input("What is the minimal score you are looking for in Environment (0-10)?\n").strip())
                print('')
                social_score_input = int(input("What is the minimal score you are looking for in Social (0-10)?\n").strip())
                print('')
                governance_score_input = int(input("What is the minimal score you are looking for in Governance (0-10)?\n").strip())

                for score in [environment_score_input, social_score_input, governance_score_input]:
                    if score > 10 or score < 0:
                        clear_screen()
                        print("Input number must be above 0 and below 10")
                        continue

                return [environment_score_input, social_score_input, governance_score_input]
                
            except ValueError as e:
                clear_screen()
                print('Input must be of type integer.')
    else:
        return []
#endregion


def setup_user_input():
    '''
    Calls all the user input functions and stores their values.
    '''

    clear_screen()
    amount_stocks = ask_user_amount()

    clear_screen()
    wanted_industry = ask_user_industry()

    clear_screen()
    wanted_establishment_year = ask_user_establishment_year()

    clear_screen()
    wanted_ESG_criteria = ask_user_ESG_criteria()

    create_final_stock_list(amount_stocks, wanted_industry, wanted_establishment_year, wanted_ESG_criteria)


def create_final_stock_list(amount_stocks, wanted_industry, wanted_establishment_year, wanted_ESG_criteria):
    '''
    Creates and modifies the dataset to the given input criteria.
    '''

    dataset = read_dataset('stocks.csv')

    if wanted_industry != '':
        dataset = get_stocks_from_industry(dataset, wanted_industry)
        
    if wanted_establishment_year != -1:
        dataset = get_below_establishment_year(dataset, wanted_establishment_year)
    
    if wanted_ESG_criteria != []:
        dataset = get_above_ESG_criteria(dataset, wanted_ESG_criteria)

    # Change settings if there are no stocks in the list and rerun this function
    if len(dataset) == 0:
        clear_screen()
        
        print('The input criteria was too strict, there are no such stocks in the dataset.')
        print('Therefore the we have changed the criteria.\n')

    
        if wanted_establishment_year != -1:
            print('The establishment year has been set to 1950.')
            wanted_establishment_year = 1950

        if wanted_ESG_criteria != []:
            print('The Environment, Social and Governance scores have all been set to a minimum of 6.')
            wanted_ESG_criteria = [6, 6, 6]

        print('')

        dataset = read_dataset('stocks.csv')
        
        return create_final_stock_list(amount_stocks, wanted_industry, wanted_establishment_year, wanted_ESG_criteria)


    dataset = get_best_performing(dataset, amount_stocks)

    print_dataset(dataset)


if __name__ == '__main__':
    setup_user_input()
