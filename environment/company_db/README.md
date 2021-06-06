# Company Database
A prefilled Postgres DB in a Docker container, or a `.sql` to setup SQLite.

## DB Structure
See [setup.sql](./setup.sql) for the DB schema that's created.

Notably contains UUID as binary data in an indexed colum in `company_metadata`. 
Queries thus require this column to be treated as a HEX number, whithout dashes.

> ### SQLite Syntax Hint
> 
> `HEX(company_metadata)` on SELECTS
> `X'{hexstring without -}` on INSERT or where clauses

> ### Postgres Syntax Hint
> 
> `HEX(company_metadata)` on SELECTS
> `X'{hexstring without -}` on INSERT or where clauses

## Sample Query 
Get id, uuid and name of a company by uuid.

### SQLite
```
SELECT companies.id, HEX(company_metadata.uuid), companies.name FROM company_metadata LEFT JOIN companies ON company_metadata.id
=companies.id WHERE company_metadata.uuid=X'7a65ce56e9a14bc583f55a459a09e85e';

1|7A65CE56E9A14BC583F55A459A09E85E|Solo Shipping Ltd.
```

### Postgres
> Note: this also handles removing dashes from input

```
SELECT companies.id, encode(company_metadata.uuid, 'hex') AS uuid, companies.name FROM company_metadata LEFT
 JOIN companies ON company_metadata.id
=companies.id WHERE company_metadata.uuid=decode(replace('7a65ce56-e9a1-4bc5-83f5-5a459a09e85e', '-', ''), 'hex');
```

## Dummy Data
Contains the following Data: 

```
{
    "companies" : [
        {
            "name": "Solo Shipping Ltd.", 
            "uuid": "7a65ce56-e9a1-4bc5-83f5-5a459a09e85e"
        },
        {
            "name": "Alluminum Falcon Recycling Co.", 
            "uuid": "db60fcd4-c1c0-4fa7-ae8a-0c1fa35b24c6"
        },
        {
            "name": "Reynolds Transport LLC", 
            "uuid": "95aa0bc5-4f79-41af-8434-ee7f6ff14b12"
        },
        {
            "name": "Serenity Trucking", 
            "uuid": "b85748f9-a6bd-4b3b-b961-d27679d395a6"
        },
        {
            "name": "Holden Windmill Repairs", 
            "uuid": "9fcd2f64-7268-4cf0-b9fb-4f690a79bc73"
        },
        {
            "name": "Rocinante Chariots Ltd.", 
            "uuid": "c01d030b-c3c7-4247-b72d-0e921d5da1a2"
        }
    ]
}
```