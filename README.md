MARCEL WANKO
# Programmation orientée objet - Soirée 15

## Duck typing et classes abstraites

Dépôt de l'atelier de la soirée 15. Il porte sur le **duck typing** et les **classes abstraites** (`abc.ABC`, `@abstractmethod`), illustrés sur une famille de modes de livraison d'un colis.

L'énoncé complet et les consignes détaillées se trouvent dans **`POO_S15_atelier_TP.pdf`**. Lisez-le en premier : c'est la référence unique pour les spécifications (valeurs, formats, comportements attendus).

> Vous travaillerez dans **VS Code**. Toutes les opérations Git de cet atelier peuvent se faire à la souris, depuis l'interface de VS Code, sans taper de commandes. Les commandes équivalentes sont indiquées en complément pour ceux qui préfèrent le terminal.

---

## Mise en route

1. **Forkez** ce dépôt (bouton *Fork* en haut à droite). Vous obtenez votre propre copie.
2. **Clonez votre fork** dans VS Code :
   - Ouvrez la palette de commandes : `Ctrl+Shift+P` (ou `Cmd+Shift+P` sur Mac).
   - Tapez **`Git: Clone`**, validez, puis collez l'URL de **votre** fork.
   - Choisissez un dossier de destination, puis cliquez sur **Ouvrir** quand VS Code le propose.
   - *Équivalent terminal :* `git clone <url-de-votre-fork>`
3. Dans l'explorateur de VS Code, **renommez** `mode_livraison_squelette.py` en **`mode_livraison.py`** (clic droit sur le fichier, *Renommer*).

---

## Fichiers fournis

| Fichier | Rôle |
|---|---|
| `POO_S15_atelier_TP.pdf` | L'énoncé complet des cinq exercices. À lire en premier. |
| `mode_livraison_squelette.py` | Point de départ. À **renommer en `mode_livraison.py`** avant de le compléter. La classe abstraite `ModeLivraison` y est fournie en entier : **ne la modifiez pas**. |
| `mode_livraison_buggy.py` | Support du diagnostic de l'exercice 1. Fichier autonome, exécutable tel quel. |

---

## Travail à produire

À compléter dans votre fork, puis à committer et pousser :

| Fichier | Contenu |
|---|---|
| `mode_livraison.py` | Le squelette renommé et complété (sous-classes, intrus, client polymorphe). |
| `test_mode_livraison.py` | Votre suite de tests, **créée par vous** (aucun squelette n'est fourni pour ce fichier). |
| `reponses.txt` | Vos réponses écrites : diagnostic de l'exercice 1, justifications des exercices 3 et 5. |

Le détail de chaque exercice et les spécifications précises sont dans le PDF. Ils ne sont pas répétés ici.

---

## Conventions à respecter

- Python 3. Respect de la PEP 8 : `PascalCase` pour les classes, `snake_case` pour les méthodes et attributs.
- Une docstring au format Google sur chaque classe et chaque méthode.
- Texte français accentué dans les docstrings, commentaires et messages d'erreur ; identifiants en ASCII (sans accent).
- Ne modifiez pas les fichiers fournis, à l'exception du squelette que vous renommez.
- Travail individuel.

---

## Committer votre travail au fil des exercices

Committez **après chaque exercice** plutôt qu'une seule fois à la fin : votre historique reste lisible et vous ne risquez pas de tout perdre. Dans VS Code, tout se fait depuis le panneau **Contrôle de code source** :

1. Ouvrez le panneau **Contrôle de code source** (icône en forme de branches dans la barre latérale gauche, ou `Ctrl+Shift+G`).
2. Vos fichiers modifiés apparaissent sous **Modifications**.
3. Survolez un fichier et cliquez sur le **`+`** pour l'indexer (*stage*), ou sur le `+` de la section pour tout indexer.
4. Saisissez un **message de commit** clair dans la zone de texte en haut du panneau.
5. Cliquez sur **Valider** (le bouton avec la coche `✓`, ou `Ctrl+Entrée`).
6. Cliquez sur **Synchroniser les modifications** pour envoyer vos commits vers votre fork.

*Équivalent terminal :*
```
git add <fichiers>
git commit -m "votre message"
git push
```

### Cadence de commits suggérée

| Après... | Fichiers concernés | Message de commit suggéré |
|---|---|---|
| Exercice 1 | `reponses.txt` | `Exercice 1 : diagnostic du contrat manquant` |
| Exercice 2 | `mode_livraison.py` | `Exercice 2 : hiérarchie ModeLivraison` |
| Exercice 3 | `mode_livraison.py`, `reponses.txt` | `Exercice 3 : duck typing et client polymorphe` |
| Exercice 4 | `test_mode_livraison.py` | `Exercice 4 : suite de tests` |
| Exercice 5 | `reponses.txt` | `Exercice 5 : justifications de conception` |

Un message court, à l'impératif ou nominal, qui dit ce que le commit apporte : c'est l'habitude à prendre.

---

## Vérifier votre travail

Lancer la suite de tests, depuis le terminal intégré de VS Code (`Terminal > Nouveau terminal`) :
```
python -m unittest test_mode_livraison.py -v
```
Tous vos tests doivent passer au vert.

Pour l'exercice 1, exécutez le fichier fourni et observez le message d'erreur :
```
python mode_livraison_buggy.py
```

---

## Remise

> *Modalité à confirmer par l'enseignant (par exemple : pousser vos trois fichiers dans votre fork et communiquer l'URL de celui-ci, ou dépôt sur la plateforme du cours).*

Assurez-vous d'avoir **synchronisé** votre dernier commit (étape 6 ci-dessus) avant la date de remise. Vous pouvez vérifier sur la page web de votre fork que les trois fichiers attendus y figurent bien.

---

## En cas de blocage

Relisez d'abord l'énoncé (`POO_S15_atelier_TP.pdf`), puis sollicitez l'enseignant. Coder un énoncé mal lu coûte plus cher que relire l'énoncé.

---

*EICPN - Enseignement pour Adultes. Programmation orientée objet (UAA 7525 21 U32 D3).*
