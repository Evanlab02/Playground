/**
 * File for parsing args and checking args given to app.
 */

#ifndef ALGOSWITHC_ARGPARSER_H
#define ALGOSWITHC_ARGPARSER_H
void log_arguments(int argc, char *argv[]);
bool is_valid_arguments(int argc, char *argv[]);
void processArguments(int argc, char *argv[]);
#endif // ALGOSWITHC_ARGPARSER_H
