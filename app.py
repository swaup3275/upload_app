import os
import textract
import json
from flask import Flask, request, redirect, url_for
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from elasticsearch import Elasticsearch
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///resume_store"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import *


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
text = textract.process('path/uploads/AKASH_SHARMA.pdf', extension='pdf')

#similarly for docx and txt

#print text
data=text
json_data = json.dumps(data)


app.config['ELASTICSEARCH_URL'] = 'http://localhost:9200/'
app.config['DEBUG'] = True
es = Elasticsearch([app.config['ELASTICSEARCH_URL']])

#es = elasticsearch.Elasticsearch() 
#es=Elasticsearch() 


 # use default of localhost, port 9200


es.indices.create(index="resume_trials", ignore=400)

es.index(index="resume_trials", doc_type='resumes', id=id, body={"text":json_data})
#print(res['created'])



'''

es.index(index='resume_trials', doc_type='resumes', id=1, body=json_data)


'''
es.get(index="resume_trials", doc_type='resumes',id=id)
#print(res['_source'])

#es.search(index='resume_trials', q='in')

'''
res = es.search(index="resume_trials", doc_type="resumes", body={"query": {"match": {"text": "in"}}})
print("%d documents found" % res['hits']['total'])
for doc in res['hits']['hits']:
    print("%s) %s" % (doc['_id'], doc['_source']['text']))
    '''

#i=i+1


'''
while True:
    try:
        query = input("Enter a search: ")
        result = es.search(index=resume_trials, doc_type=resumes, body={"query": {"match": {"text": query.strip()}}})
        if result.get('hits') is not None and result['hits'].get('hits') is not None:
            print(result['hits']['hits'])
        else:
            print({})
    except(KeyboardInterrupt):
        break
        '''


res = es.search(index="resume_trials", body={"query": {"match": {'text':'automate'}}})
#print("Got %d Hits:" % res['hits']['total'])
print res


#es.search(index="resume_trials", body={"query": {"match": {'text':'Jira'}}})


'''
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
    



