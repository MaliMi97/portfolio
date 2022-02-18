import psycopg2 as pg2

'''
This class is for executing some PostgreSQL queries in a loop, so I do not have to type everything
'''


class PostgreSQL():
    '''
    Database is the database name, user is the username, host is where the server is and
    path_to_default is path to PostgreSQL script containing queries, which create tables, views, procedures and functions,
    but does not input any data.
    '''
    def __init__(self, database, user, host, path_to_default):
        for i in range(3):
            try:
                password = input()
                self.conn = pg2.connect(database=database, user=user, password=password, host=host)
                break
            except Exception as e:
                print(e)
                print(f"You have got {2-i} tries to connect to the database")
                if i == 2: return

        self.cur = self.conn.cursor()
        self.path_to_default = path_to_default

    def close(self):
        '''
        Closes the connection to the database
        '''
        self.conn.close()

    def return_string(self, s):
        '''
        Returns null in sql if s is None, else returns string in '', so that sql knows it is string
        '''
        if s == None:
            return 'null'
        return f"'{s}'"

    def try_except(self, s):
        '''
        Tries to execute commands. If the execution succeeds, calls commit. If it fails, calls rollback.
        '''
        try:
            self.cur.execute(s)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def return_to_default(self):
        '''
        returns the database to a state of path_to_default script
        '''
        file = open(self.path_to_default, 'r')
        command = file.read().replace('\n',' ').replace('\t',' ')
        self.try_except(command)
        file.close()

    def fill_database_with_token(self, d):
        '''
        Fills the database with information about the token and connects the relations.
        '''
        self.try_except(f'''INSERT INTO crypto_token (abbreviation, token_name, website, sector, maximum_supply, launch_date)
VALUES ({self.return_string(d['crypto_token']['abbreviation'])}, {self.return_string(d['crypto_token']['token_name'])}, {self.return_string(d['crypto_token']['website'])}, {self.return_string(d['crypto_token']['sector'])}, {self.return_string(d['crypto_token']['maximum_supply'])}, {self.return_string(d['crypto_token']['launch_date'])})''')
        
        for i in d['social_media']:
            self.try_except(f'''INSERT INTO social_media (abbreviation, url)
VALUES ({self.return_string(d['crypto_token']['abbreviation'])}, {self.return_string(i)})''')
        
        for i in d['investor']:
            self.try_except(f'''INSERT INTO investor (investor_name, type_of_investor)
VALUES ({self.return_string(i['investor_name'])}, {self.return_string(i['type_of_investor'])})''')
            self.try_except(f'''INSERT INTO investment (abbreviation, investor_name)
VALUES ({self.return_string(d['crypto_token']['abbreviation'])}, {self.return_string(i['investor_name'])})''')
        
        for i in d['teammate']:
            self.try_except(f'''INSERT INTO teammate (teammate_name, background)
VALUES ({self.return_string(i['teammate_name'])}, {self.return_string(i['background'])})''')
            self.try_except(f'''INSERT INTO team (abbreviation, teammate_name, teammate_position, start_on, end_on)
VALUES ({self.return_string(d['crypto_token']['abbreviation'])}, {self.return_string(i['teammate_name'])}, {self.return_string(i['teammate_position'])}, {self.return_string(i['start_on'])}, {self.return_string(i['end_on'])})''')
        
        for i in d['keyword']:
            self.try_except(f'''INSERT INTO keyword (description)
VALUES ({self.return_string(i)})''')
            self.try_except(f'''CALL insert_characteristic_by_description ({self.return_string(d['crypto_token']['abbreviation'])}, {self.return_string(i)})''')
    