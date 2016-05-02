from flask import Flask, render_template, redirect, url_for
import os
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
import sqlite3

app = Flask(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'comments.db'),
    SECRET_KEY='development key'
))
Bootstrap(app)

#routes to webpages 
@app.route('/')
def send_static():
    pass
    
    
@app.route('/Home')
def Home():
    return render_template('Home.html')
    
    
@app.route('/latestnews')
def latestnews():
    return render_template('Latest News.html')
    
@app.route('/events')
def Events():
    return render_template('Events.html')
    
#articles    
@app.route('/article1')
def article1():
    return render_template('Article1.html')
    
@app.route('/article2')
def article2():
    return render_template('Article2.html')
    
@app.route('/article3')
def article3():
    return render_template('Article3.html')
    
#Creates form for comments
class CommentForm(Form):
    name = StringField('Name:', validators=[DataRequired()])
    comments = TextAreaField('Comments', validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Submit')

#inserts into database
@app.route('/Form', methods=['GET', 'POST'])
def view_form():
    form = CommentForm()
    if form.validate_on_submit():
        name = form.name.data
        comments = form.comments.data
        with sqlite3.connect(app.config['DATABASE']) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO comments_table (name, comments) VALUES (?,?)", (name, comments))
            con.commit()

        return redirect(url_for('list_results'))
    return render_template('Form.html', form=form)

#displays information from database
@app.route('/display')
def list_results():
    with sqlite3.connect(app.config['DATABASE']) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM comments_table")
        entries = cur.fetchall()
        return render_template('Comments.html', entries=entries)
        
        
        
#server
if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)