
#reglas familia

#linea_profe
hermanos (A,B) : -  A \ == B , padres (A,X), padres (B,X).



primos (A,B) : -  A \ == B , padres (A,X), padres (B,Y), hermanos (X,Y).

tios (A,B) : -  A \ == B , padres (A,X), hermanos (X,B).

tios (A,B) : -  A \ == B , padres (A,X), hermanos (X,Y), padres (Z,Y), padres (Z,B).

abuelos (PA,PB) : - padres (PA,X), padres (X,PB).

bisabu (A,B) : -  A \ == B , padres (A,X), padres (X,Y), padres (Y,B).

tioabu (A,B) : -  A \ == B , padres (A,X), tios (X,B).

tioseg (A,B) : -  A \ == B , padres (A,X), tioabu (X,B).

nietos (A,B) : -  A \ == B , padres (A,X), padres (X,B).

bisnie (A,B) : -  A \ == B , bisabu (B,A).

sobrinseg (A,B) : -  A \ == B , nietos (A,X), tios (X,B).
