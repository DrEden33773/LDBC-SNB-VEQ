# ChangeLog

## 1:29 AM, 2/22/2024

In [organisation.csv](./data/raw/organisation.csv):

Change row name `:ID(Organisation)` into `:ID(Organisationid)`

## version 1.0

Implemented: bi(3/4/10/11/13/14)

Structure:

- One `original data graph` for all
- One `indexed data graph` for all

## version 2.0

Implemented: bi(9/15/19), ic(8/12), is(2)

Structure:

- One `original data graph` for all
- Different `indexed data graphs` for each

## version 3.0 (ON AIR)

Change structure into:

- One `original data graph` for all
- Transfer `original data graph` to `indexed one` on each query, and recover it after finished
