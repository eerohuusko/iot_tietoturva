-- luo taulun nimeltä ktunnukset
-- taulu sisältää määritellyt kentät: id, kayttajanimi ja salasana
CREATE TABLE tunnukset
(
        id              int(5)          NOT NULL,
        kayttajanimi    CHAR(15)        NOT NULL,
        salasana        CHAR(30)        NOT NULL
)
