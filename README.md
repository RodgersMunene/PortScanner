In this Project, I intend to show how a basic portscanner works;
--I'll import relevant modules
 **sys
 **socket
 **datetime
--Define my target
 **an if statement to check for length of arguments (argv);
 **maintain appropriate syntax;
 (all this does is translate the hostname to IPv4 when correct.)
--Add a banner to showcase progress
--Check for open ports
 **We try: a for loop to:
 **give a range of scan for ports,
 **provide a variable to store both our IPv4, and ports once a scan is done,
 **set a default timeout to 1sec,
 **provide a variable to store result once the socket successfully finds a target port,
 **run an if statement to test logic of open/closed,
 **close() if else.
A very (slow process overall)...
I provided exception in the code, such as;
--KeyboardInterrupt - Ctrl + C
--socket.gaierror - for unresolved hostnames
--socket.error - for unestablished server connections
(provided a sys.exit() way out with relevant information displayed.)
