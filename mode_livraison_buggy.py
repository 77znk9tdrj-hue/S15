"""Code à diagnostiquer - LivraisonColisExpress incomplète (atelier S15).

Ce fichier est AUTONOME : il contient sa propre copie de la classe
abstraite ModeLivraison, pour pouvoir être exécuté tel quel dès le
début de l'atelier, avant tout autre travail.

Un développeur a voulu ajouter un mode de livraison express premium,
mais son code refuse de s'exécuter. À l'instanciation, Python lève
une TypeError. Votre tâche (exercice 1) : nommer le mécanisme en jeu
et le corriger.

Programmation Orientée Objet - EICPN 2025-2026.
"""

from abc import ABC, abstractmethod


class ModeLivraison(ABC):
    """Contrat abstrait pour tout mode de livraison (copie autonome)."""

    @abstractmethod
    def cout(self, poids_kg):
        """Coût de la livraison en euros."""
        raise NotImplementedError

    @abstractmethod
    def delai_estime(self):
        """Délai estimé en jours ouvrés."""
        raise NotImplementedError


class LivraisonColisExpress(ModeLivraison):
    """Mode de livraison express premium (version incomplète).
    """

    TARIF_BASE = 6.99
    TARIF_PAR_KG = 2.00

    def cout(self, poids_kg):
        """Coût premium au poids."""
        return self.TARIF_BASE + self.TARIF_PAR_KG * poids_kg
    def delai_estime(self):
        return 1

if __name__ == "__main__":
    # L'instanciation échoue AVANT même tout appel de méthode
    mode = LivraisonColisExpress()
    print(mode.cout(3.0))