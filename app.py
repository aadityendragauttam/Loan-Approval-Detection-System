from flask import Flask, request , url_for , render_template
import joblib
model = joblib.load(r'C:\Users\user\OneDrive\Desktop\Data Science\Loan-Approval-Detection-System\model\Loan_model.lb')
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
        income =int(request.form['income'])
        credit_score =int(request.form['credit_score'])
        loan_amount =int(request.form['loan_amount'])
        years_employed =int(request.form['years_employed'])
        print('Outcome :- ', [income,credit_score,loan_amount,years_employed])
        pred = model.predict([[income,credit_score,loan_amount,years_employed]])
        if pred == 0:
            final = 'Not Approved'
        else:
            final = 'Approved'
    
    return render_template('project.html',prediction = final)

if __name__ == '__main__':
    app.run(debug=True)