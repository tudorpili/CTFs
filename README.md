
# CyberEdu CTFs - Reverse Engineering

Vom prezenta rezolvarea a 4 ctf-uri din categoria Reverse Engineering.

### 1. 'source' - de dificultate easy
 - descriere: I store all my secrets in binaries, no one can read them if they don't have the source code!
 - files: Ni se ofera un fisier cu denumirea main

 #### rezolvare: Acest exercitiu ne invata prima data sa incarcam fisierul (binar,elf,text,executabil) intr o aplicatie de analiza de tip Ida, Cutter, etc . Prima data ne uitam la string-uri, acestea ne pot da multe indicii.In cazul acestui fisier putem observa stringul `TFC{3v3ryth1ng_1s_0p3n_5ourc3_1f_y0u try_h4rd_3n0ugh}`care este si raspunsul CTF-ului.

 ### 2. 'get-password' - dificultate easy
 - acest ctf a fost publicat la `European Cyber Security Challenge 2019` ce a avut loc in Romania.
 - descriere:
 - files: un fisier cu numele get
 #### rezolvare: un alt mod de analiza al unui fisier binar este verificarea functiei main si eventual a altor functii si decompilarea acestora pentru a intelege ce se intampla in spatele lor. Observam functia check_pw si prin decompilarea acesteia observam niste operatii ce se aplica pe parola introdusa pentru a fi validata 
 #### De asemenea in strings observam 20 de strings care poate prin intermediul carora se face verificarea

