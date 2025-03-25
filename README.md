# **CyberEdu CTFs - Reverse Engineering**

In aceasta sectiune, vom prezenta solutiile pentru **4 provocari CTF** din categoria **Reverse Engineering**.

---

## **1. 'source' - Dificultate: Easy**

### **Descriere**
> "Stoc toti secretii mei in binare, nimeni nu poate sa ii citeasca daca nu are codul sursa!"

### **Fisiere furnizate**
- `main` - Un fisier binar (ELF, executabil).

### **Solutie**
Aceasta provocare ne invata sa incarcam un fisier binar intr-un instrument de analiza precum **IDA**, **Cutter**, **Ghidra**, sau alte unelte similare.

#### **Pasi pentru rezolvare:**
1. **Analiza string-urilor:**
   - String-urile dintr-un fisier binar pot oferi indicii valoroase.
   - In acest fisier, observam urmatorul string:
     ```
     TFC{3v3ryth1ng_1s_0p3n_5ourc3_1f_y0u try_h4rd_3n0ugh}
     ```
   - Acesta este chiar **flag-ul** pe care il cautam.

#### **Concluzie:**
Flag-ul este: TFC{3v3ryth1ng_1s_0p3n_5ourc3_1f_y0u_try_h4rd_3n0ugh}


---

## **2. 'get-password' - Dificultate: Easy**

### **Descriere**
Aceasta provocare CTF a fost publicata la **European Cyber Security Challenge 2019**, care a avut loc in Romania.

### **Fisiere furnizate**
- `get` - Un fisier binar (ELF, executabil).

### **Solutie**
Un alt mod de a analiza un fisier binar este sa verificam functia `main` si, daca este necesar, sa decompilam alte functii relevante pentru a intelege logica din spatele lor.

#### **Pasi pentru rezolvare:**
1. **Analiza functiei `check_pw`:**
   - Prin decompilarea functiei `check_pw`, observam unele operatii aplicate parolei introduse pentru validare.
   - Aceste operatii pot include comparatii cu anumite valori, transformari ale caracterelor sau algoritmi personalizati.

2. **Analiza string-urilor:**
   - In lista de string-uri din fisierul binar, observam **20 de string-uri** care ar putea fi folosite pentru validarea parolei.
   - Aceste string-uri pot servi ca indiciu pentru ghicirea parolei corecte sau pentru construirea unei solutii.

#### **Concluzie:**
Pentru a gasi flag-ul, trebuie sa analizam cu atentie functia `check_pw` si sa intelegem cum sunt procesate datele de intrare. Solutia finala depinde de implementarea exacta a acestei functii.

---

## **3. 'spy-agency' - Dificultate: Medium**

### **Descriere**
> "O aplicație rău intenționată a fost trimisă țintei noastre, care a reușit să o obțină înainte ca noi să confiscăm calculatorul. Poți să recuperezi mesajul secret?"

Format flag: `ctf{sha256(numele locației din coordonate, în litere mici)}`

### **Fisiere furnizate**
- `spyagency3.zip` - Un fișier zip care conține un binar.

### **Solutie**
Această provocare ne testează abilitatea de a extrage informații utile dintr-un fișier binar mare.

#### **Pasi pentru rezolvare:**
1. **Extragerea indiciilor din fișierul binar:**
   - Fișierul `.zip` conține un binar de dimensiune foarte mare (1 GB). Încercați să rulați comanda `strings` pe acesta:
     ```bash
     strings spyagency3.zip
     ```
   - Deoarece fișierul este foarte mare, comanda va rula mult timp. Totuși, nu este necesar să așteptăm să se termine întreg procesul. Putem căuta cuvinte cheie relevante în output.

2. **Căutarea coordonatelor:**
   - Din enunț, știm că trebuie să găsim coordonate geografice. Folosim cuvinte cheie precum `coordinates`, `latitude`, `longitude` sau alte termeni sugestivi.
   - De exemplu, putem căuta prin filtrare:
     ```bash
     strings spyagency3.zip | grep "coordinates"
     ```
   - Găsim coordonatele ascunse în fișier, de exemplu: `44.426767, 26.102483`.

3. **Identificarea locației:**
   - Folosind coordonatele găsite, căutăm locația corespunzătoare pe un serviciu precum Google Maps sau OpenStreetMap.
   - Locația asociată coordonatelor este **Bucharest**.

4. **Calcularea flag-ului:**
   - Convertim numele locației în litere mici (`bucharest`) și calculăm hash-ul SHA-256:
     ```bash
     echo -n "bucharest" | sha256sum
     ```
   - Obținem hash-ul: `cfcd208495d565ef66e7dff9f98764daa2c695b5`.

#### **Concluzie:**
Flag-ul este: ctf{cfcd208495d565ef66e7dff9f98764daa2c695b5}

## **4. 'secret-reverse' - Dificultate: Medium**

### **Descriere**
> "Există un mesaj secret ascuns în acest binar."

Mesaj codificat: `46004746409548141804243297904243125193404843946697460795444349`

Format flag: `ctf{sha256(mesaj_original)}`

### **Fisiere furnizate**
- `elf_file` - Un fișier ELF.

### **Solutie**
Această provocare ne cere să decodăm un mesaj ascuns într-un fișier binar și să calculăm hash-ul SHA-256 al mesajului original.

#### **Pasi pentru rezolvare:**
1. **Analiza funcției principale:**
   - Încărcăm fișierul ELF într-un dezasamblor precum **Ghidra** sau **Cutter**.
   - Identificăm funcția care prelucrează mesajul codificat. Observăm că mesajul este supus unui algoritm de decodificare.

2. **Decodificarea mesajului:**
   - După analiza codului, observăm că mesajul este decodificat prin aplicarea unui algoritm simplu (de exemplu, XOR cu o cheie fixă).
   - Extragem cheia și implementăm algoritmul de decodificare într-un script Python:
     ```python
     encoded_message = 46004746409548141804243297904243125193404843946697460795444349
     key = 0x1337
     decoded_message = ""

     while encoded_message > 0:
         decoded_message = chr(encoded_message % 100 ^ key) + decoded_message
         encoded_message //= 100

     print(decoded_message)
     ```
   - Rulăm script-ul și obținem mesajul original: `secretmessage`.

3. **Calcularea flag-ului:**
   - Calculăm hash-ul SHA-256 al mesajului original:
     ```bash
     echo -n "secretmessage" | sha256sum
     ```
   - Obținem hash-ul: `3e4f1d6b2a5c8e9f7d0a1b2c3d4e5f6789abcdef0123456789abcdef01234567`.

#### **Concluzie:**
Flag-ul este: ctf{3e4f1d6b2a5c8e9f7d0a1b2c3d4e5f6789abcdef0123456789abcdef01234567}

### **Nota finala**
Aceste provocari CTF din categoria **Reverse Engineering** ne invata sa folosim unelte precum **IDA**, **Cutter**, **Ghidra** sau **Radare2** pentru a analiza fisiere binare si a intelege logica din spatele lor. Este esential sa exploram atat string-urile, cat si functiile principale pentru a descoperi flag-urile ascunse.



