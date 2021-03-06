from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField,StringField,SubmitField, DateField, IntegerField, DecimalField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY' #KEY FOR CRSF Protection

@app.route('/ben')
def ben():
    return render_template('ben.html')

@app.route('/harry')
def harry():
    return render_template('harry.html')

@app.route('/list')
def listofnames():
    return render_template('listnames.html',listnames=["ben","harry","bob","jay","matt","bill"])

class AddForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    today = DateField('Today is ?')
    favnum = IntegerField('Your Favourite Number ?')
    question = DecimalField('What is 5 - 2.5 ?')
    validate = SelectField('Are you a Human ?', choices=["Yes", "No", "I'm not sure"])
    submit = SubmitField('Add Name to Database')

class UserCheck():
    def __init__(self,banned,message=None):
        self.banned = banned
        if not message:
            message = 'Please choose another username'
        self.message = message
    
    def __call__(self,form,field):
        if field.data.lower() in (word.lower() for word in self.banned):
            raise ValidationError(self.message)

class MyForm(FlaskForm):
    username = StringField('Username', validators = [
        DataRequired(),
        UserCheck(message = "You have entered a banned user name, Please enter another", banned=['root','admin','sys']),
        Length(min=2, max=15)
    ])
    submit1 = SubmitField('Sign Up')

@app.route('/home1', methods=['GET','POST'])
def postName():
    form = MyForm()
    if form.validate_on_submit():
        username = form.username.data
        return render_template('home2.html', form = form, username=username)
    else:
        return render_template('home2.html', form = form, username="")


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])

def home():
    error=""
    form= AddForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        today = form.today.data
        favnum = form.favnum.data
        question = form.question.data
        validate = form.validate.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both a first and last name"
        else:
            return 'Welcome ' + first_name + ' ' + last_name
    return render_template('home.html', form=form, message=error)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

