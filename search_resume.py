import os
import json
import urllib2
from flask import Flask
from flask import render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)
app.config['ELASTICSEARCH_URL'] = 'localhost'
app.config['DEBUG'] = True

es = Elasticsearch([app.config['ELASTICSEARCH_URL']])

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/seed')


'''def add_document():
    resumes =[



    ]



    '''



    es.indices.delete(index="resume_trials", ignore=404)
    es.indices.create(index="resume_trials", ignore=400)

    

    id = 0
    for resume in resumes:
        id += 1
        req = urllib2.Request(resumes[1])
        res = urllib2.urlopen(req)
        data = {
          "name": resumes[0],   #have to put in json format.
          "address": resumes[1],
          "skills": res.read()
        }
        es.index(index="resume_trials",doc_type="resume",id=id,body=data)
    es.indices.refresh(index="resume_trials")
    return render_template('index.html')



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
mapping = {
    "trial": {
        "properties": {
            'name':{"type":"string"},
            'Address':{"type":"string"}
            'skills':{"type":"string"}

        }
    }
}




# connect to Elasticsearch!
es = Elasticsearch()


es.indices.create("resume_trials")

es.indices.put_mapping(index="resume_trials", doc_type="trial", body=mapping)

'''



