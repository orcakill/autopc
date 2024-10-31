echo "CANNOT BUILD WIN MODULES ON MAC"
rem rm -r all_module
sphinx-apidoc -Me -o source ../autopc
./make.bat html
start _build/html/index.html