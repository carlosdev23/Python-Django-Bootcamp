# conda create --name MyDjangoEnv python=3.9
# String:
# x = "Item one: {y} Item Two: {x}".format(x="dog", y="cat"); 
# print( x )
# split
# upper
# lower

# List 
# x = [1,2,3,4,5, False, "sdafsd", [1,2,3]]
# print( x );

# x[0] = "asdads"
# print( x );

# append/ extend
# pop
# sort
# endswith
# matrix = [[1,2,3], [4,5,6], [7,7,8]]
# first_col = [row[0] for row in matrix];
# print( first_col );

# Dictonary
# my_stuff = { "key1": "value" }
# my_stuff["key1"] = 'updated vlaue';
# print( my_stuff["key1"].upper() );

# # Tuples are immutable.
# t1 = (2,3,5, 'a')
# print( t1[3] );

# x = set();
# x.add(1)
# x.add(2);

# print(x);

# mypair = [(1,2), (3,4), (5,6)]
# for (t1, t2) in mypair:
#     print( t1 );


# # lambda function.
# myList = [1,2,3,4,5]
# evens = filter( lambda num:num%2 == 0 myList )
# print( list(evens) );

# for loop range //
# enumerate
# LEGB
# Local
# Enclosing function 
# Global
# Built int

# LOCAL 
lambda x: x**2;
# Enclosing function looks
name = 'This is a global name';

# myList = [1,2,3]
# myList.append(4);
# print( myList );

# 
class Dog():
    def __init__(self, breed):
        self.breed = breed;

myDog = Dog( 'asdas' );
print( myDog.breed );
