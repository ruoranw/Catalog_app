from flask import Flask,render_template, request, redirect, url_for,flash , jsonify
app = Flask(__name__)

# Import CRUD Operations from Lesson 1
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# Create an instance of this class with the name of running application as the argument

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Add Routes

@app.route('/')
@app.route('/restaurants/')
# Show all restaurants
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)
    # return "This page will show all my restaurants."


@app.route('/restaurants/new/',methods=['GET','POST'])
# Create a new restaurant.
def newRestaurant():
    if request.method == 'POST':
        newRestaurant = Restaurant(name = request.form['name'])
        session.add(newRestaurant)
        session.commit()
        return redirect(url_for('showRestaurants', restaurants = restaurants))
    else:
        return render_template('newRestaurant.html')

    # return "This page will be for making a new restaurant."


@app.route('/restaurants/<int:restaurant_id>/edit/', methods=['GET','POST'])
# Edit a restaurant
def editRestaurant(restaurant_id):
    editedRestaurant = session.query(Restaurant).filter_by(id =restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editRestaurant.name = request.form['name']
            session.add(editRestaurant)
            session.commit()
            return redirect(url_for('showRestaurants'))
    else:
        return render_template('editRestaurant.html', restaurant=editedRestaurant,restaurant_id=restaurant_id)

    # return "This page will be for editing the %s restaurant." %restaurant_id


@app.route('/restaurants/3/delete/')
# Delete a restaurants
def deleteRestaurant():

    return render_template('deleteRestaurant.html')
    # return "This page will be for deleting the %s restaurant." %restaurant_id


@app.route('/restaurants/restaurant_id/')
@app.route('/restaurants/3/menu/')
# Show all menu items of a restaurant
def showMenu():

    return render_template('menu.html')
    # return "This page is for the menu of restaurant %s." %restaurant_id


@app.route('/restaurants/3/menu/new')
# Make a new menu
def newMenuItem():
    return render_template('newMenuItem.html')
    # return "This page is for making a new menu item for restaurant %s." %restaurant_id


@app.route('/restaurants/restaurant_id/menu/menu_id/edit')
# Edit the menu
def editMenuItem():

    return render_template('editMenuItem.html')
    # return "This page is for editing menu item %s" %menu_id


@app.route('/restaurants/restaurant_id/menu/menu_id/delete')
# Delete the menu
def deleteMenuItem():
    return render_template('deleteMenuItem.html')
    # return "This page is for deleting menu item %s" %menu_id



#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8101)