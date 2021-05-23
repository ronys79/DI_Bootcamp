-- Get a list of all film languages.
SELECT * FROM film;
SELECT * FROM language;
-- Get a list of all films joined with their languages – select the following details : film title, description, 
-- and language name. Try your query with different joins:

SELECT title, description, name FROM film
INNER JOIN language ON film.language_id = language.language_id ORDER BY title;

--   Get all films, even if they don’t have languages.
SELECT title, description, name
FROM film
FULL JOIN language
ON film.language_id = language.language_id
ORDER BY name;

--   Get all languages, even if there are no films in those languages.