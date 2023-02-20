from flask import Flask,render_template ,Response,redirect,request,flash,url_for,Request
from sqlcon import authentication,registration,blog_data , blog_detail,email_auth,all_blog
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
UPLOAD_FOLDER = 'static/images/blog_img/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#for home page
@app.route('/')
def home():
    popular,latest,feature = blog_data()
    print(popular,latest,feature)
    return render_template('index.html',popular=popular,latest=latest,feature=feature)


#for education blog page
@app.route('/eduBlog')
def eduBlog():
    return render_template('eduBlog.html')


#for businessBlog page
@app.route('/businessBlog')
def businessBlog():
    return render_template('businessBlog.html')


#for entertainmentBlog page
@app.route('/entertainmentBlog')
def entertainmentBlog():
    return render_template('entertainmentBlog.html')


#for about page
@app.route('/about')
def about():
    return render_template('about.html')


#for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')


#for blogDetails page
@app.route('/blogDetails/<id>')
def blogDetails(id):
    blog_details = blog_detail(id)
    print(blog_details)
    return render_template('blogDetails.html',blog_details=blog_details)


#for login page
@app.route('/login')
def login():
    return render_template('login.html')

# #for userdashboard 
# @app.route('/dashboard')
# def dashboard():
#     return render_template('index.html')

#for email subscribe
@app.route('/email',methods = ['GET','POST'])
def email():
    email = request.form.get('email')
    e = email_auth(email)
   
    if e==0:
        flash("Email Insert successfully!")
        return render_template('index.html')
    else:
        flash('Email Aready Added Or Something Went Wrong!')
        return render_template('index.html')
    

#admin control goes from here
@app.route('/dashboard')
def dashboard():
    all_admin,lst = all_blog()
    # popular
    # letest
    # feature
    total_admin = len(all_admin)
    return render_template('/backend/index.html',all_admin=all_admin,total_admin=total_admin,popular=lst[0],letest=lst[1],feature=lst[2])

@app.route('/newpost')
def newpost():
    return render_template('/backend/newPost.html')
@app.route('/education')
def education():
    return render_template('/backend/education.html')
@app.route('/business')
def business():
    return render_template('/backend/business.html')
@app.route('/Entertainment')
def Entertainment():
    return render_template('/backend/entertainment.html')

@app.route('/register')
def register():
    return render_template('/backend/register.html')
@app.route('/admin')
def admin():
    return render_template('/backend/login.html')
    
@app.route('/auth',methods = ['GET','POST'])
def auth():
    name = request.form.get("name")
    password = request.form.get("password")
    user_data =  authentication(name,password)
    
    if(len(user_data)>0):
        return redirect("/dashboard",code=302)
    
@app.route('/addblog',methods=['GET','POST'])
def addblog():
    title = request.form.get("title")
    Category = request.form.get("gridRadios")
    subcategory = request.form.get("subcategory")
    type = request.form.get("checkbox")
    shortdesc = request.form.get("shortdesc")
    detaildesc = request.form.get("detaildesc")
    file = request.files['file']
    print(file)
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'done'
    else:
        return'nahi beta '
    
if __name__ == '__main__':
    app.run(debug=True)