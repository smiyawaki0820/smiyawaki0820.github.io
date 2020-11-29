import os
from os import path
import sys
import logging
import argparse
from typing import List
from pprint import pprint
from hashlib import sha256
from datetime import datetime

import csv
import sqlite3
from flask import Flask, render_template, request, session, redirect, url_for

from src.create_db import TableInstance, db_session


logging.basicConfig(
    format='%(asctime)s #%(lineno)s %(levelname)s %(name)s :::  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG,
    stream=sys.stdout,
)

logger = logging.getLogger(__name__)
app = Flask(__name__)

ROOT = '/work02/miyawaki/smiyawaki0820.github.io'


# Model ==========================================

sys.path.append(os.path.join(ROOT, 'ILYS-aoba-chatbot'))
from src.models.ilys import IlysAobaBot
from neural_dialogue_model.model_args import Args
from neural_dialogue_model.models import NeuralDialogueModel

parser = argparse.ArgumentParser(description='')
group = parser.add_argument_group("Dialogues")
group.add_argument('--model', type=path.abspath, metavar="FP", help="Path to model parameters",
    default=os.path.join(ROOT, 'models/ilys_aoba_transformer_finetuned.pt'))
group.add_argument('--spm', type=path.abspath, metavar="FP", help="Path to sentencepiece model",
    default=os.path.join(ROOT, 'models/spm_10M_tweets.cr9999.bpe.32000.model'))
group.add_argument('--vocab', type=path.abspath, metavar="FP", help="Path to vocab",
    default=os.path.join(ROOT, 'data/fairseq_vocab'))
parser_args = parser.parse_args()

args = Args(
    model_path=parser_args.model, 
    spm_path=parser_args.spm, 
    vocab_path=parser_args.vocab
)

dialogue_model = NeuralDialogueModel(args)

global model
model = IlysAobaBot(dialogue_model)

# Sample Input
model.predict('こんにちは．あおばさんは今何してますか．')
model.predict('一日中ゴロゴロしてたんですか？')
model.clear()

# ================================================


@app.route("/")
@app.route("/index") #「/index」へアクセスがあった場合に、「index.html」を返す
def index():
    """ in .html
    {{name}}    # var
    {% if hoge == fuga %} ... {% endif %}
    {% for k in iter %} ... {% endfor %}
    """
    name = request.args.get("name")         # query_string から値を受け取る
    table_data = TableInstance.query.all()  # sqlite3 content.db
    return render_template("index.html", name=name, table_data=table_data) # **kwargs 形式


@app.route("/index",methods=["post"])
def post():
    name = request.form["name"]
    table_data = TableInstance.query.all()
    return render_template("index.html", name=name, table_data=table_data)


@app.route('/add',methods=['post'])
def add():
    title = request.form['title']
    body = request.form['body']
    content = TableInstance(title,body,datetime.now())
    db_session.add(content)
    db_session.commit()
    return redirect(url_for('index'))


@app.route('/update',methods=['post'])
def update():
    content = TableInstance.query.filter_by(id=request.form['update']).first()
    content.title = request.form['title']
    content.body = request.form['body']
    db_session.commit()
    return redirect(url_for('index'))


@app.route('/delete',methods=['post'])
def delete():
    id_list = request.form.getlist('delete')
    for id in id_list:
        content = TableInstance.query.filter_by(id=id).first()
        db_session.delete(content)
    db_session.commit()
    return redirect(url_for('index'))


@app.route("/to_csv",methods=["post"])
def to_csv():
    try:
        fo_csv = request.form["fo_csv"]
        logger.info(f'GET | {fo_csv}')
        connect = sqlite3.connect('models/content.db')
        cursor = connect.execute('select * from TABLENAME')
        with open(fo_csv, 'w') as fo:
            writer = csv.writer(fo)
            writer.writerows(cursor.fetchall())
            logger.info(f'WRITE | {fo.name}')
        state = 'TRUE'
    except:
        state = 'FALSE'
    return render_template("index.html", fo_csv=fo_csv, state=state)


@app.route("/interface",methods=["post"])
def interface():
    try:
        input_text = request.form["input_text"]
        logger.info(f'GET | {input_text}')
        outputs: list = model.predict(input_text)
        state = 'TRUE'
    except:
        outputs=[]
        state = 'FALSE'
    return render_template("index.html", outputs=outputs, state_interface=state)

@app.route('/clear_history',methods=['post'])
def clear_history():
    model.clear()
    return render_template("index.html")
