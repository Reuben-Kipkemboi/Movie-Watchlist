# @auth.route('/register',methods = ["GET","POST"])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(email = form.email.data, username = form.username.data,password = form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('auth.login'))
#         title = "New Account"
    # return render_template('auth/register.html',registration_form = form)