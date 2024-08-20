cd /Users/pawansingh/Desktop/LearnApp/LearnPython
 . /opt/anaconda3/bin/activate && conda activate /opt/anaconda3/envs/learning; 
alembic revision --autogenerate -m "Corrected data type mismatch"
alembic upgrade head
python -m app.main
