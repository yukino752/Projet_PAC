import numpy as np  # Les outils mathématiques
import CoolProp.CoolProp as CP  # Les outils thermodynamiques
import CoolProp.Plots as CPP  # Les outils thermographiques
import matplotlib.pyplot as plt  # Les outils graphiques
from CoolProp.Plots import SimpleCompressionCycle
from CoolProp.CoolProp import PropsSI
import matplotlib.ticker as tck
import mysql.connector
from DB import connectDB ,QueryRequest, TupleToFloat

class DiagrammeEnthalpie:
    def __init__(self):
        self.FLUIDE = 'R134a'  # Le choix du fluide
        self.PLOGSCALE = True  # Axe en pression logarithmique ?
        self.ISO_T = True  # Veut-on des isothermes ? # température
        self.ISO_X = True  # et les isotitres ? # masse de vapeur / masse totale du fluide
        self.ISO_S = True  # et les isentropiques ? # entropie
        self.ISO_V = True  # et les isochores ? # volume densité
        # Les unités dans lesquelles on veut travailler (voir CONVERSION)
        self.unitP = 'bar'
        self.unitH = 'kJ'
        self.unitT = 'celsius'
        self.CONVERSION = {'bar': 1e5, 'kPa': 1e3, 'Pa': 1, 'kJ': 1e3, 'J': 1}
        self.dT = 10
        self.ds = 0.5e3
        self.val_x = np.linspace(0.1, 0.9, 9)
        self.x_to_show = None
        self.v_to_show = None
        self.UNITS = {'T': 'K', 'Q': '', 'S': 'kJ/K/kg', 'V': 'm$^3$/kg'}
        self.LABEL = {'T': 'T', 'Q': 'x', 'S': 's', 'V': 'v'}
        self.COLOR_MAP = {'T': 'Darkred',
                     'P': 'DarkCyan',
                     'H': 'DarkGreen',
                     'V': 'DarkBlue',
                     'S': 'DarkOrange',
                     'Q': 'black'}
        self.LINE_STYLE = {'T': '-.',
              'V': '--',
              'S': ':',
              'Q': '-'}
        self.p_min = 0.0
        self.p_max = 0.0
        self.h_min = 0.0
        self.h_max = 0.0
        self.t_min = 0.0
        self.t_max = 0.0
        self.t_triple = 0.0
        self.t_crit = 0.0
        self.val_t = None
        self.t_to_show = []
        self.s_triple_x0 = 0.0
        self.s_triple_x1 = 0.0
        self.val_s = None
        self.s_to_show = []
        self.v_crit = 0.0
        self.exp_min = 0
        self.exp_max = 0
        self.val_v = []
        self.v_triple_x1 = 0.0
        self.HP = 0.0
        self.BP = 0.0
        self.DetenteurE = 0.0
        self.DetenteurS = 0.0
        self.CompresseurE = 0.0
        self.CompresseurS = 0.0

    def get_kelvin(self):
        return 273.15

    def get_celsius(self):
        return -273.15

    def get_p_min(self):
        self.p_min = (CP.PropsSI(self.FLUIDE, 'ptriple') + 1) / self.CONVERSION[self.unitP]
        return self.p_min

    def get_p_max(self):
        self.p_max = (1.5 * CP.PropsSI(self.FLUIDE, 'pcrit')) / self.CONVERSION[self.unitP]
        return self.p_max

    def get_h_min(self):
        self.h_min = 0.9 * CP.PropsSI('H', 'P', self.get_p_min() * self.CONVERSION[self.unitP], 'Q', 0,  self.FLUIDE) / self.CONVERSION[self.unitH]
        return self.h_min

    def get_h_max(self):
        self.h_max = 1.5 * CP.PropsSI('H', 'P', self.get_p_min() * self.CONVERSION[self.unitP], 'Q', 1, self.FLUIDE) / self.CONVERSION[self.unitH]
        return self.h_max

    def get_t_triple(self):
        self.t_triple = CP.PropsSI(self.FLUIDE, 'Ttriple')
        return self.t_triple

    def get_t_crit(self):
        self.t_crit = CP.PropsSI(self.FLUIDE, 'Tcrit')
        return self.t_crit

    def get_t_min(self):
        self.t_min = (self.get_kelvin() + int((self.get_celsius()+self.get_t_triple()) / 10) * 10 + 10) + 20
        return self.t_min

    def get_val_t(self):
        self.val_t = np.arange(self.get_t_min(), 1.5 * self.get_t_crit(), self.dT)
        return self.val_t

    def get_t_to_show(self):
        self.t_to_show = list(range(2, len(self.get_val_t()), 2))
        return self.t_to_show

    def get_s_triple_x0(self):
        self.s_triple_x0 = CP.PropsSI('S', 'Q', 0, 'T', self.get_t_triple(), self.FLUIDE)
        return self.s_triple_x0

    def get_s_triple_x1(self):
        self.s_triple_x1 = CP.PropsSI('S', 'Q', 1, 'T', self.get_t_triple(), self.FLUIDE)
        return self.s_triple_x1

    def get_val_s(self):
        self.val_s = np.arange(self.get_s_triple_x0(), self.get_s_triple_x1() * 1.2, 100)
        return self.val_s

    def get_s_to_show(self):
        self.s_to_show = list(range(2, len(self.get_val_s()), 2))
        return self.s_to_show

    def get_v_crit(self):
        self.v_crit = 1 / CP.PropsSI(self.FLUIDE, 'rhocrit')
        return self.v_crit

    def get_exp_min(self):
        self.exp_min = int(np.floor(np.log10(self.get_v_crit()))) + 1
        return self.exp_min

    def get_v_triple_x1(self):
        self.v_triple_x1 = 1 / CP.PropsSI('D', 'Q', 1, 'T', self.get_t_triple(), self.FLUIDE)
        return self.v_triple_x1

    def get_exp_max(self):
        self.exp_max = int(np.ceil(np.log10(self.get_v_triple_x1()))) - 1
        return self.exp_max

    def get_val_v(self):
        self.val_v = [a * 10 ** b for a in [1, 2, 5] for b in range(self.get_exp_min(), self.get_exp_max() + 1)]
        return self.val_v

    def fait_isolignes(self, type_, valeurs, position=None, nb_points=1000, to_show=None, round_nb=0):
        """ S'occupe du calcul et du tracé des isolignes. """

        if not to_show:  # Valeurs par défauts:
            to_show = list(range(len(valeurs)))  # toutes !
        p_min, p_max = [p * self.CONVERSION[self.unitP] for p in plt.ylim()]  # On regarde les
        h_min, h_max = [H * self.CONVERSION[self.unitH] for H in plt.xlim()]  # limites du graphique
        # Par défaut, l'échantillonnage en P est linéaire
        val_p0 = np.linspace(p_min, p_max, nb_points)
        # Sinon, on se met en échelle log.
        if self.PLOGSCALE:
            val_p0 = np.logspace(np.log10(p_min), np.log10(p_max), nb_points)
        # Cas où les lignes ne vont pas sur tout l'éventail des pression, on
        # échantillonne en températures (car on ne peut pas directement
        # échantillonner en enthalpie h)
        t_min = self.get_t_triple()
        t_max = CP.PropsSI('T', 'P', p_max, 'H', h_max, self.FLUIDE)
        val_t = np.linspace(t_min, t_max, nb_points)
        val = ""
        # Pour chacune des valeurs demandées,
        for val, i in zip(valeurs, range(len(valeurs))):
            if type_ == 'V':  # Cas particulier des volumes massiques: échantillonnage
                val_p = CP.PropsSI('P', 'T', val_t, 'D', 1 / val, self.FLUIDE)  # en température
                val_h = CP.PropsSI('H', 'T', val_t, 'D', 1 / val, self.FLUIDE)  # et non en P
            elif type_ == 'Q':
                val_t = np.linspace(self.get_t_triple(), self.get_t_crit(), nb_points)
                val_p = CP.PropsSI('P', 'T', val_t, 'Q', val, self.FLUIDE)
                val_h = CP.PropsSI('H', 'T', val_t, 'Q', val, self.FLUIDE)
            else:  # Sinon, on utilise l'éventail des pression
                val_p = np.array(val_p0)
                val_h = CP.PropsSI('H', 'P', val_p, type_, val, self.FLUIDE)
            # On se remet dans les bonnes unités
            val_h = val_h / self.CONVERSION[self.unitH]
            val_p = val_p / self.CONVERSION[self.unitP]
            if type_ == 'S':
                val /= 1e3  # Pour mettre en kJ/K/kg
            if type_ == 'T':
                val = self.get_celsius()+val
            if round_nb > 0:
                val = str(round(val, round_nb))  # Pour faire joli

            else:
                val = str(int(round(val)))  # là aussi...
            label = '${}={}$ {}'.format(self.LABEL[type_], val, self.UNITS[type_])
            # Affichage courbe
            plt.plot(val_h, val_p,
                     color=self.COLOR_MAP[type_], linestyle=self.LINE_STYLE[type_])

            # Le programme proprement dit commence ici.
    def CycleFrigorifique(self):

        self.HP = QueryRequest(1)
        self.HP = TupleToFloat(self.HP)

        # Cette méthode récupère la ligne suivante d'un ensemble de résultats de requête et renvoie une séquence unique.Par défaut, le tuple retourné est constitué de données renvoyées par le serveur MySQL, converties en objets Python.
        self.BP = QueryRequest(2)
        self.BP = TupleToFloat(self.BP)

        self.DetenteurE = PropsSI('H', 'P', self.HP * 100000, 'Q', 0, self.FLUIDE) * 0.001
        self.DetenteurS = PropsSI('H', 'P', self.BP * 100000, 'Q', 0, self.FLUIDE) * 0.001
        self.CompresseurE = PropsSI('H', 'P', self.BP * 100000, 'Q', 1, self.FLUIDE) * 0.001
        self.CompresseurS = PropsSI('H', 'P', self.HP * 100000, 'Q', 1, self.FLUIDE) * 0.001



    def creer_diagramme(self):
        self.CycleFrigorifique()
        fig = plt.figure(figsize=(15, 10))
        ax = fig.add_subplot(111)
        ax.set_xlim(self.get_h_min(), self.get_h_max())
        ax.set_ylim(self.get_p_min(), self.get_p_max())
        ax.xaxis.set_minor_locator(tck.AutoMinorLocator())
        if self.PLOGSCALE:
            plt.yscale('log')  # Passage en log(P)

        # Tracé de la courbe de saturation
        self.fait_isolignes('Q', [0, 1], position=0, to_show=[''])
        # Ici, on fait toutes les autres isolignes (le boulot a été fait plus haut)

        if self.ISO_T:
            self.fait_isolignes('T', self.get_val_t(), position=0.8, to_show=self.get_t_to_show())
        if self.ISO_S:
            self.fait_isolignes('S', self.get_val_s(), position=0.3, to_show=self.get_s_to_show(), round_nb=3)
        if self.ISO_V:
            self.fait_isolignes('V', self.get_val_v(), position=0.25, to_show=self.v_to_show, round_nb=3)
        if self.ISO_X:
            self.fait_isolignes('Q', self.val_x, position=0.1, to_show=self.x_to_show, round_nb=2)

        plt.plot([self.DetenteurE, self.CompresseurS, self.CompresseurE, self.DetenteurS, self.DetenteurE], [self.HP, self.HP, self.BP, self.BP, self.HP], "-rs")
        plt.plot([0, self.DetenteurE], [0, self.HP], "--c")
        plt.plot([0, self.DetenteurS], [0, self.BP], "--c")
        plt.plot([0, self.CompresseurS], [0, self.HP], "--c")
        plt.plot([0, self.CompresseurE], [0, self.BP], "--c")
        plt.plot([0, self.DetenteurE], [self.HP, self.HP], "--c")
        plt.plot([0, self.DetenteurS], [self.BP, self.BP], "--c")

        plt.xlabel('Enthalpie massique $h$ (en {}/kg)'.format(self.unitH))
        plt.ylabel('Pression P (en {})'.format(self.unitP))
        plt.title('Diagramme Pression/Enthalpie pour le fluide {}'.format(self.FLUIDE))

        plt.grid(which='both')  # Rajout de la grille
        plt.savefig(r"C:\Dossier_Perso\Etude Supérieur\Lycee\Projet_PAC\Aymeric\assets\diagramme".format(self.FLUIDE))







