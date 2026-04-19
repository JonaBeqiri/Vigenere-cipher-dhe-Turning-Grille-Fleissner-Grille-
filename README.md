# Vigenere-cipher-dhe-Turning-Grille-Fleissner-Grille

Vigenère Cipher është një metodë klasike e kriptimit (fshehjes së mesazheve) që përdor një fjalë kyçe (keyword) për të ndryshuar shkronjat e mesazheve në mënyrë të përsëritur.

Ndryshe nga Caesar (ku zhvendosja është gjithmonë e njëjtë), këtu:

* çdo shkronjë e mesazhit mund të ketë një zhvendosje tjetër dhe
* kjo varet nga shkronja përkatëse e fjalës kyçe

## Ideja bazë

* Zgjedh një mesazh të thjeshtë (plaintext)
* Zgjedh një fjalë kyçe (p.sh. "KEY")
* Fjalën kyçe e përsërit mbi mesazhin
* Çdo shkronjë e mesazhit zhvendoset sipas shkronjës përkatëse të fjalës kyçe

Fillimisht, çdo shkronjë kthehet në numër:

A = 0
B = 1
C = 2
...
Z = 25

**Mesazhi:** HELLOWORLD
**Fjala kyçe:** KEY

**Përsëritet:** KEYKEYKEYK

## Formula e kriptimit

Për çdo shkronjë përdoret kjo formulë:

`C = (P + K) mod 26`

Ku:

* `P` = numri i shkronjës së mesazhit (plaintext)
* `K` = numri i shkronjës së fjalës kyçe
* `C` = rezultati (ciphertext)

## Shndërrimi në numra

| Shkronja | H | E | L  | L  | O  |
| -------- | - | - | -- | -- | -- |
| P        | 7 | 4 | 11 | 11 | 14 |

| Shkronja | K  | E | Y  | K  | E |
| -------- | -- | - | -- | -- | - |
| K        | 10 | 4 | 24 | 10 | 4 |

## Llogaritja

`C = (P + K) mod 26`

* (7 + 10) mod 26 = 17 → R
* (4 + 4) mod 26 = 8 → I
* (11 + 24) mod 26 = 9 → J
* (11 + 10) mod 26 = 21 → V
* (14 + 4) mod 26 = 18 → S

**Rezultati:** `RIJVS`

## Si bëhet deshifrimi?

Përdoret formula e kundërt:

`P = (C - K) mod 26`

Pra:

* merr shkronjën e koduar
* zbrit vlerën e fjalës kyçe
* kthen rezultatin në shkronjë

Kodi implementon algoritmin Vigenere Cipher.
Fillimisht, programi kërkon nga përdoruesi të fusë tekstin që dëshiron të enkriptojë dhe një fjalë kyçe përmes funksionit `input()`. Kjo fjalë kyçe përdoret për të përcaktuar zhvendosjen e çdo shkronje në tekst. Para se të vazhdojë, programi kontrollon që çelësi të përmbajë vetëm shkronja duke përdorur `isalpha()`, për të siguruar që algoritmi të funksionojë saktë.

Gjatë enkriptimit, programi kalon nëpër çdo karakter të tekstit. Nëse karakteri është shkronjë ai shndërrohet në një vlerë numerike (0–25) me `ord()` dhe i shtohet vlera e shkronjës përkatëse nga çelësi, i cili përsëritet automatikisht duke përdorur operatorin modulo sipas gjatësisë së tij. Rezultati llogaritet me formulën `(p + k) % 26` dhe kthehet përsëri në shkronjë me `chr()`, duke ruajtur dallimin mes shkronjave të mëdha dhe të vogla. Nëse karakteri nuk është shkronjë (si hapësira apo simbole), ai mbetet i pandryshuar.

Në pjesën e dekriptimit, përdoruesi jep përsëri tekstin e koduar dhe të njëjtin çelës. Programi përdor të njëjtën logjikë, por këtë herë aplikon formulën `(c - k + 26) % 26` për të kthyer çdo shkronjë në formën e saj origjinale. Kështu, kodi realizon me sukses si enkriptimin ashtu edhe dekriptimin duke përdorur parimet bazë të algoritmit Vigenere Cipher.

---

# Turning (Fleissner) Grille

Turning (Fleissner) Grille është një metodë klasike e enkriptimit të të dhënave. Algoritmi përdor një rrjetë (matricë ose grille) me "vrima". Teksti shkruhet në këto vrima dhe pas çdo hapi, grila rrotullohet me 90 gradë në drejtimin e akrepave të orës, derisa të mbushet e gjithë matrica. Kodi i implementuar në këtë projekt i ka 3 funksionalitete kryesore:

