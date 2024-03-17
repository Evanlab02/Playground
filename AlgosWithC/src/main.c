/**
 * Entry point for the AlgosWithC project.
 */

// Standard Imports
#include <stdio.h>
#include <stdbool.h>

// Local Imports
#include "cli/argparser.h"



/**
 * Entry point for the AlgosWithC project.
 *
 * @param argc The number of arguments passed in.
 * @param argv The arguments passed in when started.
 * @return The exit code.
 */
int main(int argc, char *argv[]) {
  char ERROR_PREFIX[] = "\033[0;31m[ERROR]\033[0;37m";

  int exit_code = 0;
  log_arguments(argc, argv);
  bool valid_arguments = is_valid_arguments(argc, argv);

  if (!valid_arguments) {
    printf("%s Invalid arguments given\n", ERROR_PREFIX);
    exit_code = 1;
  } else {
    processArguments(argc, argv);
  }

  return exit_code;
}
