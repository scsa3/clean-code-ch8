# Unittest

python -m unittest test_unittest_git.py


# Coverage

coverage run -m unittest
coverage report -m


# Mutpy

mut.py \
  --target git_mutate.py \
  --unit-test test_unittest_git_mutate.py \
  --operator AOD \
  --operator AOR \
  --operator COD \
  --operator COI \
  --operator CRP \
  --operator ROR \
  --show-mutants