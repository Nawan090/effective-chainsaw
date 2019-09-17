from google.appengine.ext import ndb


class Stanza(ndb.Model):
    stanza_id = ndb.StringProperty(required=True)
    nome_stanza = ndb.StringProperty(required=True)
    numero = ndb.IntegerProperty()
    piano = ndb.StringProperty()
    tipologia = ndb.StringProperty()
    prezzo = ndb.FloatProperty()
    immagine = ndb.BlobProperty()
    immagine_mimetype = ndb.StringProperty()