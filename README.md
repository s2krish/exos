# Release Note

1. Project setup using Django 1.9 with a sqlite database
2. Extended User model to add birthday and random number with OneToOne relation with UserProfile Model
3. Views for listing all users, viewing, adding, editing and deleting a single user
4. Template tags added:
    1. bizzfuzz: will display "allowed" if the user is > 13 years old otherwise display "blocked"
    2. check_age: will display the BizzFuzz result of the random number that was generated for the user. The BizzFuzz specification is that for multiples of three print "Bizz" instead of the number and for the multiples of five print "Fuzz". For numbers which are multiples of both three and five print "BizzFuzz"


# Installation

1. Clone project https://github.com/s2krish/exos
2. Install requirements using pip

        pip install -r requirements.txt

3. Run migration

        ./manage.py migrate