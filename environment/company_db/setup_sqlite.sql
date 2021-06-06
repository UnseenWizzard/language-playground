CREATE TABLE companies (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(2048)
);
CREATE TABLE company_metadata (
    id INT PRIMARY KEY,
    uuid BINARY(16) UNIQUE NOT NULL,
    yearly_dollar_revenue INT,
    interesting_data VARCHAR(255),
    FOREIGN KEY(id) REFERENCES companies(id)
);

CREATE INDEX uuid_index ON company_metadata(uuid);

INSERT INTO companies VALUES (1, "Solo Shipping Ltd.", "A Place 42, 1234 ZIP, Country");
INSERT INTO company_metadata VALUES (1, X'7a65ce56e9a14bc583f55a459a09e85e', 42000, "information!");
INSERT INTO companies VALUES (2, "Alluminum Falcon Recycling Co.", "A Place 42, 1234 ZIP, Country");
INSERT INTO company_metadata VALUES (2, X'db60fcd4c1c04fa7ae8a0c1fa35b24c6', 42000, "information!");
INSERT INTO companies VALUES (3, "Reynolds Transport LLC", "A Place 42, 1234 ZIP, Country");
INSERT INTO company_metadata VALUES (3, X'95aa0bc54f7941af8434ee7f6ff14b12', 42000, "information!");
INSERT INTO companies VALUES (4, "Serenity Trucking", "A Place 42, 1234 ZIP, Country");
INSERT INTO company_metadata VALUES (4, X'b85748f9a6bd4b3bb961d27679d395a6', 42000, "information!");
INSERT INTO companies VALUES (5, "Holden Windmill Repairs", "A Place 42, 1234 ZIP, Country");
INSERT INTO company_metadata VALUES (5, X'9fcd2f6472684cf0b9fb4f690a79bc73', 42000, "information!");
INSERT INTO companies VALUES (6, "Rocinante Chariots Ltd.", "A Place 42, 1234 ZIP, Country");
INSERT INTO company_metadata VALUES (6, X'c01d030bc3c74247b72d0e921d5da1a2', 42000, "information!");