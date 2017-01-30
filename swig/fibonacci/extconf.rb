require 'mkmf'

$CFLAGS << ' -std=c11 -Wall -Wextra -g0 -O3 '

create_makefile('fibonacci')
