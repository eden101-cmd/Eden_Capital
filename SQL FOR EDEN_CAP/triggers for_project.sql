CREATE OR REPLACE FUNCTION insert_price()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.Product_Id = 8198129 AND NEW.Price_Per_Unit != 151.00 THEN
        RAISE EXCEPTION 'the price of this product must be equal to 151';
    END IF;
    IF NEW.Product_Id = 4772822 AND NEW.Price_Per_Unit != 37.00 THEN
        RAISE EXCEPTION 'the price of this product must be equal to 37';
    END IF;
    IF NEW.Product_Id = 8870011 AND NEW.Price_Per_Unit != 34.00 THEN
        RAISE EXCEPTION 'the price of this product must be equal to 34';
    END IF;
    IF NEW.Product_Id = 1883191 AND NEW.Price_Per_Unit != 1.10 THEN
        RAISE EXCEPTION 'the price of this product must be equal to 1.1';
    END IF;
    IF NEW.Product_Id = 1091919 AND NEW.Price_Per_Unit != 0.70 THEN
        RAISE EXCEPTION 'the price of this product must be equal to 0.7';
    END IF;
    IF NEW.Product_Id = 7100190 AND NEW.Price_Per_Unit != 2.10 THEN
        RAISE EXCEPTION 'the price of this product must be equal to 2.1';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER insert_price
BEFORE INSERT OR UPDATE ON Products_Cap_1
FOR EACH ROW
EXECUTE FUNCTION insert_price();

CREATE OR REPLACE FUNCTION prod_name()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.Product_Id = 8198129 AND NEW.Product_Name != 'Water Pump Melody' THEN
        RAISE EXCEPTION 'the name of the product must be Water Pump Melody';
    END IF;
    IF NEW.Product_Id = 4772822 AND NEW.Product_Name != 'Microscope Landless Land' THEN
        RAISE EXCEPTION 'the name of the product must be Microscope Landless Land';
    END IF;
    IF NEW.Product_Id = 8870011 AND NEW.Product_Name != 'Paint Brush V3' THEN
        RAISE EXCEPTION 'the name of the product must be Paint Brush V3';
    END IF;
    IF NEW.Product_Id = 1883191 AND NEW.Product_Name != 'Spoon Rotonda 4' THEN
        RAISE EXCEPTION 'the name of the product must be Spoon Rotonda 4';
    END IF;
    IF NEW.Product_Id = 1091919 AND NEW.Product_Name != 'Standard Keyboard Key R' THEN
        RAISE EXCEPTION 'the name of the product must be Standard Keyboard Key R';
    END IF;
    IF NEW.Product_Id = 7100190 AND NEW.Product_Name != 'Tea Cup Purple Sea' THEN
        RAISE EXCEPTION 'the name of the product must be Tea Cup Purple Sea';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER prod_name
BEFORE INSERT OR UPDATE ON Products_Cap_1
FOR EACH ROW
EXECUTE FUNCTION prod_name();
