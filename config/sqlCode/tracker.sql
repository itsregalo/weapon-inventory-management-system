BEGIN;
--
-- Create model BaseStation
--
CREATE TABLE "tracker_basestation" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "location" varchar(50) NOT NULL, "slug" varchar(50) NOT NULL, "description" text NOT NULL);
CREATE INDEX "tracker_basestation_slug_62db6a02" ON "tracker_basestation" ("slug");
COMMIT;
