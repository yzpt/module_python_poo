python3 -m venv venv_module_poo
source venv_module_poo/bin/activate
pip install ipykernel pandas matplotlib seaborn plotly 

touch .gitignore
echo "venv_module_poo/" >> .gitignore
echo "z/" >> .gitignore

git init
git branch -m main
git add .
git commit -m "Initial commit"

gh repo create module_python_poo --public
git remote add origin https://github.com/yzpt/module_python_poo.git
git push -u origin main



