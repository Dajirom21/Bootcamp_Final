CREATE TABLE "movements" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Fecha"	TEXT NOT NULL,
	"Hora"	TEXT NOT NULL,
	"Moneda_from"	TEXT NOT NULL,
	"Cantidad_from"	REAL NOT NULL,
	"Moneda_to"	TEXT NOT NULL,
	"Cantidad_to"	REAL NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT)
)