#!/bin/bash
#
# to run this script:
# chmod u+x
# ./solutions-needed.sh <extension>

PROBLEMS_DIR='./problems'
EULER_DIR="./problems/euler"

if [ ! $# -eq 1 ]; then
    echo "usage: $0 <extension>"
    exit 1
fi

EXTENSION=$1

check_folder () {

  # for each folder in #Problems
  for path_to_folder in $1/*
  do
    folder_name="${path_to_folder##*/}"

    # recurse into the EULER_DIR
    if [ $path_to_folder == $EULER_DIR ]
    then
      check_folder $EULER_DIR
    else

      #NOTE: if we could rely on filenames to match the containing folders, this is more elegant
      # filename="$path_to_folder/$folder_name.$EXTENSION"
      # if [ ! -e $filename ]

      # if there are no files with the desired extension
      if ! compgen -G "$path_to_folder/*.$EXTENSION" > /dev/null
      then
          echo $path_to_folder
      fi
    fi
  done
}

echo ""
echo "The following problems do not have a solution for: .$1:"
check_folder $PROBLEMS_DIR
