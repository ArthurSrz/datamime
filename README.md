<p align="center">
  <img src="https://raw.githubusercontent.com/ArthurSrz/datamime/main/logo_datamime.png" alt="animated" />
</p>


## WTF Datamime ?

Datamime adresse le problème du manque récurrent de jeux de données ouverts, de volume et de qualité suffisante pour permettre le développement de modèles ou d'applications (notamment dans le cadre de Hackathon). Datamime propose un générateur de données mimétiques, qui, sur la base d'un petit échantillon ou tout simplement d'un modèle, voire d'un début d'embryon de connaissances sur un jeu de données, permet de produire un jeu de données suffisamment volumineux pour initier un travail de développement technique. 


## Datamime : pourquoi et pour qui ? 

#### Une alternative à la désillusion post-"Des données, j'en ai plein"...

On rencontre souvent des collectivités, des entreprises qui organisent ou participent à un hackathon/datathon parce que :

> "Des données, on en a plein et on ne sait pas quoi en faire"
>
> **Jojo Data Manager**, 3 mois avant le hackathon

Alors qu'en réalité : 

> "Avec mes équipes, nous n'avons pas le temps nécessaire pour extraire et créer les données. Vous comprenez, c'est compliqué. Mais je peux vous transmettre un fichier excel de 10 lignes"
>
> **Jojo Data Manager**, 3 jours avant le hackathon


#### Pour tout ceux qui ne veulent pas attendre de disposer de vraies données 

Datamime s'adresse aux impatients, à ceux qui pensaient avoir des données et qui finalement doivent attendre longtemps (très longtemps, trop longtemps) pour commencer à bosser sur leur appli ou sur leur modèle. 

<p align="center">
  <img src="https://media.giphy.com/media/EZAofOteI32AzIa6Db/giphy.gif" alt="animated" />
</p>


## Datamime : comment ça marche ? 


1.(si vous n'avez pas d'échantillon) Crééz un tableur ou un fichier .csv dans lequel vous mettez des valeurs fictives mais cohérentes par rapport au phénomène temporel représenté

> **Exemple**
> 
> Vous voulez travailler avec des données sur la concentration de polluants atmosphériques heure par heure. Vous savez que la concentration est corrélée avec l'activité humaine (intense le jour, faible la nuit). Dès lors, vous pouvez créer un tableur dans lequel les valeurs de concentration augmente de 9h à 16h et baisse de 16h à 9h. 

2.(si vous avez un échantillon) Uploadez l'échantillon dans Datamime

3.Choisissez la variable/colonne qui contient la date et l'heure et renseignez la dans la liste déroulante "Time variable"

> **Exemple**
> 
> La date et l'heure à laquelle la concentration de polluants atmosphériques est mesurée se trouve dans la colonne "date_debut". Dans la liste déroulante "Time variable", choisissez "date_debut"

4.Choisissez les caractéristiques qui déterminent la série temporelle et renseignez les dans la liste déroulante "Sub samples". Plus vous sélectionnerez de caractéritiques, plus les modèles qui seront générés seront spécifiques (voir étape 6)

> **Exemple**
> 
> A chaque moment de mesure (voir variable "date_debut") est spécifié la station de mesure et le type de polluant atmosphérique. Renseignez ces valeurs dans la liste déroulante "Sub samples". En renseignant ces valeurs, Datamime va générer des modèle pour chaque station de mesure et pour chaque type de polluant.

5.Choisissez la variable qui contient la valeur mesurée et renseignez la dans la liste déroulante "Value"

> **Exemple**
> 
> La valeur qui mesure la concentration de polluants atmosphérique se trouve dans la variable "valeur". Renseignez la dans la liste déroulante "Value"


6.Datamime créé autant de modèles que de séries temporelles présentes dans le jeu de données. Les modèles s'affichent sous l'onglet "Dataset description" dans l'interface principale

> **Exemple**
> 
> Datamime va créer un modèle par station et par polluant atmosphérique. Il y a aura donc un modèle pour la concentration de CO2 à la station de mesure du Havre, un modèle pour la concentration de NO2 à la station de Rouen, etc. 

7.A partir du modèle créé, Datamime va générer un nouveau jeu de données. Vous pouvez le type de données générées ainsi que le volume dont vous avez besoin. Pour cela, 


