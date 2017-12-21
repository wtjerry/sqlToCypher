# what does it do
It will convert a sql file containing 'InsertInto' statements to cypher text

# how to config it
Appart from the path to the sql file you also need to provide 3 dictionaries with configurations:
## tables_to_convert_to_nodes

![tables_to_convert_to_nodes](https://user-images.githubusercontent.com/15376943/34259676-7c2bda18-e663-11e7-9ada-fb8af5810d50.png)

1. Table name in sql that should be converted to a cypher node
2. Id column in sql. The value of this column will be used as the cypher node identifier.
3. Node name in cypher text

## foreign_key_relationship_tables

![foreign_key_relationship_tables](https://user-images.githubusercontent.com/15376943/34259702-8ef933b6-e663-11e7-95cd-36616ab96e3b.png)

This config dictionary is only required if there are foreign key relationships in the sql file.
Each item in this config relates to a cypher relationship to be generated.

1. Table name in sql that has a foreign key
2. Id column (doesnt need to be in the same table as 1.) of which the value relates to a cypher Node identifier. Is used as the source of the relationship
3. Id column (doesnt need to be in the same table as 1.) of which the value relates to a cypher Node identifier. Is used as the destination of the relationship
4. Node name in cypher text. Will be written as all upper case.
5. Column in sql in table 1. which should not be converted to a attribute in cypher text. Can be used to not convert the foreign key column

## many_to_many_relationship_tables

![many_to_many_relationship_tables](https://user-images.githubusercontent.com/15376943/34259694-8bb43084-e663-11e7-9b6b-7b3154266310.png)

This config dictionary is only required if there are many to many relationship tables in the sql file.
Each item in this config relates to a cypher relationship to be generated.

1. Table name in sql that is a many to many relationship table
2. Id column in table 1. of which the value relates to a cypher Node identifier. Is used as the source of the relationship
3. Id column in table 1. of which the value relates to a cypher Node identifier. Is used as the destination of the relationship
4. Node name in cypher text. Will be written as all upper case
