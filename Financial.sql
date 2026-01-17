CREATE DATABASE CorporateFinanceDB;
GO

USE CorporateFinanceDB;
GO

CREATE TABLE Sales_FACT (
    Segment VARCHAR(50),
    Country VARCHAR(50),
    Product VARCHAR(50),
    Discount_Band VARCHAR(50),
    Units_Sold FLOAT,
    Manufacturing_Price FLOAT,
    Sale_Price FLOAT,
    Gross_Sales FLOAT,
    Discounts FLOAT,
    Sales FLOAT,
    COGS FLOAT,
    Profit FLOAT,
    Date DATETIME
);