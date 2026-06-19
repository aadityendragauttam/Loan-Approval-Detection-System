from flask import Flask, request , url_for , render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/project')
def project():
    return render_template('project.html')
@app.route('/history')
def history():
    return render_template('history.html')
@app.route('/project',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        brand_name =request.form['brand_name']
        owner =int(request.form['owner'])
        age =int(request.form['age'])
        power =int(request.form['power'])
        kms_driven =int(request.form['kms_driven'])
        print('Outcome :- ', [brand_name,owner,age,power,kms_driven])
    
    return render_template('project.html')

if __name__ == '__main__':
    app.run(debug=True)