from bottle import TEMPLATE_PATH  # type: ignore
from bottle import route, run, template  # type: ignore
from bottle import redirect, request  # type: ignore
from scraputils import get_news
from db import News, session
from bayes import NaiveBayesClassifier

TEMPLATE_PATH.insert(0, "")

s = session()

news = s.query(News).all()

titles = [n.title for n in news]
labels = [n.label for n in news]

X = titles[:800]
y = labels[:800]

X_test = titles[800:900]
y_test = titles[800:900]

nbc = NaiveBayesClassifier(1)
nbc.fit(X, y)


@route("/news personalisation")
def news_list():
    rows = s.query(News).filter(News.label == None).all()
    return template("news_template", rows=rows)


@route("/add_label/")
def add_label():
    news_id = request.query.id
    label = request.query.label
    s.query(News).filter(News.id == news_id)[0].label = label
    s.commit()
    redirect("/news personalisation")


@route("/recommendations")
def recommendations():

    rows = s.query(News).filter(News.label == None).all()
    predictions = [nbc.predict(n.title) for n in rows]

    rows = [rows[i] for i in range(len(rows)) if predictions[i] == "good"]
    return template("news_recommendations", rows=rows)


run(host="localhost", port=8080)
