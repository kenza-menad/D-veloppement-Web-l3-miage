from flask import Flask, render_template, request, redirect, url_for, flash, session
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_folder="static/", static_url_path="/static")
app.secret_key = "votre_cle_secrete"  # Clé secrète pour les sessions

# Configuration de la base de données
db_config = {
    "host": "localhost",
    "database": "travel_agency",
    "user": "kenza",  # Nom d'utilisateur PostgreSQL
    "password": "kenza"  # Mot de passe PostgreSQL
}

# Fonction pour obtenir une connexion à la base de données
def get_db_connection():
    try:
        conn = psycopg2.connect(**db_config)
        return conn
    except psycopg2.Error as e:
        print(f"Erreur de connexion à la base de données : {e}")
        return None
@app.route("/")
def index():
    return redirect(url_for("travel"))
# Page d'inscription
@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    if request.method == "POST":
        nom = request.form.get("nom")
        prenom = request.form.get("prénom")
        email = request.form.get("adresse mail")
        mot_de_passe = request.form.get("mot de passe")
        numero = request.form.get("numéro")

        if len(mot_de_passe) < 6:
            return {"error": "Le mot de passe doit contenir au moins 6 caractères."}, 400

        mot_de_passe_hash = generate_password_hash(mot_de_passe)

        conn = get_db_connection()
        if conn is None:
            return {"error": "Erreur de connexion à la base de données."}, 500

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM utilisateurs WHERE email = %s", (email,))
            if cursor.fetchone():
                return {"error": "Cet email est déjà utilisé."}, 409
            else:
                cursor.execute(
                    """
                    INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, telephone)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (nom, prenom, email, mot_de_passe_hash, numero),
                )
                conn.commit()
                return redirect(url_for("travel"))
        except Exception as e:
            print(f"Erreur lors de l'insertion d'utilisateur : {e}")
            return {"error": "Une erreur est survenue."}, 500
        finally:
            cursor.close()
            conn.close()

    return render_template("inscription.html")

# Page de connexion
@app.route("/compte", methods=["GET", "POST"])
def compte():
    if request.method == "POST":
        email = request.form.get("email")
        mot_de_passe = request.form.get("mot de passe")

        conn = get_db_connection()
        if conn is None:
            return {"error": "Erreur de connexion à la base de données."}, 500

        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("SELECT * FROM utilisateurs WHERE email = %s", (email,))
            utilisateur = cursor.fetchone()

            if utilisateur:
                if check_password_hash(utilisateur["mot_de_passe"], mot_de_passe):
                    session["utilisateur_id"] = utilisateur["id_utilisateur"]
                    session["nom"] = utilisateur["nom"]
                    session["email"] = utilisateur["email"]
                    return redirect(url_for("travel"))

                else:
                    return {"error": "Mot de passe incorrect."}, 401
            else:
                return {"error": "Cet email n'est pas enregistré."}, 404
        except Exception as e:
            print(f"Erreur lors de la connexion : {e}")
            return {"error": "Une erreur est survenue."}, 500
        finally:
            cursor.close()
            conn.close()

    return render_template("compte.html")

# Page de réservation
@app.route("/reservation", methods=["GET", "POST"])
def reservation():
    if request.method == "POST":
        try:
            nom = request.form.get("nom", "").strip()
            prenom = request.form.get("prenom", "").strip()
            email = request.form.get("email", "").strip()
            telephone = request.form.get("telephone", "").strip()
            pays_residence = request.form.get("pays_residence", "").strip()
            code_postal = request.form.get("code_postal", "").strip()
            date_depart = request.form.get("date_depart", "").strip()
            date_retour = request.form.get("date_retour", "").strip()
            nb_adultes = int(request.form.get("nb_adultes", 0))
            nb_enfants = int(request.form.get("nb_enfants", 0))
            nb_bebes = int(request.form.get("nb_bebes", 0))
            classe = request.form.get("classe", "").strip()
            bagages_main = int(request.form.get("bagages_main", 0))
            bagages_soute = int(request.form.get("bagages_soute", 0))
            id_utilisateur = session.get("utilisateur_id")

            if not all([nom, prenom, email, telephone, pays_residence, code_postal, date_depart, id_utilisateur]):
                return {"error": "Tous les champs obligatoires doivent être remplis."}, 400

            conn = get_db_connection()
            if conn is None:
                return {"error": "Erreur de connexion à la base de données."}, 500

            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO reservation (
                    id_utilisateur, nom, prenom, email, telephone, pays_residence, code_postal,
                    date_depart, date_retour, nb_adultes, nb_enfants, nb_bebes, classe,
                    bagages_main, bagages_soute
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    id_utilisateur, nom, prenom, email, telephone, pays_residence, code_postal,
                    date_depart, date_retour, nb_adultes, nb_enfants, nb_bebes, classe,
                    bagages_main, bagages_soute
                )
            )
            conn.commit()
            return redirect(url_for("reservation"))
        except ValueError:
            return {"error": "Erreur dans les données saisies."}, 400
        except Exception as e:
            print(f"Erreur lors de l'insertion de la réservation : {e}")
            return {"error": "Une erreur est survenue."}, 500
        finally:
            if conn:
                cursor.close()
                conn.close()

    return render_template("reservation.html")

# Page de contact
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        nom = request.form.get("nom")
        email = request.form.get("email")
        probleme = request.form.get("probleme")

        if not nom or not email or not probleme:
            return {"error": "Tous les champs sont obligatoires."}, 400

        conn = get_db_connection()
        if conn is None:
            return {"error": "Erreur de connexion à la base de données."}, 500

        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO contact (nom, email, probleme)
                VALUES (%s, %s, %s)
                """,
                (nom, email, probleme)
            )
            conn.commit()
            return redirect(url_for("contact"))
        except Exception as e:
            print(f"Erreur lors de l'enregistrement du contact : {e}")
            return {"error": "Une erreur est survenue."}, 500
        finally:
            cursor.close()
            conn.close()

    return render_template("contact.html")

