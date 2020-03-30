import base64
import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', password='3754', database='Project')
cur = conn.cursor()
cur.execute("CREATE TABLE Morphemes (MorphemeID INTEGER PRIMARY KEY AUTO_INCREMENT, Type_of_morpheme VARCHAR(10), Part_of_speech VARCHAR(50), Morpheme VARCHAR(20))")
var1 = 'еньк'.encode("utf-8")
var2 = 'юш'.encode("utf-8")
var3 = 'ш'.encode("utf-8")
var4 = 'к'.encode("utf-8")
v641 = str(base64.b64encode(var1),)
v642 = str(base64.b64encode(var2),)
v643 = str(base64.b64encode(var3),)
v644 = str(base64.b64encode(var4),)
suf = 'suffix'
aan = 'adjective/adverb/noun'
noun = 'noun'
und = 'undefined'
strvar0 = """INSERT INTO Morphemes(Type_of_morpheme, Part_of_speech, Morpheme) VALUES (%s, %s, %s)"""
strvar1 = """INSERT INTO Morphemes(Type_of_morpheme, Part_of_speech, Morpheme) VALUES (%s, %s, %s)"""
strvar2 = """INSERT INTO Morphemes(Type_of_morpheme, Part_of_speech, Morpheme) VALUES (%s, %s, %s)"""
strvar3 = """INSERT INTO Morphemes(Type_of_morpheme, Part_of_speech, Morpheme) VALUES (%s, %s, %s)"""
strvar4 = """INSERT INTO Morphemes(Type_of_morpheme, Part_of_speech, Morpheme) VALUES (%s, %s, %s)"""
cur.execute(strvar0, ((und), (und), (und)))
cur.execute(strvar1, ((suf), (aan), (v641)))
cur.execute(strvar2, ((suf), (noun), (v642)))
cur.execute(strvar3, ((suf), (noun), (v643)))
cur.execute(strvar4, ((suf), (noun), (v644)))

cur.execute("CREATE TABLE Words (WordID INTEGER PRIMARY KEY AUTO_INCREMENT, Word VARCHAR(50), Emotion VARCHAR(11), Morpheme INTEGER, FOREIGN KEY (Morpheme) REFERENCES Morphemes(MorphemeID))")
var1 = 'маленький'.encode("utf-8")
var2 = 'кот'.encode("utf-8")
var3 = 'Антоша'.encode("utf-8")
var4 = 'диван'.encode("utf-8")
v641 = str(base64.b64encode(var1),)
v642 = str(base64.b64encode(var2),)
v643 = str(base64.b64encode(var3),)
v644 = str(base64.b64encode(var4),)
emo = 'emotive'
nemo = 'not emotive'
strvar0 = """INSERT INTO Words(Word, Emotion, Morpheme) VALUES (%s, %s, %s)"""
strvar1 = """INSERT INTO Words(Word, Emotion, Morpheme) VALUES (%s, %s, %s)"""
strvar2 = """INSERT INTO Words(Word, Emotion, Morpheme) VALUES (%s, %s, %s)"""
strvar3 = """INSERT INTO Words(Word, Emotion, Morpheme) VALUES (%s, %s, %s)"""
strvar4 = """INSERT INTO Words(Word, Emotion, Morpheme) VALUES (%s, %s, %s)"""
cur.execute(strvar0, ((und), (und), (1)))
cur.execute(strvar1, ((v641), (emo), (2)))
cur.execute(strvar2, ((v642), (nemo), (1)))
cur.execute(strvar3, ((v643), (emo), (4)))
cur.execute(strvar4, ((v644), (nemo), (1)))

cur.execute("CREATE TABLE Sentences (SentenceID INTEGER PRIMARY KEY AUTO_INCREMENT, Sentence VARCHAR(400), Emotion VARCHAR(11), Word INTEGER, FOREIGN KEY (Word) REFERENCES Words(WordID))")
var1 = 'Это не бред, именно в таком дурдоме и рос маленький мальчик, сын Санаевой.'.encode("utf-8")
var2 = 'Дома тихо, спокойно, кот рядом валяется, мурлычет.'.encode("utf-8")
var3 = 'Глупец! ― презрительно ответил маленький кот, наперед зная, что двуногий его не услышит.'.encode("utf-8")
var4 = 'Возьми и верни все себе.'.encode("utf-8")
v641 = str(base64.b64encode(var1),)
v642 = str(base64.b64encode(var2),)
v643 = str(base64.b64encode(var3),)
v644 = str(base64.b64encode(var4),)
strvar1 = """INSERT INTO Sentences(Sentence, Emotion, Word) VALUES (%s, %s, %s)"""
strvar2 = """INSERT INTO Sentences(Sentence, Emotion, Word) VALUES (%s, %s, %s)"""
strvar3 = """INSERT INTO Sentences(Sentence, Emotion, Word) VALUES (%s, %s, %s)"""
strvar4 = """INSERT INTO Sentences(Sentence, Emotion, Word) VALUES (%s, %s, %s)"""
strvar5 = """INSERT INTO Sentences(Sentence, Emotion, Word) VALUES (%s, %s, %s)"""
cur.execute(strvar1, ((v641), (emo), (2)))
cur.execute(strvar2, ((v642), (nemo), (3)))
cur.execute(strvar3, ((v643), (emo), (2)))
cur.execute(strvar4, ((v643), (emo), (3)))
cur.execute(strvar5, ((v644), (und), (1)))
conn.commit()

