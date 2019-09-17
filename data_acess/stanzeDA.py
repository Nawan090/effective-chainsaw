import uuid

from google.appengine.ext import ndb

from models.stanzeModel import Stanza


def getAllStanze():
    stanze = Stanza().query().fetch()
    return stanze


def getStanza(stanza_id):
    stanza = Stanza().query(Stanza.stanza_id==stanza_id).fetch(1)
    return stanza


def insertStanza(form):
    try:
        stanza = Stanza()
        stanza.stanza_id = str(uuid.uuid4())
        stanza.nome_stanza = form['nome_stanza']
        stanza.prezzo = form['prezzo']
        stanza.numero = form['numero']
        stanza.piano = form['piano']
        stanza.put()
        return "Stanza creata!"
    except Exception as e:
        print(str(e))
        return "Stanza non creata!"


def editStanza(stanza_id, form):
    try:
        stanza = Stanza().query(Stanza.stanza_id==stanza_id).fetch(1)
        stanza.nome_stanza = form['nome_stanza']
        stanza.prezzo = form['prezzo']
        stanza.numero = form['numero']
        stanza.piano = form['piano']
        stanza.put()
        return "Aggiornamento completato!"
    except Exception as e:
        print(str(e))
        return "Aggiornamento non completato!"


def deleteStanza(stanza_id):
    try:
        Stanza.query(Stanza.stanza_id == stanza_id).fetch(1,
                    keys_only=True)[0].get().key.delete()
        return "Stanza eliminata!"
    except Exception as e:
        print(str(e))
        return "Eliminazione non riuscita!"


def deleteAllStanza():
    try:
        ndb.delete_multi(Stanza.query().fetch(keys_only=True))
        return "Tutte le stanze sono state eliminate!"
    except Exception as e:
        print(str(e))
        return "Eliminazione non riuscita!"