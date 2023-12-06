CREATE TABLE "RANDOM_TABLE" ( "VARDAS" INT, "PAVARDĖ" datetime, "GIMIMO_DATA" TEXT, "PAREIGOS" TEXT, "SKYRIUS_PAVADINIMAS" TEXT )
 
DROP TABLE RANDOM_TABLE;
 
select * from DARBUOTOJAI;
 
 
select distinct PAREIGOS from DARBUOTOJAI;
 
select count(*) from DARBUOTOJAI;
 
 
select
    count(*), PAREIGOS
from
    DARBUOTOJAI
WHERE
    1 = 1
group by
    PAREIGOS
HAVING
    count(*) > 1
order by
    count(*);
 
 
 
SELECT
    *
FROM
    DARBUOTOJAI
WHERE
    SKYRIUS_PAVADINIMAS = 'Gamybos'
    OR PAREIGOS = 'Finansininkas'
ORDER BY
    GIMIMO_DATA
    DESC;
   
 
SELECT
    *
FROM
    DARBUOTOJAI
WHERE
    substr(GIMIMO_DATA, 1, 4) BETWEEN '1980' AND '1988'
order by
    GIMIMO_DATA;
 
 
INSERT INTO DARBUOTOJAI VALUES(
"Jotautas", "Treigys", "2000-01-01", "Montuotojas", "Gamybos"
);
 
 
INSERT INTO DARBUOTOJAI
    (VARDAS, GIMIMO_DATA, PAREIGOS, SKYRIUS_PAVADINIMAS)
VALUES
    ("Antanas", "1999-01-01", "Montuotojas", "Gamybos");
 
 
UPDATE DARBUOTOJAI SET PAVARDĖ = "Antanauskas" WHERE VARDAS = "Antanas" AND PAREIGOS = "Montuotojas";
 
 
DELETE FROM DARBUOTOJAI where VARDAS = "Antanas" AND PAVARDĖ = "Antanauskas";
turi kontekstinį meniu






# 1. Select all data in the table.
# 2. Select Unique first names
# 3. Select Unique last names
# 4. Count how many distinct companies are in the table
# 5. Select all people whose date_of_birth is between 1970s and 1990s inclusive
# 6. count how many emails end with ".com"
# 7. In one result get count of Males and Females