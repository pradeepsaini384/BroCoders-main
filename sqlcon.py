import mysql.connector

conn = mysql.connector.connect(host = "localhost",user= "root",password ="",database="blog")
cursor = conn.cursor()

def registration(rollno,name,email,password):
    cursor.execute("""INSERT INTO `users` (`user_id`,`name`,`email`,`password`) VALUES ('{}','{}','{}','{}')""".format(rollno,name,email,password))
    conn.commit()

def email_auth(email):
    done = 1
    cursor.execute("""SELECT * FROM `email` WHERE `email` LIKE '{}' """.format(email))
    popular = cursor.fetchall()
    if len(popular)>0:
        return done
    else:
        cursor.execute("""INSERT INTO `email` (`email`) VALUES('{}')""".format(email))
        conn.commit()
        done = 0
        return done
        
def addblog(title,category,subcategory,type,shortdesc,detail):

    
def authentication(email,password):
    cursor.execute("""SELECT * FROM `admin` WHERE `name` LIKE '{}' AND `pwd` LIKE '{}'""".format(email,password))
    users = cursor.fetchall()
    return users

def blog_data():
    category = ['popular','latest','feature']
    
    cursor.execute("""SELECT * FROM `blog` WHERE `type` LIKE '{}' """.format(category[0]))
    popular = cursor.fetchall()
    
    cursor.execute("""SELECT * FROM `blog` WHERE `type` LIKE '{}' """.format(category[1]))
    latest = cursor.fetchall()

    cursor.execute("""SELECT * FROM `blog` WHERE `type` LIKE '{}' """.format(category[2]))
    feature = cursor.fetchall()

    return popular,latest,feature

def all_blog():
    cursor.execute("""SELECT * FROM `admin` """)
    all_admin = cursor.fetchall()
    p = 0
    l = 0
    f =0
    lst = []
    cursor.execute("""SELECT * FROM `blog` """)
    all_blog = cursor.fetchall()
    for i in all_blog:
        category = ['popular','latest','feature']
        if i[11] == category[0]:
            p += 1
        elif i[11] == category[1]:
            l += 1
        elif i[11] == category[2]:
            f += 1
        else:
            pass
    lst.append(p)
    lst.append(l)
    lst.append(f)
    return all_admin,lst
def blog_detail(id):
    cursor.execute("""SELECT * FROM `blog` WHERE `id` LIKE '{}'""".format(id))
    blog_details = cursor.fetchall()
    return blog_details