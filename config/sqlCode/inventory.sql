BEGIN;
--
-- Create model WeaponBrand
--
CREATE TABLE "inventory_weaponbrand" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "slug" varchar(50) NOT NULL, "description" text NOT NULL);
--
-- Create model WeaponBrandSupplier
--
CREATE TABLE "inventory_weaponbrandsupplier" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "slug" varchar(50) NOT NULL, "description" text NOT NULL, "user_id" bigint NOT NULL REFERENCES "accounts_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Weapon
--
CREATE TABLE "inventory_weapon" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "weapon_id" varchar(50) NOT NULL, "slug" varchar(50) NOT NULL, "price" decimal NOT NULL, "image" varchar(100) NULL, "quantity_available" integer NOT NULL, "in_inventory" bool NOT NULL, "category_id" bigint NOT NULL REFERENCES "inventory_weaponbrand" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "inventory_weaponbrand_slug_6c7e6cdc" ON "inventory_weaponbrand" ("slug");
CREATE INDEX "inventory_weaponbrandsupplier_slug_a58fc7d6" ON "inventory_weaponbrandsupplier" ("slug");
CREATE INDEX "inventory_weaponbrandsupplier_user_id_b1f7824d" ON "inventory_weaponbrandsupplier" ("user_id");
CREATE INDEX "inventory_weapon_slug_158af863" ON "inventory_weapon" ("slug");
CREATE INDEX "inventory_weapon_category_id_c691c0d2" ON "inventory_weapon" ("category_id");
COMMIT;
