#!/usr/bin/env bash

find . -name '*.py'| xargs wc -l
find . -name '*.sh'| xargs wc -l
