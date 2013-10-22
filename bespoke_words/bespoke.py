# Write a web site that provides organic hand-crafted cage-free non-GMO Words,
# carefully selected by skilled artisans for each visitor. Each Words will be
# randomly from a lovingly curated dictionary, and no Word will be given out
# more than once (i.e. to more than one user.) Conversely, these bespoke
# Words are one per customer: if a user leaves and comes back, he receives the
# same Word he was assigned.

# Write this project twice, two different ways:
# * In Phase 1, do it entirely within the browser: the server will serve up one
#   page, and that page does the rest.
# * In Phase 2, do it entirely on the server: you may not use JavaScript.


# will need to initialize array of words (read in from file)
# when user goes to page: check for cookie. if no cookie: set cookie,
# pick and remove random key from array
# THEN keep a dict of already used words. Key = cookie, value = word.
# if a visitor comes to site and cookie exists: retrieve work from dict
# using cookie as value.