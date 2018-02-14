#Ryan McVicker
#database application
#this application should involve a class that will RETURN values
# ADD values to database
# or DELETE values from database
import sqlite3
import time



class DatabaseApp:

    def __init__(self):

        #initializes database for storing tables of
        #weather data or file names and directories 
        self.conn = sqlite3.connect('testdata.db')
        self.c = self.conn.cursor()


        #table to hold values of weather data
        self.c.execute('CREATE TABLE IF NOT EXISTS WeatherData(date TEXT,temperature INT)')

        #table to hold values of file names and directories
        self.c.execute('CREATE TABLE IF NOT EXISTS FileData(filename TEXT,filedirectory TEXT)')

        

    #values should be in a dictionary or list
    #if list then convert to tuple
    def add_to_weather_table(self,values_to_add):
        self.c.execute("INSERT INTO WeatherData VALUES(?,?)",values_to_add)
        self.conn.commit() #ALWAYS DO THIS WHEN MODIFYING DATA


    def add_to_file_table(self,values_to_add):


        #try statement to check for too many values ready to be entered
        try:
            if len(values_to_add) > 2:
                print("those are too many values to enter the database......")

                

        
            else:
                
                #default for this statement is going to assume the "list to tuple" tactic
                try:
                    self.c.execute("INSERT INTO FileData VALUES(?,?)",values_to_add)
                    self.conn.commit()

                except Exception as e:
                    print(e)
                    print('need to fix the insert statement in databaseapp.py')

        except Exception as e:
            pass

        


    #same as before, dictionary or list
    def delete_value_file(self,value_to_delete):
        
        #note: SHOULD ALWAYS EXPECT FOR DATABASE FUNCTIONS TO GO AWRY
        try:
                                   
            self.c.exeute("DELETE FROM FileData VALUES(?,?)",value_to_delete)
            self.conn.commit()

        except Exception as e:
            print(e)
            print('you should probably fix this.....in databaseapp.py')


    def delete_value_weather(self,value_to_delete):
        
        try:
                                   
            self.c.exeute("DELETE FROM WeatherData VALUES(?,?)",tuple(value_to_delete))
            self.conn.commit()

        except Exception as e:
            print(e)
            print('you should probably fix this.....in databaseapp.py at the delete statement')

                      
