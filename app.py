from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketing_items.db'
db = SQLAlchemy(app)

class MarketingItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)

    def __repr__(self):
        return f"<MarketingItem {self.id}>"

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

@app.route('/')
def index():
    items = MarketingItem.query.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        item = MarketingItem(name=name, description=description)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    item = MarketingItem.query.get(id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    item = MarketingItem.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

