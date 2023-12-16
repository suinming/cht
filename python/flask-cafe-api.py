# 想要了解與比較各家咖啡店的狀況？適不適合工作閱讀？
# 此api的情境就是讓你了解各家咖啡店的情況，基本的資料結構如下：
# id: 咖啡店的id
# name: 咖啡店的名稱
# has_wifi: 咖啡店是否有wifi
# price: 咖啡店咖啡的價格

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# db table Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        # Loop through each column in the data record
        print(self.__table__.columns)
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET

@app.route("/all")
def get_all_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    # Simply convert the random_cafe data record to a dictionary of key-value pairs.
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/search", methods=['get'])
def search_cafe():
    location = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    try:
        cafes = result.scalars().all()
        return jsonify(cafe=[cafe.to_dict() for cafe in cafes])
    except Exception:
        return jsonify(error={"Not found": "Sorry, we do not find the cafe in that location"})


# HTTP POST
@app.route("/add", methods=['post'])
def add_cafe():
    try:
        new_cafe = Cafe(
            name=request.form.get("name"),
            has_wifi=bool(request.form.get("wifi")),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(result={"success": True})
    except Exception:
        return jsonify(error={"success": False})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['put', 'patch'])
def update_cafe(cafe_id):
    new_price = request.args["new_price"]
    try:
        cafe = db.get_or_404(Cafe, cafe_id)
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(result={"success": True})
    except Exception:
        return jsonify(result={"success": False})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['delete'])
def delete_cafe(cafe_id):
    key = request.args["api-key"]
    # verify if the api key is correct
    if(key == "secret"):
        try:
            cafe = db.get_or_404(Cafe, cafe_id)
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(result={"success": True})
        except Exception:
            return jsonify(result={"success": False})
    else:
        return jsonify(result={"success": False, "msg": "wrong api key"})


if __name__ == '__main__':
    app.run(debug=True)
