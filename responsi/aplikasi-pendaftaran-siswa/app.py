from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/siswa_db' 
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    smp_origin = db.Column(db.String(100), nullable=False)

class StudentForm(FlaskForm):
    name = StringField('Nama', validators=[DataRequired()])
    birth_date = DateField('Tanggal Lahir', validators=[DataRequired()], format='%Y-%m-%d')
    smp_origin = StringField('Asal SMP', validators=[DataRequired()])
    submit = SubmitField('Daftar')

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        new_student = Student(name=form.name.data, birth_date=form.birth_date.data, smp_origin=form.smp_origin.data)
        db.session.add(new_student)
        db.session.commit()
        flash('Data siswa berhasil ditambahkan!', 'success')
        return redirect(url_for('index'))
    return render_template('add_student.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        student.name = form.name.data
        student.birth_date = form.birth_date.data
        student.smp_origin = form.smp_origin.data
        db.session.commit()
        flash('Data siswa berhasil diubah!', 'success')
        return redirect(url_for('index'))
    return render_template('edit_student.html', form=form)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Data siswa berhasil dihapus!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
