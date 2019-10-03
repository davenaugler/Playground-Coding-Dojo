from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def play():
    return render_template('index.html', num=3, color='#9FC5F8')

@app.route('/play/<int:num>')
def playNum(num):
    return render_template('index.html', num=num, color='#9FC5F8')

@app.route('/play/<int:num>/<string:color>')
def playNumColor(num,color):
    return render_template('index.html', num=num, color=color)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")
    # return 'This is a 404 Error! Please check the URL and try again.'

if __name__=="__main__":
    app.run(debug=True)