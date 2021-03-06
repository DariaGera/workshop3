import chart_studio

chart_studio.tools.set_credentials_file(username='dariagera', api_key='T7GBkfPRVdtxOQIgxs91')
import plotly.graph_objs as go
import chart_studio.plotly as py
import cx_Oracle
import re



# ----------------------------------------------------------------------
def fileId_from_url(url):
    # Return fileId from a url
    raw_fileId = re.findall("~[A-z.]+/[0-9]+", url)[0][1:]
    return raw_fileId.replace('/', ':')


def unique_values(some_list):
    new_list = []
    new_list.append(some_list[0])
    for element in some_list:
        if element not in new_list:
            new_list.append(element)
    return new_list


def amount(some_list, town, year_list):
    new_list = []
    for year in year_list:
        for lst in some_list:
            if lst[0] == town and lst[1] == year:
                new_list += [lst[2]]
    return new_list


def insert_zero(year_list, some_list, help_list):
    for year in year_list:
        for el in some_list:
            if [el[0], year, el[2] >= 0] in help_list:
                continue
            elif [el[0], year, 0] not in all:
                some_list.append([el[0], year, 0])
    return some_list
# ------------------------------------------------------------------------

username = 'MYONLINEEDU'
password = 'oracle'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()

"""-------------------------------------------------------------------------------------
Запит 1 - вивести топ 10 міст(Township) з найменшою кількістю всіх випадків по рокам."""

query = """
SELECT
    table_1.twp,
    table_1.year,
    table_1.amount
FROM
    (
    SELECT
        twp,
        EXTRACT(YEAR FROM full_accident_table.timestamp) AS year,
        COUNT(twp) AS amount
    FROM
        full_accident_table
    GROUP BY EXTRACT(YEAR FROM full_accident_table.timestamp), twp
    ) table_1
    JOIN (
        SELECT
            twp
        FROM
            (
            SELECT
                twp,
                COUNT(twp) AS amount
            FROM
                full_accident_table
            GROUP BY twp
            ORDER BY amount ASC
        )
    WHERE
        ROWNUM < 10
    ) table_2 ON table_1.twp = table_2.twp
GROUP BY
    table_1.year, table_1.twp, table_1.amount
ORDER BY
    table_1.year, table_1.twp, table_1.amount
"""
cursor.execute(query)
print('Запит 1')
print('|Town           |year|Amount of accidents|')
print('-' * 41)

towns = []
years = []
all = []
help_all = []

row = cursor.fetchone()
while row:
    print("|{:15s}|{:2d}|{:2d}".format(row[0], row[1], row[2]))
    towns += [row[0]]
    years += [row[1]]
    all += [[row[0], row[1], row[2]]]
    help_all += [[row[0], row[1], row[2] > 0]]
    row = cursor.fetchone()

unique_town = unique_values(towns)
unique_year = unique_values(years)

all_new = all
all_new = insert_zero(unique_year, all, help_all)
print()


# Visualization of query 1st---------------------------------------------------------------------
fig = go.Figure()

fig.add_trace(go.Bar(x=unique_year,
                     y=amount(all_new, unique_town[0], unique_year),
                     name=unique_town[0],
                     marker_color='rgb(55, 83, 109)'
                     ))
fig.add_trace(go.Bar(x=unique_year,
                     y=amount(all_new, unique_town[1], unique_year),
                     name=unique_town[1],
                     marker_color='rgb(26, 118, 255)'
                     ))

fig.add_trace(go.Bar(x=unique_year,
                     y=amount(all_new, unique_town[2], unique_year),
                     name=unique_town[2],
                     marker_color='rgb(148, 0, 211)'
                     ))

fig.add_trace(go.Bar(x=unique_year,
                     y=amount(all_new, unique_town[3], unique_year),
                     name=unique_town[3],
                     marker_color='rgb(0, 0, 205)'
                     ))

fig.update_layout(
    xaxis=dict(
        title='Years',
        titlefont_size=16,
        tickfont_size=14,
    ),
    yaxis=dict(
        title='Amount of accidents',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,  # gap between bars of adjacent location coordinates.
    bargroupgap=0.1  # gap between bars of the same location coordinate.
)
query_1 = py.plot(fig, filename='accidents')



"""--------------------------------------------------------------------------------------------
Запит 2 - вивести назву ситуації в місті(Township) та частоту її виникнення(%) відносно частоти
 виникнення цієї ситуації в інших містах округа Монтгомері, Пенсильванія. (за конкретний рік)"""

query = """
SELECT
    EXTRACT(YEAR FROM full_accident_table.timestamp) AS year,
    title,
    twp,
    COUNT(twp) AS amount
FROM
    full_accident_table
WHERE
        EXTRACT(YEAR FROM full_accident_table.timestamp) =: year
    AND title =: title
GROUP BY title, twp, EXTRACT(YEAR FROM full_accident_table.timestamp)
ORDER BY twp
"""
cursor.execute(query, title='Traffic: VEHICLE ACCIDENT -', year='2019')
print('Запит 2')
print('|Year|Title                      |Town           |Amount|Percentage|')
print('-'*67)

towns = []
percentage = []

row = cursor.fetchone()
# year = row[0]
# t_tle = row[1]
# ("Accident:{:s}in town. Year{:d}".format(t_tle,year))

while row:
    print("|{:4d}|{:25s}|{:15s}|{:6d}".format(row[0], row[1], row[2], row[3]))
    towns += [row[2]]
    percentage += [row[3]]
    row = cursor.fetchone()

print()
# Visualization of query 2st---------------------------------------------------------------------
labels = towns
values = percentage
pie = go.Pie(labels = labels, values = values)
query_2 = py.plot([pie], filename='percentage')



"""--------------------------------------------------------------------------------------------
Запит 3 - вивести динаміку дзвінків(тобто ситуацій) по роках в конкретному місті. """

query = """
SELECT
    twp
    ,EXTRACT(YEAR FROM full_accident_table.timestamp) AS year
    ,COUNT(twp) AS amount
FROM full_accident_table
WHERE twp=: town
GROUP BY EXTRACT(YEAR FROM full_accident_table.timestamp), twp
ORDER BY EXTRACT(YEAR FROM full_accident_table.timestamp)
"""
# cursor.execute(query, town='WHITPAIN')
cursor.execute(query, town='first')
print('Запит 1')
print('|Town           |year|Amount of accidents|')
print('-'*41)

years = []
amount = []

row=cursor.fetchone()
while row:
    print("|{:15s}|{:4d}|{:5d}".format(row[0], row[1], row[2]))
    years += [row[1]]
    amount += [row[2]]
    row = cursor.fetchone()

print()
# Visualization of query 3st---------------------------------------------------------------------
data = go.Scatter(
    x = years,
    y = amount,
    mode='lines+markers'
)
query_3 = py.plot([data], filename='years')

cursor.close()
connection.close()
