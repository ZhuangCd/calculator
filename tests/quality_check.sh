#!/bin/bash

if [[ ! -d "reports" ]]; then
  mkdir reports
fi

get_mypy_report() {
  mypy ./calculator.py > mypy_calculator.txt
  echo "mypy done"
}

get_bandit_report() {
  bandit ./calculator.py > bandit_calculator.py.txt
  echo "bandit done"
}

get_flake8_report() {
  flake8 ./calculator.py > flake8_calculator.py.txt
  echo "flake8 done"
}

get_unittest_report() {
  python3 -m unittest -v test_calculator.py 2> unittest_calculator.txt
  echo "unit tests done"
}

get_coverage_report() {
  python3 -m coverage run test_calculator.py
  python3 -m coverage report > cov_calculator.txt
  python3 -m coverage report -m calculator.py > cov_calculator.txt
  python3 -m coverage html
}


main() {
  get_mypy_report
  get_bandit_report
  get_flake8_report
  get_unittest_report
  get_coverage_report
}

main
