from flask import Flask, send_from_directory

app = Flask(__name__);

@app.route('/')
def send_static():
    pass
    # return render_template()
    
@app.route('/Home')
def send_static2():
    return app.send_static_file('Home.html')

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)
    # app.run()