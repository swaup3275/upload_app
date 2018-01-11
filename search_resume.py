import os, zipfile, urllib.request
from elasticsearch import Elasticsearch
import xml.etree.ElementTree as ET

mapping = {
    "trial": {
        "properties": {
            'name':{"type":"string"},
            'Address':{"type":"string"}
            'skills':{"type":"string"}

        }
    }
}



#to ignore new line.
def strip_newlines(strings):
    return strings.replace("\n", "<br />")

# ignore spaces.
def strip_extra_spaces(strings):
    return " ".join(strings.split())

# connect to Elasticsearch!
es = Elasticsearch()


es.indices.create("resume_trials")

es.indices.put_mapping(index="resume_trials", doc_type="trial", body=mapping)

