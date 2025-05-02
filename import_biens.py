import pandas as pd
from app import db, Bien, app

df = pd.read_excel('excel.xlsx')

# Nettoyage des noms de colonnes 
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(',', '')

def importer_biens():
    with app.app_context():
        for index, row in df.iterrows():
            
            matricule = str(row['MATRICULE']) if pd.notna(row['MATRICULE']) else ''
            etat = str(row['ETAT/PANNES CONSTATEES']) if pd.notna(row['ETAT/PANNES CONSTATEES']) else ''
            prix_depart = float(row['PRIX DE DEPART']) if pd.notna(row['PRIX DE DEPART']) else 0.0

            bien = Bien(
                numero=str(row['N.']),
                denomination=str(row['DENOMINATION']),
                type=str(row['TYPE']),
                matricule=matricule,
                etat=etat,
                prix_depart=prix_depart,
                photo=''
            )

            # la session et valider les changements
            db.session.add(bien)

        db.session.commit()
        print("Importation terminée avec succès !")

if __name__ == "__main__":
    importer_biens()
