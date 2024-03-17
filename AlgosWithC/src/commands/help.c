/**
 * Contains logic for the help command.
 */

#include <stdio.h>



/**
 * Log the help command output to the console.
 */
void helpCommand() {
  char CYAN_START[] = "\033[0;36m";
  char RICH_END[] = "\033[0;37m";
  char INFO_PREFIX[] = "\033[0;34m[INFO]\033[0;37m";
  char INDENT[] = "    ";

  char help_command[] = "Help";
  char help[] = "Use to see more info about how to use this application.";
  char array_access_command[] = "Array access";
  char array_access[] = "Use to access an array at the given index.";

  printf("%s AlgosWithC\n", INFO_PREFIX);
  printf("%s Commands:\n", INFO_PREFIX);
  printf("%s %s %s %s%s: %s\n", INFO_PREFIX, INDENT, CYAN_START, help_command, RICH_END, help);
  printf("%s %s %s %s%s: %s\n", INFO_PREFIX, INDENT, CYAN_START, array_access_command, RICH_END, array_access);
}