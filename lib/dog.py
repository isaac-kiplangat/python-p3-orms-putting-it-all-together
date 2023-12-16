import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    
    def __init__(self, name, breed):
      self.name = name
      self.breed = breed
      self._id = None
      
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS dogs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                breed TEXT
            )
        """
        CURSOR.execute(sql)
        
    @classmethod
    def drop_table(self):
        sql = """DROP TABLE IF EXISTS dogs """

        CURSOR.execute(sql)
        
    def save(self):
        sql = """
            INSERT INTO dogs (name,breed)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.breed))
     
    @classmethod   
    def create(cls, name, breed):
      new_dog = cls(name, breed)
      new_dog.save()
      
      return new_dog
    

Dog.create("joey", "cocker spaniel")