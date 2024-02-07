import mysql.connector
from mysql.connector import Error
def create_connection (hostname, uid, pwd, dbname):
    conn = None
    try:
        conn = mysql.connector.connect(
            host = hostname,
            user = uid,
            password = pwd,
            database = dbname
        )
        print("DB created successfully")
    except Error as e:
        print("Error is", e)
    return conn

myconn = create_connection('sp2024db.c7ugmewi8xhh.us-east-1.rds.amazonaws.com', 'admin', 'Gau113114115116!', 'sp2024db')
mycursor = myconn.cursor(dictionary=True)



print('MENU')
print('a - Add game')
print('o - Output all games in console')
print('q - Quit')

option = 'Choose an option!'
while option != 'q':
    if option == 'a':
        game_name = input('Name of the game?')
        player_number = int(input('What is the maxplayers number?'))
        gameresult = input('What is the result?')
        game_duration = int(input('What is the duration of the game?'))
        game_score = int(input('What is the score?'))
        try:
            mycursor.execute('insert into boardgame(gamename, maxplayers, result, gameduration, maxscore) values (%s,%s,%s,%s,%s)', (game_name, player_number, gameresult, game_duration, game_score))
            print("Game added successfully")
        except Error as e:
            print("Error is", e)
        option = 'Choose an option!'
    elif option == 'o':
        mycursor.execute('select* from boardgame')
        gamelist = mycursor.fetchall()
        print(gamelist)
    else:
        print("Wrong option")



                             

                         
