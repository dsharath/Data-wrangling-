# The query below finds the names and birthdates of all the gorillas.
# 
# Modify it to make it find the names of all the animals that are not
# gorillas and not named 'Max'.
#
SELECT name, birthdate 
FROM animals 
WHERE species = 'gorilla';