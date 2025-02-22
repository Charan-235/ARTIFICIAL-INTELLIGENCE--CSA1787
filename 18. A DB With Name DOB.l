#code
person(john_doe, date(1990, 5, 14)).
person(jane_smith, date(1985, 8, 23)).
person(alice_jones, date(1992, 11, 30)).
find_dob(Name, DOB) :- person(Name, DOB).

#Output:


?- consult('DOB.l').
true.

?- find_dob(john_doe, DOB).
DOB = date(1990, 5, 14).