# Page des avis
@app.route("/avis", methods=["GET", "POST"])
def avis():
    if request.method == "POST":
        nom = request.form.get("nom")
        prenom = request.form.get("prenom")
        adresse = request.form.get("adresse")
        email = request.form.get("email")
        pays = request.form.get("pays")
        departement = request.form.get("departement")
        code_postal = request.form.get("code_postal")
        avis_texte = request.form.get("avis")

        if not all([nom, prenom, adresse, email, pays, departement, code_postal, avis_texte]):
            return {"error": "Tous les champs sont obligatoires."}, 400

        conn = get_db_connection()
        if conn is None:
            return {"error": "Erreur de connexion à la base de données."}, 500

        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO avis (nom, prenom, adresse, email, pays, departement, code_postal, avis)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (nom, prenom, adresse, email, pays, departement, code_postal, avis_texte)
            )
            conn.commit()
            return redirect(url_for("avis"))
        except Exception as e:
            print(f"Erreur lors de l'insertion de l'avis : {e}")
            return {"error": "Une erreur est survenue."}, 500
        finally:
            cursor.close()
            conn.close()

    return render_template("avis.html")

# Page de paiement
@app.route("/paiement", methods=["GET", "POST"])
def paiement():
    if request.method == "POST":
        email = request.form.get("email")
        telephone = request.form.get("phone")
        numero_carte = request.form.get("card-number")
        date_expiration = request.form.get("expiry")
        cvc = request.form.get("cvc")
        titulaire_carte = request.form.get("cardholder-name")
        adresse_facturation = f"{request.form.get('address-line-1')}, {request.form.get('address-line-2') or ''}"
        code_postal = request.form.get("postal-code")
        ville = request.form.get("city")
        pays = request.form.get("billing-country")

        if not all([email, numero_carte, date_expiration, cvc, adresse_facturation, pays]):
            return {"error": "Tous les champs requis doivent être remplis."}, 400

        conn = get_db_connection()
        if conn is None:
            return {"error": "Erreur de connexion à la base de données."}, 500

        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO paiements (
                    email, telephone, numero_carte, date_expiration, cvc, 
                    titulaire_carte, adresse_facturation, code_postal, ville, pays
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (email, telephone, numero_carte, date_expiration, cvc, titulaire_carte,
                 adresse_facturation, code_postal, ville, pays)
            )
            conn.commit()
            return redirect(url_for("travel"))
        except Exception as e:
            print(f"Erreur lors de l'enregistrement du paiement : {e}")
            return {"error": "Une erreur est survenue lors du traitement du paiement."}, 500
        finally:
            cursor.close()
            conn.close()

    return render_template("paiement.html")


@app.route("/travel", methods=["GET"])
def travel():
    return render_template("travel/index.html")



@app.route("/maldives", methods=["GET"])
def desination1():
    return render_template("maldives.html")



@app.route("/Suisse", methods=["GET"])
def desination2():
    return render_template("Suisse.html")


@app.route("/grece", methods=["GET"])
def desination3():
    return render_template("grece.html")


@app.route("/Espagne", methods=["GET"])
def desination4():
    return render_template("Espagne.html")


@app.route("/Thailande", methods=["GET"])
def desination5():
    return render_template("Thailande.html")

#hotel_Maldives
@app.route("/hotel_Maldives", methods=["GET"])
def desination6():
    return render_template("hotel_Maldives.html")



#hotel_Grece
@app.route("/hotel_Grece", methods=["GET"])
def desination7():
    return render_template("hotel_Grece.html")


#hotel_Suisse
@app.route("/hotel_Suisse", methods=["GET"])
def desination8():
    return render_template("hotel_Suisse.html")

#hotel_Espagne
@app.route("/hotel_Espagne", methods=["GET"])
def desination9():
    return render_template("hotel_Espagne.html")


#hotel_Thailande
@app.route("/hotel_Thailande", methods=["GET"])
def desination10():
    return render_template("hotel_Thailande.html")

#page Apropos
@app.route("/about us", methods=["GET"])
def desination11():
    return render_template("about us.html")

#page About
@app.route("/concept", methods=["GET"])
def desination12():
    return render_template("concept.html")


if __name__ == "__main__":
    app.run(debug=True)


