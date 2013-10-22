# You work for a pizza restaurant. Your restaurant has an oven with 4 slots
# where pizzas can be cooked. How long the pizza takes to cook varies by its
# size and number of toppings:
#   * Small: 10 minutes
#   * Medium: 15 minutes
#   * Large: 20 minutes
#   * Colossal: 25 minutes
#   * Each topping adds 2 minutes
# Write a program that:
#   * Reads in a JSON file I provide [happy to use a different format if you
#     prefer] containing a list of pizza configs
#   * Schedules the pizzas to be cooked in the slots
#     * Just do first-come first-served, no "optimal" solution required
#   * Prints out the schedule to console