# LAZAudio
LAZAudio ist ein Studentenprojekt von Lars Dörper und Zahit Kiziltepe, dass im Rahmen des Kurses Machine Learing entstanden ist. Dabei ging es darum ein Verständnis für neuronale Netzwerke zu bekommen und mit diesen zu Arbeiten. In unserem Projekt haben wir uns zur Aufgabe gemacht eine Applikation zu entwickeln, die Sprachnachrichten oder -memos in Text zu übersetzen und zusammenzufassen, was mit der Analyse des Textes auf Schlagwörter hin, gemacht wird. 

## Front-End
Im Front-End der Applikation arbeiteten wir mit einer HTML und CSS Ausgabe unserer Inhalte. Unterstuützt wird es in seiner Funktion durch JavaScript.

## Framework
Um aus unserem Web - Front-End ein zu machen, benutzten wir in unserem Projekt Apache Cordova. Installiert werden kann Apache Cordova über Node.js mit
```
npm install -g Cordova
```
Zu Beginn initiierten wir das Projekt unter dem Namen LAZAudio mit dem Befehl 
```
cordova create Projektname
```
Um Cordova auf dem Smartphone nutzen zu können musste zusätzlich Adroid als Platform installieren
```
cordova platform add Android
```
In den, durch die Befehle erzeugten Ordner und Datein, haben wir nun allso begonnne unser Application aufzubauen.

## API's 
Serverseitig nutzten wir für die Texterkennenung die API von speechtext.ai, die für uns die Transkription der Sprachnachrichten übernahm. Für die Analyse des Texte nutzten wir zusätzlich die Natural-Language-Understanding - API von IBM Watson. Beide unserer API's nutzten wir in Python, damit wir sie in unserem Server ansprechen konnten. 

## Networking
Für die Kommunikation zwischen unserem Server und dem Client, welchen unsere mobile Applikation darstellt, nutzten wir das TCP-Protokoll. In unserem Server nutzen wir dafür das Socket-Modul, welches in Python vorinstalliet ist. Clientseitig mussten wir in Cordova zusätzlich ein Plug-In installieren, mit
```
cordova plugin add cz.blocshop.socketsforcordova
```
um das Protokoll nutzen zu können und die Verbingung herstellen zu können und die Sprachnachricht versenden zu können.

## Server
Unseren Server haben wir in Python aufgebaut. Dieser hatte die Aufgabe die empfangenen Daten zu verwalten, an die API's weiterzugeben und die Ergebnisse an die App zurück zu senden. 
