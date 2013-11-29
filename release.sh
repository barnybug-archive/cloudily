#!/bin/bash -e

sublime -w setup.py:4
VERSION=$(python setup.py --version)

# make changelog
echo -e "$VERSION\n" > changelog
git log --format='- %s%n' $(git describe --abbrev=0).. >> changelog
sublime -w README.rst:56 changelog
rm changelog

git add README.rst setup.py
git commit -m $VERSION
git push
python setup.py release

echo "$VERSION released"
