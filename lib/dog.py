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
  
  
    @classmethod
    def new_from_db(cls, row):
        # Create a new Dog instance from a database row (array)
        dog = cls(name=row[1], breed=row[2])
        dog.id = row[0]
        return dog

    @classmethod
    def get_all(cls):
        # Retrieve all records from the dogs table and return a list of Dog instances
        sql = "SELECT * FROM dogs"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.new_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        # Find a dog by name and return a Dog instance
        sql = "SELECT * FROM dogs WHERE name = ?"
        CURSOR.execute(sql, (name,))
        row = CURSOR.fetchone()
        return cls.new_from_db(row) if row else None
    

Dog.create("joey", "cocker spaniel")