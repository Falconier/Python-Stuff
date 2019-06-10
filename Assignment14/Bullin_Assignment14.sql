--Assignment 14
--Jacob Emory Bullin

--step 5
--assuming that you meant rows, not columns (because i dont think you want me to select just the 'categories' column)
--select * from 'Movie' where categoryID = 2

--step 6
--select * from 'Movie' where categoryID = 3

--step 7
--select name, year from 'Movie'

--step 8
--select name, year from 'Movie' order by year

--step 9
--this resulted in an error as I found that the categoryID field cannot be null
--upon further investigation I found you set all fields to NOT NULL, 
--so this would never work, nor would you be able to ever make a blank row...
--but this is how it would work if all field values allowed NULL.
--insert into 'Movie' default values

--step 11
--since in the above step 9 there was an error, I was unable to officially test this statement, though it should theoretically work
--delete from 'Movie' where name is null