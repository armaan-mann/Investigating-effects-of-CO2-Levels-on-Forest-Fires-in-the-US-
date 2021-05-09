"""
Part 2: Visual Representation of the Forest Fires in US (2005 - 2015)
Objective: In this file, the plot of the relationship between CO2 Emissions
and the forest fires using the Bar Graph with Line.
The file gives you two options:
    - You can look at the relationship between the CO2 Emissions and
    the forest fires per state.
    - You can also look at the relationship between CO2 Emission and
    the forest fires of the whole US.

This file is Copyright (c) 2020 Ansh Malhotra, Armaan Mann, Leya Abubaker, Gabriel Pais
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots
from main import get_data_co2, get_data_fire, total_fire


################################################################################################
# state_plot creates the bar plot with line.
# It combines all the information from the functions:
# get_data_co2 and get_data_fire from main.py
################################################################################################
def state_plot(state_name: str) -> None:
    """
    Plot the Bar Chart with Line using the x-values and y-values obtained from the
    functions: get_data_co2, get_data_fire from the main.py.

    Preconditions:
        - len(state_name) == 2
        - all(str.isupper(i) for i in state_name)
        - state_name should match with the function call of get_data_fire().
    """

    fire = get_data_fire(state_name)
    x_years = fire[0]
    y_num_forest_fire = fire[1]
    co2_year_by = get_data_co2(state_name)

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Adding the Bar graph
    fig.add_trace(
        go.Bar(x=x_years, y=co2_year_by, name="CO2 Emissions"),
        secondary_y=False,
    )
    # Adding the Line graph
    fig.add_trace(
        go.Scatter(x=x_years, y=y_num_forest_fire, name="Number of Forest Fires"),
        secondary_y=True,
    )

    # Set x-axis title
    fig.update_xaxes(title_text="<b>Years<b>")

    # Set y-axes titles
    fig.update_yaxes(
        title_text="<b>CO2 Emissions in <b> " + state_name + "<b>per year (g/mi)</b>",
        secondary_y=False
    )
    fig.update_yaxes(
        title_text="<b>Number of Forest Fires in </b> " + state_name + " <b> per year <b>",
        secondary_y=True
    )

    # Add figure title
    fig.update_layout(
        title_text="Relationship Between C02 Emission in " + state_name + " and Forest Fire"
    )

    fig.show()


###################################################################################
# For the US plot: represents the total CO2 emissions by year
# from 2005 to 2015.
###################################################################################
united_states = [5991.4, 5910.8, 6001.1, 5811.6, 5387.4, 5585.6,
                 5446.4, 5236.9, 5362.5, 5413.5, 5267.1]


def entire_plot() -> None:
    """
    Plot the Bar Chart with Line using the y-values obtained from the helper
    function: total_fire() from the main.py.
    """
    # Using the functions above to generate these and be able to use them in the plot.
    x_years = [2005, 2006, 2007, 2008, 2009,
               2010, 2011, 2012, 2013, 2014, 2015]
    y_fire = total_fire()
    co2_total = united_states

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    # Adding the Bar graph
    fig.add_trace(
        go.Bar(x=x_years, y=co2_total, name="CO2 Emissions",
               marker=dict(color='rgb(51, 34, 138)')),
        secondary_y=False,
    )
    # Adding the Line graph
    fig.add_trace(
        go.Scatter(x=x_years, y=y_fire, name="Number of Forest Fires",
                   marker=dict(color='#22FFA7')),
        secondary_y=True,
    )

    # Set x-axis title
    fig.update_xaxes(title_text="<b>Years<b>")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>CO2 Emissions per year (g/mi)</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b> Number of Forest Fires of all US </b>", secondary_y=True)

    # Add figure title
    fig.update_layout(
        title_text="Relationship Between C02 Emission of entire US and Forest Fire"

    )
    fig.show()


##################################################################################
# The function below are for checking the trends of the CO2 Emissions with the
# forest fires for each state as well as the trends of the CO2 Emissions with the
# entire US.
# 1. check_trend checks the trends for each state.
# 2. check_trend_all checks the trends for the entire US.
##################################################################################
def check_trend(state_name: str) -> str:
    """
    Return a message if it follows the trend or not.

    Our predicted trend is if there is a increase in CO2 emissions then
    there will also be increase in forest fires per state.

    Preconditions:
        - len(state_name) == 2
        - str.isupper(state_name)
    """

    co2_y = get_data_co2(state_name)
    fire_y = get_data_fire(state_name)[1]

    max_co2 = max(co2_y)
    max_fire = max(fire_y)

    if list.index(co2_y, max_co2) == list.index(fire_y, max_fire):
        return 'Follows trend, hypothesis is correct'

    else:
        return 'Does not follow trend, hypothesis is incorrect'


def check_trend_all() -> str:
    """"
    Return a message if it follows the trend or not.

    Our predicted trend is if there is a increase in CO2 emissions then
    there will also be increase in forest fires for teh entire US.
    """
    co2_y = united_states
    fire_y = total_fire()

    max_co2 = max(co2_y)
    max_fire = max(fire_y)

    if list.index(co2_y, max_co2) == list.index(fire_y, max_fire):
        return 'Follows trend, hypothesis is correct'

    else:
        return 'Does not follow trend, hypothesis is incorrect'


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'allowed-io': ['graph_data', 'read_file_2', 'read_file_fire',
                       'read_file_co', 'read_file_map', 'get_data_co2',
                       'get_data_fire', 'total_fire', "main"],
        'extra-imports': ['python_ta.contracts', 'csv', 'datetime',
                          'plotly.graph_objects', 'plotly.subplots', 'numpy',
                          'plotly', 'main'],
        'max-line-length': 100,
        'max-args': 6,
        'max-locals': 25,
        'disable': ['R1705'],
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = True
    python_ta.contracts.check_all_contracts()
