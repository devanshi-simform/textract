from django.conf import settings
import boto3
from trp import Document
import csv


s3bucketName = "devanshidev"
TabledocumentName = "refer_image.jpg"

# Amazon TextTract Client
textractmodule = boto3.client('textract',  region_name='us-east-1',                            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key= settings.AWS_SECRET_ACCESS_KEY)

def lines(documentName, doc):
    f = open(documentName + "-lines.txt", "w+")
    for page in doc.pages:
        for line in page.lines:
            f.write("{} -- {}".format(line.text, line.confidence) + "\n")
    f.close()

def forms(documentName, doc):
    f = open(documentName + "-fields.txt", "w+")
    for page in doc.pages:
        for field in page.form.fields:
            kv = "Key: {} Value: {}".format(field.key, field.value)
            f.write(kv + "\n")
    f.close() 


def tables(documentName, doc):
    for p, page in enumerate(doc.pages):
        for t, table in enumerate(page.tables):
            f = open(documentName + "-table-" + str(p) + "-" + str(t) + ".csv", "w+")
            w = csv.writer(f, escapechar='\\', lineterminator='\n')
            for r, row in enumerate(table.rows):
                rw = []
                for c, cell in enumerate(row.cells):
                    rw.append(cell.text)
                w.writerow(rw)
            f.close()


def analyze(document,choice_data):
    # breakpoint()
    response = textractmodule.analyze_document(
        Document={
            'S3Object': {
                'Bucket': s3bucketName,
                'Name': TabledocumentName
            }
        },
        FeatureTypes=["TABLES", "FORMS"]
    )
    doc = Document(response)
    if choice_data == 'Form':
        forms(document,doc)
    elif choice_data == 'Table':
        tables(document,doc)
    elif choice_data == 'Text':
        lines(document,doc)

client = boto3.client('s3')
