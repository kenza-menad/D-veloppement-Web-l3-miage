
   
        function toggleReponse(id) {
            var reponse = document.getElementById(id);
            if (reponse.style.display === "none") {
                reponse.style.display = "block";
            } else {
                reponse.style.display = "none";
            }
        }
   
    function sendFeedback(feedback) {
        // Afficher le message de remerciement
        var thankYouMessage = document.getElementById('thankYouMessage');
        thankYouMessage.style.display = 'block';
        
        // Désactiver les boutons après la sélection
        var feedbackButtons = document.getElementsByClassName('feedbackButton');
        for (var i = 0; i < feedbackButtons.length; i++) {
            feedbackButtons[i].disabled = true;
        }
    
        // Envoyer le feedback à un serveur ou traiter localement, par exemple :
        console.log("Feedback : " + feedback);
    }
    
    // Parissssssssss

    