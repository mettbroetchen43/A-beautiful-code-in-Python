import random as rnd
from time import perf_counter as pfc

start = pfc()
anz_türen = 3
gew_ow = gew_mw = 0
anz_simulationen = 1_000_000

for _ in range(anz_simulationen):
  preis = rnd.randrange(anz_türen)
  wahl  = rnd.randrange(anz_türen)
  if preis == wahl:
    gew_ow += 1
  moderator = [t for t in range(anz_türen) if t != wahl and t != preis].pop()
  wahl      = [t for t in range(anz_türen) if t != wahl and t != moderator].pop()
  if preis == wahl:
    gew_mw += 1

print(f'{anz_simulationen:,.0f} Simulationen in {pfc()-start:.2f} Sek.')
print(f'Gewinnquote ohne Wechsel = {gew_ow/anz_simulationen*100:.2f} %')    
print(f'Gewinnquote mit Wechsel  = {gew_mw/anz_simulationen*100:.2f} %')


