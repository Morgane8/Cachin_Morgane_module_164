"""
    Fichier : gestion_disc_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterDisc(FlaskForm):
    """
        Dans le formulaire "disc_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    #nom_genre_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_genre_regexp = ""
    label_disc_wtf = StringField("Clavioter le label du disc ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_genre_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    weight_disc_wtf = StringField("Clavioter le poids ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                 Regexp(nom_genre_regexp,
                                                                        message="Pas de chiffres, de caractères "
                                                                                "spéciaux, "
                                                                                "d'espace à double, de double "
                                                                                "apostrophe, de double trait union")
                                                                 ])

    color_disc_wtf = StringField("Clavioter la couleur ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                      Regexp(nom_genre_regexp,
                                                                             message="Pas de chiffres, de caractères "
                                                                                     "spéciaux, "
                                                                                     "d'espace à double, de double "
                                                                                     "apostrophe, de double trait union")
                                                                      ])
    stamp_disc_wtf = StringField("Clavioter le stamp ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                      Regexp(nom_genre_regexp,
                                                                             message="Pas de chiffres, de caractères "
                                                                                     "spéciaux, "
                                                                                     "d'espace à double, de double "
                                                                                     "apostrophe, de double trait union")
                                                                      ])


    submit = SubmitField("Enregistrer disc")



class FormWTFUpdateDisc(FlaskForm):
    """
        Dans le formulaire "disc_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    #nom_genre_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_genre_update_regexp = ""
    label_disc_update_wtf = StringField("Clavioter le label du disc ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_genre_update_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    weight_disc_update_wtf = StringField("Clavioter le poids ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                 Regexp(nom_genre_update_regexp,
                                                                        message="Pas de chiffres, de caractères "
                                                                                "spéciaux, "
                                                                                "d'espace à double, de double "
                                                                                "apostrophe, de double trait union")
                                                                 ])

    color_disc_update_wtf = StringField("Clavioter la couleur ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                      Regexp(nom_genre_update_regexp,
                                                                             message="Pas de chiffres, de caractères "
                                                                                     "spéciaux, "
                                                                                     "d'espace à double, de double "
                                                                                     "apostrophe, de double trait union")
                                                                      ])
    stamp_disc_update_wtf = StringField("Clavioter le stamp ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                      Regexp(nom_genre_update_regexp,
                                                                             message="Pas de chiffres, de caractères "
                                                                                     "spéciaux, "
                                                                                     "d'espace à double, de double "
                                                                                     "apostrophe, de double trait union")
                                                                      ])

    submit = SubmitField("Update disc")


class FormWTFDeleteDisc(FlaskForm):
    """
        Dans le formulaire "disc_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_person".
    """
    nom_pers_delete_wtf = StringField("Effacer ce nom")
    submit_btn_del = SubmitField("Effacer nom")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
