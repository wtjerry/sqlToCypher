INSERT INTO vorlesungen(VorlNr, Titel, SWS, gelesenVon)
VALUES (5001, 'Grundzuege', 4, 2137);

INSERT INTO vorlesungen(VorlNr, Titel, SWS, gelesenVon)
VALUES (5041, 'Ethik', 4, 2125);

INSERT INTO voraussetzen(Vorgänger, Nachfolger)
VALUES (5001, 5041);