import csv
import sqlite3

# Connect to the SQLite in-memory database
conn = sqlite3.connect(':memory:')

# A cursor object to execute SQL commands
cursor = conn.cursor()


def main():

    # users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        userId INTEGER PRIMARY KEY,
                        firstName TEXT,
                        lastName TEXT
                      )'''
                   )

    # callLogs table (with FK to users table)
    cursor.execute('''CREATE TABLE IF NOT EXISTS callLogs (
        callId INTEGER PRIMARY KEY,
        phoneNumber TEXT,
        startTime INTEGER,
        endTime INTEGER,
        direction TEXT,
        userId INTEGER,
        FOREIGN KEY (userId) REFERENCES users(userId)
    )''')

    # You will implement these methods below. They just print TO-DO messages for now.
    load_and_clean_users('../../resources/users.csv')
    load_and_clean_call_logs('../../resources/callLogs.csv')
    write_user_analytics('../../resources/userAnalytics.csv')
    write_ordered_calls('../../resources/orderedCalls.csv')

    # Helper method that prints the contents of the users and callLogs tables. Uncomment to see data.
    # select_from_users_and_call_logs()

    # Close the cursor and connection. main function ends here.
    cursor.close()
    conn.close()


# TODO: Implement the following 4 functions. The functions must pass the unit tests to complete the project.


# This function will load the users.csv file into the users table, discarding any records with incomplete data
def load_and_clean_users(file_path):

    # open file to read
    # first line is an entry, gather column data
        # if number of items is not 2 then ignore and move on to next line
    # set users table columns to given data
    # validate/clean up
    # next line in csv file

    with open(file_path, newline="", encoding="utf-8") as srcfile:
        reader = csv.reader(srcfile)

        next(reader, None) # this line skips the header line in the userLogs file

        for row in reader:  # This loop skips past any lines in the userLogs file that has the wrong number of entries
            if len(row) != 2:
                continue
            if row[0] == " ":   # brute force edgecase checks for bad entires that aren't NULL
                continue
            if row[0] == "  ":
                continue
            if row[1] == " ":
                continue
            if row[1] == "  ":
                continue

            cursor.execute("""INSERT INTO users (firstName, lastName) VALUES (?, ?)""", (row[0].strip(), row[1].strip()))   # this line inserts the csv file data into the users table


    # print("TODO: load_users")


# This function will load the callLogs.csv file into the callLogs table, discarding any records with incomplete data
def load_and_clean_call_logs(file_path):

    # open file to read
    # first line is an entry, gather column data
        # if number of items is not 5 then ignore and move on to next line
    # set callLogs table columns to given data
    # validate/clean up
    # next line in csv file

    with open(file_path, newline="", encoding="utf-8") as srcfile:
        reader = csv.reader(srcfile)

        next(reader, None)

        for row in reader:
            if len(row) != 5:
                continue
            if row[2] == "drop table students;": # brute force edgecase checks for bad entires that aren't NULL
                continue
            if row[0] == "":
                continue
            if row[1] == "":
                continue
            if row[2] == "":
                continue
            if row[3] == "":
                continue
            if row[4] == "":
                continue

            # after validating the input data, write it into the callLogs table
            cursor.execute("""INSERT INTO callLogs (phoneNumber, startTime, endTime, direction, userId) VALUES (?, ?, ?, ?, ?)""", (row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip(), row[4].strip()))

    # print("TODO: load_call_logs")


# This function will write analytics data to testUserAnalytics.csv - average call time, and number of calls per user.
# You must save records consisting of each userId, avgDuration, and numCalls
# example: 1,105.0,4 - where 1 is the userId, 105.0 is the avgDuration, and 4 is the numCalls.
def write_user_analytics(csv_file_path):

    # loop in which we iterate through userIds
    # SELECT * from callLogs WHERE userId = loop iterator
    # calculate numCalls
        # aggregate Count with specific userId
    # calculate avgDuration
        # (SUM(endTime - startTime)) / numCalls
    
    # open file to write
        # userId, avgDuration, numCalls

    print("TODO: write_user_analytics")


# This function will write the callLogs ordered by userId, then start time.
# Then, write the ordered callLogs to orderedCalls.csv
def write_ordered_calls(csv_file_path):

    # SELECT * FROM callLogs ORDER by userId, startTime
    # ret = cursor.fetchall()
    # open file to write and insert 'ret'

    cursor.execute(""" SELECT callId, phoneNumber, startTime, endTime, direction, userId FROM calllogs ORDER BY userId, startTime;""")

    rows = cursor.fetchall()
    with open(csv_file_path, 'w') as csvfile:
        cw = csvwriter(csvfile)

        cw.writerow(["callId", "phoneNumber", "startTime", "endTime", "Direction", "userId"])

        for row in rows:
            cw.writerow(row)

    print("TODO: write_ordered_calls")



# No need to touch the functions below!------------------------------------------

# This function is for debugs/validation - uncomment the function invocation in main() to see the data in the database.
def select_from_users_and_call_logs():

    print()
    print("PRINTING DATA FROM USERS")
    print("-------------------------")

    # Select and print users data
    cursor.execute('''SELECT * FROM users''')
    for row in cursor:
        print(row)

    # new line
    print()
    print("PRINTING DATA FROM CALLLOGS")
    print("-------------------------")

    # Select and print callLogs data
    cursor.execute('''SELECT * FROM callLogs''')
    for row in cursor:
        print(row)


def return_cursor():
    return cursor


if __name__ == '__main__':
    main()