1. Enkriptimi,
2. Dekriptimi,
3. Validimi i Matricës (Grilës).

## ENKRIPTIMI

Gjatë enkriptimit programi konverton plaintext-in në ciphertext duke e shpërndarë në matricë përmes rrotullimeve të grilës. Kodi përdor një matricë standarde të formatit 4x4 me vrima në pikat:

(0, 0), (0, 1), (1, 0), (1, 1)

```text
1 | 1 | 0 | 0
_____________
1 | 1 | 0 | 0
_____________  <-- Pozita Fillestare
0 | 0 | 0 | 0
_____________
0 | 0 | 0 | 0
```

---

```text
01 | 02 | 08 | 06
_________________
03 | 04 | 07 | 05
_________________  <-- Hapat e plotësimit të matricës
14 | 16 | 12 | 11
_________________
13 | 15 | 10 | 09
```

Kjo matricë mund të enkriptojë një tekst me gjatësi 16 karaktere. Fillimisht kodi e standardizon tekstin duke i larguar të gjitha hapsirat mes shkronjave dhe duke i kthyer të gjitha në madhësi të njejtë. Pastaj enkriptimi kryhet në 4 raunde, për secilin raund 4 karaktere vendosen në vrimat në matrice pastaj grila rrotullohet për 90° në drejtim të akrepave të orës. Në qoftë se teksti të cilin duam ta enkriptojmë është më i shkurtër se numri i hapsirave në matricë programi do t'i zëvendësojë hapsirat me "X".

Për shembull teksti Hello World enkriptohet si në vijim:

`HELLOWORLD => HEOOLLRWXXXXXXDL`

```text
H | E | O | O
-------------
L | L | R | W
-------------
X | X | X | X
-------------
X | X | D | L
```

Nëse dëshirojmë të enkriptojmë trekst me gjatësi më të madhe për të cilin na nevojitet një matricë me dimensione më të mëdha, si dhe nëse duam ta enkriptojmë duke përdorur një set tjetër të vrimave atëhere ne duhet të ndryshojmë kodin përkatësisht variablat `size` dhe `holes` brenda main-it.

## DEKRIPTIMI

Dekriptimi është një process i kundërt me enkriptimin. Programi merr tekstin e shifruar dhe, duke përdorur të njëjtën grilë, e kthen në tekstin origjinal duke hequr karakteret mbushëse nga fundi dhe duke e rrotulluar grilen në drejtim të kundërt me procesin e enkriptimit.

## Validimi i Grilës

Kodi ka mekanizmin e sigurisë `validate_grille` që siguron që vrimat e zgjedhura janë valide dhe të mos mbivendosen gjatë rrotullimit si dhe mbulojnë të gjitha qelizat e matricës.

**Shënim:** Grila e përdorur në këtë shembull është për ilustrim të funksionimit të rrotullimeve. Në praktikë, përdoret funksioni `validate_grille` për të siguruar që grila është valide dhe mbulon çdo pozicion vetëm një herë.

## Rrotullimet e Grilës

Rrotullimi i grilës është një hap kyç në algoritëm. Grila rrotullohet me **90° në drejtim të akrepave të orës (clockwise)** pas çdo raundi të enkriptimit ose dekriptimit.

Në një matricë 4×4, kemi gjithmonë 4 pozicione:

1. 0° (pozicioni fillestar)
2. 90°
3. 180°
4. 270°

### Shembull i rrotullimeve

Grila fillestare:

```text
1 | 1 | 0 | 0
-------------
1 | 1 | 0 | 0
-------------
0 | 0 | 0 | 0
-------------
0 | 0 | 0 | 0
```

Rrotullimi 90°:

```text
0 | 0 | 1 | 1
-------------
0 | 0 | 1 | 1
-------------
0 | 0 | 0 | 0
-------------
0 | 0 | 0 | 0
```

Rrotullimi 180°:

```text
0 | 0 | 0 | 0
-------------
0 | 0 | 0 | 0
-------------
0 | 0 | 1 | 1
-------------
0 | 0 | 1 | 1
```

Rrotullimi 270°:

```text
0 | 0 | 0 | 0
-------------
0 | 0 | 0 | 0
-------------
1 | 1 | 0 | 0
-------------
1 | 1 | 0 | 0
```

Gjatë çdo rrotullimi:

* vrimat (1) kalojnë në pozicione të reja
* në ato pozicione vendosen shkronjat e radhës
* pas 4 rrotullimeve mbulohet e gjithë matrica




  ## Ide kryesore

- **Vrimat = çelësi sekret**
- **Çdo pozicion përdoret vetëm një herë gjatë rrotullimeve**
- **Pa grilën e saktë, mesazhi nuk mund të lexohet**




