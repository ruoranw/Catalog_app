from flask import Flask , render_template, request, redirect, url_for,flash , jsonify
app = Flask(__name__)

# Import CRUD Operations from Lesson 1
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# Create an instance of this class with the name of running application as the argument

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/restaurants/<int:restaurant_id>/menu/<int:item_id>/JSON/')
def menuItemJSON(restaurant_id, item_id):
    oneItem = session.query(MenuItem).filter_by(id = item_id).one()
    return jsonify(MenuItem=oneItem.serialize)


@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])


# Making an API Endpoint
# These two are decorators
@app.route('/')
@app.route('/restaurants/')
def showRestaurant():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurant.html',restaurants=restaurants)

# Show a restaurant menu
@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')

def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    return render_template('menu.html', restaurant=restaurant, items=items)


# Task 1: Create route for newMenuItem function here


@app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET','POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
         newItem = MenuItem(name = request.form['name'],restaurant_id = restaurant_id)
         session.add(newItem)
         session.commit()
         flash("new menu item created!")
         return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)


# Task 2: Create route for editMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/',methods=['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        session.add(editedItem)
        session.commit()
        flash("Item has been edited successfully.")
        return redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem)


# Task 3: Create a route for deleteMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete', methods=['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        session.delete(editedItem)
        session.commit()
        flash("Item has been deleted successfully.")
        return redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 8020)




