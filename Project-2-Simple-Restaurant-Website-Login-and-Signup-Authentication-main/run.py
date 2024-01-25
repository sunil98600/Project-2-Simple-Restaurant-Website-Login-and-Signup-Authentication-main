from restaurant.routes import app
from restaurant import db

#checks if main.py has executed directly and not imported
if __name__ == '__main__':
    app.run(debug = True)



