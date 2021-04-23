CREATE TABLE II_GA_IP_CATEGORIES
(
   CN             VARCHAR(34)    NOT NULL PRIMARY KEY,
   GRANT_CN       VARCHAR(34)    NOT NULL,
   CATEGORY_CD    VARCHAR(2)     NOT NULL,
   CATEGORY_DESC  VARCHAR(120),
   LAST_UPDATE    DATE                 DEFAULT CURRENT_TIMESTAMP NOT NULL
)
;

CREATE INDEX II_GA_IP_CATEGORIES_FK_I
   ON II_GA_IP_CATEGORIES (GRANT_CN ASC)
   ;

ALTER TABLE II_GA_IP_CATEGORIES
 ADD CONSTRAINT II_GA_IP_CATEGORIES_FK FOREIGN KEY (GRANT_CN)
 REFERENCES II_GRANTS (CN);
