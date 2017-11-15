#!/usr/bin/env python3
# This program searches the "news" database and prints out 3 Reports
# 1. What are the most popular three articles of all time?
# 2. Who are the most popular article authors of all time?
# 3. On which days did more than 1% of requests lead to errors?
# All report functions are named after report number.
# Added Header and Footer for readablity if report is run more than once.
# Paul Griz 11/15/17

import psycopg2

# Header
print("""\n
--------------------------------------------------
     The Requested Reports Are Listed Below
--------------------------------------------------\n\n""")
# Prints all reports after they are produced.
def all_reports():
    # Prints out all reports in order.
    # All the data is passed through data_fromSQL_clean function first
    db = psycopg2.connect(dbname="news")
    cur = db.cursor()

    print("1.) The 3 Most Viewed Articles:\n")
    report_1(cur)
    print("2.) The 3 Most Popular Authors by Views:\n")
    report_2(cur)
    print("3.) Days With Error Code 200 over 1%:\n")
    report_3(cur)

    db.close()

def data_fromSQL_clean(d):
    # After some research, I found this method to iterate over
    # dictionaries using a for loop from the SQL outputs so the
    # final results printed out will match the given examples.
    for key, value in d:
        # Selects the report_3 output
        if (type(value) is float):
            # Multiples the data from decimal into percentage
            value = value * 100
            print(" " + str(key) + " - " + str("%.2f" % value) + "%")
        # Selects the  report_1 & report_2 output
        else:
            print(" \"" + str(key) + "\" - " + str(value))
    # Adds a space inbetween each report
    print("\n")

def report_1(cur):
    # 1. What are the most popular three articles of all time?
    # Example: Princess Shellfish Marries Prince Handsome" - 1201 views
    cur.execute("""select title, count(*) as total_views
        from articles, log
        where articles.slug = substring(log.path, 10)
        group by articles.title
        order by total_views desc
        limit 3;""")
    # For memory optimization and human error check
    if (cur.rowcount == 0):
        print("No Results Found! Make sure database news is loaded.")
        print("""Use Command: "psql -d news -f newsdata.sql"
                Inside the /vagrant/newsdata directory to load database "news" """)
    else:
        data_fromSQL_clean(cur.fetchall())

def report_2(cur):
    # 2. Who are the most popular article authors of all time?
    # Example:Ursula La Multa - 2304 views
    # CONCAT function called to match format in author.slug and log.path
    cur.execute("""select name, count(*) as total_views
        from authors, articles, log
        where authors.id = articles.author
        and path = concat('/article/', slug)
        group by name
        order by total_views desc
        limit 3;""")
    # For memory optimization and human error check
    if (cur.rowcount == 0):
        print("No Results Found! Make sure database news is loaded.")
        print("""Use Command: "psql -d news -f newsdata.sql"
                Inside the /vagrant/newsdata directory to load database "news" """)
    else:
        data_fromSQL_clean(cur.fetchall())

def report_3(cur):
    # 3. On which days did more than 1 percent of requests lead to errors?
    # Example: July 29, 2016 - 2.5 percent errors
    # TO_CHAR (datetime) used to format days_over to match example
    # Lowercase SQL reutned errors. Had to edit report_3 within a SQL Editor
    # Saves Output as a float to separate data type from report_1 & report_2
    cur.execute("""SELECT to_char(days_over, 'FMMonth FMDD, YYYY'),
        count_error_code/count_days_over AS ratio
        FROM (SELECT time::date as days_over,
        COUNT(*) AS count_days_over,
        SUM((status != '200 OK')::int)::float AS count_error_code
        FROM log
        GROUP BY days_over) AS errors
        WHERE count_error_code/count_days_over > 0.01;""")
    # For memory optimization and human error check
    if (cur.rowcount == 0):
        print("No Results Found! Make sure database news is loaded.")
        print("""Use Command: "psql -d news -f newsdata.sql"
                Inside the /vagrant/newsdata directory to load database "news" """)
    else:
        data_fromSQL_clean(cur.fetchall())

all_reports()

# Footer
print("""
--------------------------------------------------
                End of Reports
--------------------------------------------------\n\n """)
