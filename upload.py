import os
import textract
from flask import Flask, request, redirect, url_for
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'path/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'docx'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return render_template('upload.html')

#import textract
text = textract.process('path/uploads/resumeswarup.pdf', extension='pdf')

#similarly for docx and txt

#print text


'''
#see the imports from the previous file.




app.config['ELASTICSEARCH_URL'] = 'http://localhost:9200/'
app.config['DEBUG'] = True
es = Elasticsearch([app.config['ELASTICSEARCH_URL']])

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/insert')

    es.indices.delete(index="resume_trials", ignore=404)
    es.indices.create(index="resume_trials", ignore=400)

    #i am not able to figure out the conversion txt,docx,pdf to json format while storing.

    id = 0
    for resume in resumes:
        id += 1
        #req = urllib2.Request(resumes[1])
        #res = urllib2.urlopen(req)

        data = {
          "name": resumes[0],
          "address": resumes[1],
          "skills": res.read()
        }
        es.index(index="resume_trials",doc_type="resume",id=id,body=data)
    es.indices.refresh(index="resume_trials")
    return render_template('index.html')


data = 
{
    "name":text
       }
json_data = json.dumps(data)




@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search']
    #res = es.search(index="resume_trials", body={"query": {"match_all": {}}})
    try:
        res = es.search(index="resume_trials", size=100, body={"query": {"multi_match" : { "query": search_term, "fields": ["name", "skills","address"] }}})
        return render_template('results.html', res=res, term=search_term)
    except:
        return render_template('other.html', res="ERROR: Can't find any ElasticSearch servers.")

@app.route('/search/<search_term>', methods=['GET'])
def search_history(search_term):
    try:
        res = es.search(index="resume_trials", size=100, body={"query": {"multi_match" : { "query": search_term, "fields": ["name", "address","skills"] }}})
        return render_template('results.html', res=res, term=search_term)
    except:
        return render_template('other.html', res="ERROR: Can't find any ElasticSearch servers.")

'''
    


if __name__ == '__main__':
    app.run(debug=True)
    

