from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User,Organization
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods =  ['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email= email).first()
        if user:
            if check_password_hash(user.password, password):
                
                organization_id = user.organization_id
                session['organization_id'] = organization_id

                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password!", category="error")
        else:
            flash("User does not exist.", category="error")


    return render_template("login.html", user= current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup' , methods =  ['GET', 'POST'])
def signup():
    if(request.method == 'POST'):
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        organization_id = request.form.get('organization')
        is_super_admin = False

        # Create the user and associate with the organization

        user = User.query.filter_by(email= email).first()
        if user:
            flash("User already exist.", category="error")

        elif len(email) < 4:
            flash("Email is too short!", category="error")
        elif len(firstName) < 2:
            flash("firstName is too short!", category="error")

        elif len(password1) < 7:
            flash("password1 is too short!", category="error")

        elif password1 != password2:
            flash("password1 is not matching with password2!", category="error")

        else:
            #add user to database
            if organization_id == 'other':
                # Create the new organization
                new_organization_name = request.form.get('newOrganizationName')
                new_organization_address = request.form.get('newOrganizationAddress')
                new_organization_city = request.form.get('newOrganizationCity')
                new_organization_state = request.form.get('newOrganizationState')
                new_organization_country = request.form.get('newOrganizationCountry')
                new_organization_phone = request.form.get('newOrganizationPhone')
                new_organization_email = request.form.get('newOrganizationEmail')

                # Create a new instance of Organization
                new_organization = Organization(
                    name=new_organization_name,
                    address=new_organization_address,
                    city=new_organization_city,
                    state=new_organization_state,
                    country=new_organization_country,
                    phone=new_organization_phone,
                    email=new_organization_email
                    )

                # Add the new organization to the database
                db.session.add(new_organization)
                db.session.commit()
                is_super_admin = True
            

            new_user = User(email=email, password=generate_password_hash(password1, method='sha256'), first_name=firstName, organization_id=new_organization.id, is_super_admin = is_super_admin)
            db.session.add(new_user)
            db.session.commit()
            session['organization_id'] = organization_id
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user, allow_organization_creation = True)