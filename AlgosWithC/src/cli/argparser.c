/**
 * File for parsing args and checking args given to app.
 */

// Standard Imports
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// Local Imports
#include "../commands/array_command.h"
#include "../commands/help.h"

/**
 * Log all the argument info the console.
 * @param argc The number of arguments given.
 * @param argv The string array of arguments given.
 */
void log_arguments(int argc, char *argv[]) {
  char DEBUG_PREFIX[] = "\033[0;35m[DEBUG]\033[0;37m";

  printf("%s Number of Arguments: %d\n", DEBUG_PREFIX, argc);

  for (int i = 0; i < argc; i++) {
    printf("%s Argument [%d]: %s\n", DEBUG_PREFIX, i, argv[i]);
  }
}

/**
 * Checks if it is valid arguments.
 *
 * @param argc The number of arguments.
 * @param argv The arguments given to the app.
 * @return Whether the arguments are valid.
 */
bool is_valid_arguments(int argc, char *argv[]) {
  bool isZeroArgs = argc == 1;
  bool isHelpCommand = argc == 2 && strcmp(argv[1], "help") == 0;
  bool isArrayCommand = argc == 3 && strcmp(argv[1], "array") == 0 && strcmp(argv[2], "access") == 0;

  if (isZeroArgs || isHelpCommand || isArrayCommand)
    return true;

  return false;
}

void processArguments(int argc, char *argv[]) {
  bool isHelpCommand = argc == 1 || argc == 2 && strcmp(argv[1], "help") == 0;
  bool isArrayCommand = argc == 3 && strcmp(argv[1], "array") == 0;

  if (isHelpCommand)
    helpCommand();
  else if (isArrayCommand)
    array();
}
