Description:
This database is to store details of a game matches between players as well as pair two players according to their matches records.

Files include tournament.py, tournament.sql, tournament_test.py

Requirements: 
You must have Python-2.7 and PostgreSQL installed on your machine.

Usage:
Launch the Vagrant VM from inside the vagrant folder with:
vagrant up
vagrant ssh
Execute the following commands to create the necessary tables inside the database:
cd/vagrant/tournament
psql tournament
\i tournament.sql
execute the following command to run the test and see the output from your console:
python tournament_test.py
 
If you have any questions, please contact 979935898@qq.com
