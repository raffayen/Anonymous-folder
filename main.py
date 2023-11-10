from flask import Flask, request, render_template, flash, redirect
import pickledb


app = Flask(__name__)
app.secret_key = '12022008'

db = pickledb.load('base.db', True)

if not db.get('counter'):
    db.set('counter', 1)
    db.dump()
    
def next_id():
    counter = db.get('counter')
    db.set('counter', counter+1)
    db.dump()
    return counter

def set_info(title, text):
    post_id = next_id()
    db.set(str(post_id), {"title": title, "text": text})
    db.dump()


@app.route('/')
def home():
    posts = []
    for post_id in range(db.get('counter') - 1, 0, -1):
        post = db.get(str(post_id))
        if post:
            posts.append(post)
    return render_template("index.html", posts=posts)





@app.route('/post')
def make_post():
    return render_template('registration.html')


@app.route("/create_post", methods=["POST"])
def create_post():
    if request.method == "POST":
        post_title = request.form['postTitle']
        post_text = request.form['postText']
        
        set_info(post_title, post_text)
        
        # Добавляем сообщение о публикации поста в объект запроса
        flash('Пост опубликован!', 'success')
        
        return redirect('/')

    

app.run(debug=True)