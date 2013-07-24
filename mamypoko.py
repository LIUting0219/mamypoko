from flask import Flask,render_template,request,redirect
app = Flask(__name__)


######################### Html ###########################

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/', methods=['GET', 'POST'])
def user():
    return render_template('user.html', username='kevin', selected='user')

@app.route('/video/', methods=['GET', 'POST'])
def video():
    return render_template('video.html', username='kevin', selected='video')

@app.route('/feedback/', methods=['GET', 'POST'])
def feedback():
    return render_template('feedback.html', username='kevin', selected='feedback')

@app.route('/admin/', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html', username='kevin', selected='admin')


######################### Data ###########################

@app.route('/form/login/', methods=['POST','GET'])
def form_login():
    if request.method == 'POST':
        name = request.form('username')
        password = request.form('password')
    if request.method == 'GET':
        name = request.args.get('username')
        password = request.args.get('password')
    return redirect('/admin/')



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9999, debug=True)