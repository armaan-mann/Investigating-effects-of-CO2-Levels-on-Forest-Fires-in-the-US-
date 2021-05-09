"""
Final Project Title: Investigating the Implications of CO2 Levels
                    on the Number of Forest Fires in the US

Objective: This file does all the data wrangling and provides
key information about how the data is stored which further uses these functions
to generate the plot and the US map.

By: Ansh Malhotra, Armaan Mann, Leya Abubaker, Gabriel Pais

This file is Copyright (c) 2020 Ansh Malhotra, Armaan Mann, Leya Abubaker, Gabriel Pais
"""

# Importing Packages
import csv
from typing import List


#############################################################################################
# The functions below are used to obtain the data from the csv files
# and form it into a dictionary.
# **Optional** you can run the code below in the console to see the extraction of the data
# 1. read_file_co is for storing the CO2 Emissions through the 'CO2_DataSet.csv'
# 2. read_file_fire is for collecting the data through 'FireData10yrs.csv'
# 3. read_file_map is for collecting the data through 'FireData5yrs.csv'
#############################################################################################
def read_file_co(filepath: str) -> dict:
    """
    Return a dictionary containing the State name and the years from 2005 to 2015.

    Preconditions:
        - filepath refers to a csv file in the format of
          "CO2_DataSet.csv"
    """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip the header
        next(reader)

        # Creates Empty Dictionary with specified keys and empty list
        extract = {"State": [], "2005": [], "2006": [],
                   "2007": [], "2008": [], "2009": [],
                   "2010": [], "2011": [], "2012": [],
                   "2013": [], "2014": [], "2015": []}
        # Appending the desired row's value into the desired the key
        for row in reader:
            extract["State"].append(row[0])
            extract["2005"].append(row[1])
            extract["2006"].append(row[2])
            extract["2007"].append(row[3])
            extract["2008"].append(row[4])
            extract["2009"].append(row[5])
            extract["2010"].append(row[6])
            extract["2011"].append(row[7])
            extract["2012"].append(row[8])
            extract["2013"].append(row[9])
            extract["2014"].append(row[10])
            extract["2015"].append(row[11])
    return extract


def read_file_fire(filepath: str) -> dict:
    """
    Return a dictionary of State and Time from the data mapped from the CSV file.

    Preconditions:
        - filepath refers to a csv file in the format of
          'FireData10yrs.csv'
    """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip the header
        next(reader)

        extract = {"State": [], "Time": []}

        # Appending the desired row's value into the desired the key
        for row in reader:
            extract["State"].append(row[4])
            extract["Time"].append(row[7])
        return extract


def read_file_map(filepath: str) -> dict:
    """
    Return a dictionary of State, Latitude, Longitude, Time, Fire Size,
    Fire Size Class, Fire Magnitude, Wind Contained, Humid Contained,
    Remoteness and Links from the data mapped from a CSV file.

    Preconditions:
        - filepath refers to a csv file in the format of
          'FireData5yrs.csv'
    """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip the header
        next(reader)

        # Creating empty locker
        extract = {"State": [], "Latitude": [], "Longitude": [],
                   "Time": [], "Fire Size": [], "Fire Size Class": [],
                   "Vegetation": [], "Fire Magnitude": [], "Wind Contained": [],
                   "Humid Contained": [], "Remoteness": [], "Links": []}

        # Appending the desired row's value into the desired the key
        for row in reader:
            extract["State"].append(row[4])
            extract["Fire Size Class"].append((row[1]))
            extract["Latitude"].append(row[2])
            extract["Longitude"].append(row[3])
            extract["Fire Size"].append(row[0])
            extract["Time"].append(row[7])
            extract["Vegetation"].append(row[8])
            extract["Fire Magnitude"].append(row[9])
            extract["Wind Contained"].append(row[10])
            extract["Humid Contained"].append(row[11])
            extract["Remoteness"].append(row[12])
            extract["Links"].append(row[13])
        return extract


