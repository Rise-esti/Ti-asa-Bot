
'use strict';
// le token de la page
const PAGE_ACCESS_TOKEN = "EAAgl1cfQLIIBAEWJRVZAUUiHPqcR5CTb2TtOlrcbjr7mwqGOgEQB7I9nE0yUS0xkFACZAJsKpc98BQif0uOZBhKJGMlrvADJpocC6hN7nAll9k85ukW3DI6rRJNyBNR0PJcZAv5c1EM5L21XvcZAUM9ecxyxZC3seZCQZBob1WWeZCQZDZD";
// On va importer les dependances ci-dessus
const 
  request = require('request'),
  express = require('express'),
  body_parser = require('body-parser'),
  app = express().use(body_parser.json()); // creates express http server

// creer un serveur d ecoute pour les envoyer de Facebook
app.listen(process.env.PORT || 1337, () => console.log('webhook est en ecoute'));

//fonction lanceons en cas de requetes de type POST
app.post('/webhook', (req, res) => {  

  // Parser le corps de la requete
  let body = req.body;

 
  if (body.object === 'page') {

    body.entry.forEach(function(entry) {

      // recuperer l evenement qui a declenché l envoie 
      let webhook_event = entry.messaging[0];
      console.log(webhook_event);


      // recupere l'ID de la personne qui a envoyer le message au bot
      let sender_psid = webhook_event.sender.id;
      console.log('Sender ID: ' + sender_psid);

      // cas d u message
      if (webhook_event.message) {
        handleMessage(sender_psid, webhook_event.message);  
      // cas d'un evenement 
      } else if (webhook_event.postback) {
        
        handlePostback(sender_psid, webhook_event.postback);
      }
      
    });
    // renvoie un reponse 200 pour tous evenements
    res.status(200).send('EVENT_RECEIVED');

  } else {
    // 404 erreur si c estpas pour la page 
    res.sendStatus(404);
  }

});

//fonction pour les request get 
app.get('/webhook', (req, res) => {
  
  // le token pour les requets get 
  const VERIFY_TOKEN = "mytoken";
  
  // Parser les verifications de requetes
  let mode = req.query['hub.mode'];
  let token = req.query['hub.verify_token'];
  let challenge = req.query['hub.challenge'];
    
  // verificer si les token ont ete envoyer 
  if (mode && token) {
  
    // verifie si le token est vraie 
    if (mode === 'subscribe' && token === VERIFY_TOKEN) {
      
      // envoie un ok que le requet est confirmer 
      console.log('WEBHOOK_VERIFIED');
      res.status(200).send(challenge);
    
    } else {
      // le token est faux donc est retour 403
      res.sendStatus(403);      
    }
  }
});

function handleMessage(sender_psid, received_message) {
  let response;
  let bot_reponse;
  
  // si le message est un fichier texte
  if (received_message.text) {    
    // creer alors le message de retour
	
	request.post({
		headers: {'content-type' : 'application/x-www-form-urlencoded'},
		url: 'http://localhost:5000/bot',
		body: `text="${received_message.text}"`, 
	function(error, response, body){
		//console.log(body);
		if (!error){
			bot_reponse = body;
		}
		else{
			bot_reponse = "Désolé il y a une erreur dans mon programme, Veuillez avertir un des Admin, https://ti-asa.esti.mg#team, Merci ";
		}
	}
}

);
    response = {
      "text": bot_reponse
    }
  } else if (received_message.attachments) {
    // cas d'envoie d'une piece jointe 
    let attachment_url = received_message.attachments[0].payload.url;
    // envoye du type de fichier que la personne a envoyer
    response = {
      "attachment": {
        "type": "template",
        "payload": {
          "template_type": "generic",
          "elements": [{
            "title": "Is this the right picture?",
            "subtitle": "Tap a button to answer.",
            "image_url": attachment_url,
            "buttons": [
              {
                "type": "postback",
                "title": "Yes!",
                "payload": "yes",
              },
              {
                "type": "postback",
                "title": "No!",
                "payload": "no",
              }
            ],
          }]
        }
      }
    }
  } 
  
  // envoie du message de retour 
  callSendAPI(sender_psid, response);    
}

function handlePostback(sender_psid, received_postback) {
  console.log('ok')
   let response;
  // prendre le payyload pour le postback
  let payload = received_postback.payload;

  // faire la reponse en fonction de celle ci 
  if (payload === 'yes') {
    response = { "text": "Merci!" }
  } else if (payload === 'no') {
    response = { "text": "Oops, Essayer une autre image." }
  }
  //envoyer la reponse 
  callSendAPI(sender_psid, response);
}

function callSendAPI(sender_psid, response) {
  // contruit le destinataire du message
  let request_body = {
    "recipient": {
      "id": sender_psid
    },
    "message": response
  }

  // envoie la requete http a messenger pour transferer a la personne
  request({
    "uri": "https://graph.facebook.com/v2.6/me/messages",
    "qs": { "access_token":  "EAAgl1cfQLIIBAEWJRVZAUUiHPqcR5CTb2TtOlrcbjr7mwqGOgEQB7I9nE0yUS0xkFACZAJsKpc98BQif0uOZBhKJGMlrvADJpocC6hN7nAll9k85ukW3DI6rRJNyBNR0PJcZAv5c1EM5L21XvcZAUM9ecxyxZC3seZCQZBob1WWeZCQZDZD"},
    "method": "POST",
    "json": request_body
  }, (err, res, body) => {
    if (!err) {
      console.log('message sent!')
    } else {
      console.error("Unable to send message:" + err);
    }
  }); 
}
