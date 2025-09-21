#!/bin/bash
git pull origin main

# Run analyzer & generate report as a test
python data_analyzer.py
python generate_report.py
if [ $? -eq 0 ]; then
git add .
if [ -z "$1" ]; then
echo "Enter commit message:"
read msg
else
msg=$1
fi
git commit -m "$msg"
git push origin $(git branch --show-current)
else
echo "Tests failed. Commit aborted."
fi
