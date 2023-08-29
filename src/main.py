import logging

from Golondrina import Golondrina
from Paloma import Paloma
from Mariposa import Mariposa
from Logger import Logger


Log = Logger("INFO")

Pepita = Golondrina("Pepita", Log)
Pepon = Golondrina("Pepon", Log)
Bombon = Paloma("Bombon", Log)
Twinkle = Mariposa("Twinkle", 1, Log)

Pepita.comer(20)
Pepon.comer(20)
Bombon.comer(20)
Twinkle.comer(20)

Pepita.volar(2)
Pepon.volar(2)
Bombon.volar(2)
Twinkle.volar(2)

Pepita.comer(10)
Pepon.comer(10)
Bombon.comer(10)
Twinkle.comer(10)

Pepita.volar(3)
Pepon.volar(3)
Bombon.volar(3)
Twinkle.volar(3)

Pepita.obtener_kms_recorridos()
Pepon.obtener_kms_recorridos()
Bombon.obtener_kms_recorridos()
Twinkle.obtener_kms_recorridos()
