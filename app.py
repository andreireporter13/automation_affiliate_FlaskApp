from flask import Flask, render_template
from dry_modules import return_list_from_csv


# start app;
app = Flask(__name__)

# set secret key;


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('acasa.html')


@app.route('/reduceri-beauty')
def reduceri_beauty():
    
    # this function from module; respect DRY rule;
    list_with_html_code = return_list_from_csv("pages_scrapers/csv_data_base/beauty_data.csv")
      
    return render_template('beauty.html', list_with_html_code=list_with_html_code)
   
    
@app.route('/reduceri-books')
def reduceri_books():
    return render_template('books.html')


# sa caut o conexiune pentru newsletter + contact;


if __name__ == "__main__":
    app.run(debug=True)