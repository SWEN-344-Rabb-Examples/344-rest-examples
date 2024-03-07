from flask import Flask
from flask_restful import Resource, Api
from api.menu import Menu, MenuItem, Init,MenuItemTaxes
from db.example import rebuild_tables
from api.books import Books

app = Flask(__name__)
api = Api(app)

api.add_resource(Menu, '/')
api.add_resource(MenuItem,'/<string:id>')
api.add_resource(Init, '/init')
api.add_resource(MenuItemTaxes,'/menu_taxes')
#api.add_resource(Menu, '/<string:searchTerm>') #Try to add a search string
api.add_resource(Books, '/books')

if __name__ == '__main__':
    rebuild_tables() #Before server starts, init the DB
    app.run(debug=True)