################################################################################################
# get_data_fire collects the values for the y-axis of the line and the x-axis for both the
# line and bars and the values for x-axis stays the same.
#
# Below are the states and the corresponding abbreviation to be used the following functions:
# Alabama      - AL
# Alaska       - AK
# Arizona      - AZ
# Arkansas     - AR
# California   - CA
# Colorado     - CO
# Connecticut  - CT
# Delaware     - DE
# District of Columbia - DC
# Florida      - FL
# Georgia      - GA
# Hawaii       - HI
# Idaho        - ID
# Illinois     - IL
# Indiana      - IN
# Iowa         - IA
# Kansas       - KS
# Kentucky     - KY
# Louisiana    - LA
# Maine        - ME
# Maryland     - MD
# Massachusetts - MA
# Michigan      - MI
# Minnesota     - MN
# Mississippi   - MS
# Missouri      - MO
# Montana       - MT
# Nebraska      - NE
# Nevada        - NV
# New Hampshire - NH
# New Jersey    - NJ
# New Mexico    - NM
# New York      - NY
# North Carolina - NC
# North Dakota   - ND
# Ohio           - OH
# Oklahoma       - OK
# Oregon         - OR
# Pennsylvania   - PA
# Puerto Rico    - PR
# Rhode Island   - RI
# South Carolina - SC
# South Dakota   - SD
# Tennessee      - TN
# Texas          - TX
# Utah           - UT
# Vermont        - VT
# Virginia       - VA
# Washington     - WA
# West Virginia  - WV
# Wisconsin      - WI
# Wyoming        - WY
################################################################################################
def get_data_fire(state_name: str) -> List[list]:
    """
    Return the x values for the graph as a list of 'YYYY'.
    Return the y values for the line points in the graph as list.

    The x values represent the years from 2005 to 2015.
    The y values represent the list of each years fire frequencies for that particular
    state.

    Preconditions:
        - len(state_name) == 2
        - all(str.isupper(i) for i in state_name)
        - state_name should match the given corresponding state abbreviation
        from the given list above.
    """
    extract_fire = read_file_fire("FireData10yrs.csv")
    # Initializing Variables
    x_years = ['2005']
    y_num_forest_fire = []
    fire_frequency = 0
    year1 = '2005'
    # Iterating through the Dictionary
    for i in range(0, len(extract_fire['State'])):
        # Compares the provided state with each state in the data
        if state_name == extract_fire["State"][i]:
            # If the year equals the year in the data, it does the following:
            if year1 != extract_fire["Time"][i]:
                year1 = extract_fire["Time"][i]
                list.append(y_num_forest_fire, fire_frequency)
                list.append(x_years, year1)
                fire_frequency = 0
                fire_frequency = fire_frequency + 1
            # Otherwise, it runs this:
            else:
                fire_frequency = fire_frequency + 1

    list.append(y_num_forest_fire, fire_frequency)
    return [x_years, y_num_forest_fire]


################################################################################################
# The function collects the values for the y-axis of the bars within the graph.
# The values of the y-axis of the bars are on the left side.
# One bar is storing values for the cars and the other is for the trucks
################################################################################################
def get_data_co2(state_name: str) -> list:
    """
    Return the y values for the bars in the graph of the co2 emissions.

    The y values represent CO2 emissions produced by each state from teh years 2005 to 2015.

    Preconditions:
        - len(state_name) == 2
        - all(str.isupper(i) for i in state_name)
        - state_name should match the given corresponding state abbreviation
        from the given list above and the function above.
    """
    extract_co2 = read_file_co("CO2_DataSet.csv")

    co2_year_by = []

    for i in range(len(extract_co2['State'])):
        if state_name == str(extract_co2['State'][i]):
            x = list.index(extract_co2['State'], str(extract_co2['State'][i]))
            list.append(co2_year_by, float(extract_co2['2005'][x]))
            list.append(co2_year_by, float(extract_co2['2006'][x]))
            list.append(co2_year_by, float(extract_co2['2007'][x]))
            list.append(co2_year_by, float(extract_co2['2008'][x]))
            list.append(co2_year_by, float(extract_co2['2009'][x]))
            list.append(co2_year_by, float(extract_co2['2010'][x]))
            list.append(co2_year_by, float(extract_co2['2011'][x]))
            list.append(co2_year_by, float(extract_co2['2012'][x]))
            list.append(co2_year_by, float(extract_co2['2013'][x]))
            list.append(co2_year_by, float(extract_co2['2014'][x]))
            list.append(co2_year_by, float(extract_co2['2015'][x]))
    return co2_year_by


################################################################################################
# Helper Function: collects the y-values for the entire US plot.
# **Optional** You can run this if you like, this just shows the total number of forest fires
# per year of each state.
################################################################################################
def total_fire() -> list:
    """
    Return a list of y-values per year.

    y-values represent the total forest fires happened per year from 2005 to 2015.
    The y-values are for the entire US.
    """
    year = '2005'
    y_value = []
    freq = 0
    extract = read_file_fire("FireData10yrs.csv")

    for x in extract["Time"]:

        if x != year:
            list.append(y_value, freq)
            freq = 0
            year = x
            freq += 1
        else:
            freq += 1

    list.append(y_value, freq)
    return y_value


if __name__ == '__main__':
    # import python_ta
    #
    # python_ta.check_all(config={
    #     'allowed-io': ['graph_data', 'read_file_2', 'read_file_fire',
    #                    'read_file_co', 'read_file_map'],
    #     'extra-imports': ['python_ta.contracts', 'csv', 'datetime',
    #                       'plotly.graph_objects', 'plotly.subplots', 'numpy',
    #                       'matplotlib.pyplot'],
    #     'max-line-length': 100,
    #     'max-args': 6,
    #     'max-locals': 25,
    #     'disable': ['R1705'],
    # })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = True
    python_ta.contracts.check_all_contracts()
