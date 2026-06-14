from abc import ABC, abstractmethod


class ModeLivraison(ABC):
    """Contrat abstrait pour tout mode de livraison d'un colis."""

    @abstractmethod
    def cout(self, poids_kg):
        """Calcule le coût de la livraison."""
        raise NotImplementedError

    @abstractmethod
    def delai_estime(self):
        """Retourne le délai estimé."""
        raise NotImplementedError

    @staticmethod
    def _valider_poids(poids_kg):
        """Valide le poids du colis."""
        if isinstance(poids_kg, bool) or not isinstance(poids_kg, (int, float)):
            raise TypeError("Le poids doit être un nombre (int ou float).")

        if poids_kg <= 0:
            raise ValueError("Le poids doit être strictement positif.")

    def recapitulatif(self, poids_kg):
        """Construit une ligne récapitulative."""
        return (
            f"{type(self).__name__} : {self.cout(poids_kg):.2f} EUR, "
            f"livraison en {self.delai_estime()} jour(s) ouvré(s)"
        )

    def __repr__(self):
        """Représentation de l'objet."""
        return f"{type(self).__name__}()"


class LivraisonStandard(ModeLivraison):
    """Livraison standard à domicile."""

    TARIF_BASE = 4.99
    TARIF_PAR_KG = 1.50
    DELAI_JOURS = 3

    def cout(self, poids_kg):
        """Calcule le coût standard."""
        self._valider_poids(poids_kg)
        return self.TARIF_BASE + self.TARIF_PAR_KG * poids_kg

    def delai_estime(self):
        """Retourne le délai standard."""
        return self.DELAI_JOURS


class LivraisonExpress(ModeLivraison):
    """Livraison express avec supplément."""

    TARIF_BASE = 4.99
    TARIF_PAR_KG = 1.50
    DELAI_JOURS = 1

    def __init__(self, supplement=10.0):
        """Initialise le supplément express."""
        super().__init__()

        if isinstance(supplement, bool) or not isinstance(
            supplement, (int, float)
        ):
            raise TypeError("Le supplément doit être un nombre.")

        if supplement < 0:
            raise ValueError("Le supplément doit être positif ou nul.")

        self._supplement = supplement

    @property
    def supplement(self):
        """Retourne le supplément."""
        return self._supplement

    def cout(self, poids_kg):
        """Calcule le coût express."""
        self._valider_poids(poids_kg)

        return (
            self.TARIF_BASE
            + self.TARIF_PAR_KG * poids_kg
            + self._supplement
        )

    def delai_estime(self):
        """Retourne le délai express."""
        return self.DELAI_JOURS


class PointRelais(ModeLivraison):
    """Livraison en point relais."""

    TARIF_FORFAIT = 3.50
    DELAI_JOURS = 4

    def __init__(self, nom_reseau):
        """Initialise le réseau de relais."""
        super().__init__()

        if not isinstance(nom_reseau, str):
            raise TypeError("Le nom du réseau doit être une chaîne.")

        if nom_reseau.strip() == "":
            raise ValueError("Le nom du réseau ne peut pas être vide.")

        self._nom_reseau = nom_reseau

    @property
    def nom_reseau(self):
        """Retourne le nom du réseau."""
        return self._nom_reseau

    def cout(self, poids_kg):
        """Coût forfaitaire."""
        self._valider_poids(poids_kg)
        return self.TARIF_FORFAIT

    def delai_estime(self):
        """Retourne le délai du point relais."""
        return self.DELAI_JOURS


class RetraitMagasin:
    """Intrus du duck typing."""

    def cout(self, poids_kg):
        """Retrait gratuit."""
        ModeLivraison._valider_poids(poids_kg)
        return 0.0

    def delai_estime(self):
        """Retrait immédiat."""
        return 0


def comparer_livraisons(modes, poids_kg):
    """Compare plusieurs modes de livraison."""

    lignes = []

    for mode in modes:
        lignes.append(
            f"{type(mode).__name__} : "
            f"{mode.cout(poids_kg):.2f} EUR en "
            f"{mode.delai_estime()} jour(s)"
        )

    return "\n".join(lignes)


if __name__ == "__main__":

    print("=== Recapitulatifs ===")
    modes = [
        LivraisonStandard(),
        LivraisonExpress(),
        PointRelais("RelaisColis")
    ]

    for mode in modes:
        print(mode.recapitulatif(2.5))

    print("\n=== Comparaison (duck typing) ===")

    modes = [
        LivraisonStandard(),
        LivraisonExpress(12.0),
        PointRelais("RelaisColis"),
        RetraitMagasin()
    ]

    print(comparer_livraisons(modes, 2.5))

    print("\n=== Vérification isinstance ===")
    print(isinstance(LivraisonStandard(), ModeLivraison))
    print(isinstance(RetraitMagasin(), ModeLivraison))