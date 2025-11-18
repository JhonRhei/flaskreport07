from flask import Flask, render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'


RECORDS = []
class RecordForm(FlaskForm):
    title = StringField( 
    'Title',
    validators=[
        DataRequired(message= 'Title is Required'),
        Length(min=1, max=140, message='Title must be between 1-140 characters')
        ]
    )

    content = TextAreaField(
        'Content',
        validators=[
            Length(max=2000, message='Content cannot exceed 2000 characters')
        ]
    )

    submit = SubmitField('Save Report')

@app.route('/records/new', methods=['GET', 'POST'])

def create_record():
    form = RecordForm()

    if form.validate_on_submit():
        new_record = {
            'id': len(RECORDS) + 1,
            'title': form.title.data,
            'content': form.content.data
        }
        RECORDS.append(new_record)

        return redirect(url_for('list_records'))

    return render_template('form.html', form=form, action='Create')

@app.route('/records')
def list_records():
    return render_template('records_list.html', records=RECORDS)



@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/index')
def index(): 
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

