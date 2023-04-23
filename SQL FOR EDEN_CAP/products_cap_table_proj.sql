CREATE TABLE Products_Cap_1 (
    Product_Id integer PRIMARY KEY CHECK (Product_Id IN (8198129, 4772822, 8870011, 1883191, 1091919, 7100190)),
    Product_Name text CHECK (Product_Name IN ('Water Pump Melody', 'Microscope Landless Land', 'Paint Brush V3', 'Spoon Rotonda 4', 'Standard Keyboard Key R', 'Tea Cup Purple Sea')),
    Amount_Purchased integer CHECK (Amount_Purchased > 0 AND Amount_Purchased <= 1000),
    Price_Per_Unit numeric(5,2) CHECK (Price_Per_Unit IN (151.00, 37.00, 34, 1.10, 0.70, 2.10)),
    Total_Price numeric GENERATED ALWAYS AS (Amount_Purchased * Price_Per_Unit) STORED
);

INSERT INTO Products_cap_1
VALUES (8198129,'Water Pump Melody',3,151.00),
(4772822,'Microscope Landless Land',3,37.00),
(8870011,'Paint Brush V3',3,34.00),
(1883191,'Spoon Rotonda 4',3,1.10),
(1091919,'Standard Keyboard Key R',3,0.70),
(7100190,'Tea Cup Purple Sea',3,2.10);

select * from Products_Cap

alter table products_cap_1 rename to products_cap


SELECT current_user;
SELECT inet_server_addr();