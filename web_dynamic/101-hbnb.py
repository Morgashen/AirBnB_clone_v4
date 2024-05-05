#!/usr/bin/python3
"""Flask app to generate complete html page containing location/amenity
dropdown menus and rental listings"""
from flask import Flask, render_template
from models import storage
import uuid
app = Flask('web_dynamic')
app.url_map.strict_slashes = False

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB is alive!"""
    places = storage.all(Place).values()
    places = sorted(places, key=lambda x: x.name)
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda x: x.name)
    values = {
        'states': storage.all(State).values(),
        'amenities': amenities,
        'places': places,
        'cache_id': uuid.uuid4()
    }
    return render_template('101-hbnb.html', **values)

@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Close database or file storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
