from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/todoapp'  # Veritabanı bağlantı bilgileri için değişmesi lazım(geçerli bir bağlantı)
db = SQLAlchemy(app)


class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<TodoItem {self.id}>'


@app.route('/')
def index():
    todo_items = TodoItem.query.all()
    return render_template('index.html', todo_items=todo_items)


@app.route('/add', methods=['POST'])
def add():
    content = request.form['content']
    new_todo = TodoItem(content=content)
    db.session.add(new_todo)
    db.session.commit()
    return redirect('/')


@app.route('/complete/<int:todo_id>')
def complete(todo_id):
    todo = TodoItem.query.get(todo_id)
    todo.completed = True
    db.session.commit()
    return redirect('/')


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = TodoItem.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
