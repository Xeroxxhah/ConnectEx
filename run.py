from core.web import APP
from flask import render_template

app = APP()
app_instance = app.get_app()


@app_instance.route('/dashboard')
def dashboard():
     return render_template('dashboard.html')




app.run()