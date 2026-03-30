open ~/Downloads
open ~/Documents/resumes
echo "Enter when done!!"
read
source /Users/mzhang/Documents/0b_cs_projects/-environments-/cs2100-code/bin/activate
cd ~/Documents/0b_cs_projects/lint_pdf
python make_resumes.py
