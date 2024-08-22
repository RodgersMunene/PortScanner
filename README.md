In this Project, I intend to show how a basic portscanner works;
</br>
--I'll import relevant modules
</br>
  **sys
 </br>
  **socket
 </br>
  **datetime
 </br>
--Define my target
</br>
 **an if statement to check for length of arguments (argv);
 </br>
 **maintain appropriate syntax;
 </br>
 (all this does is translate the hostname to IPv4 when correct.)
 </br>
--Add a banner to showcase progress
</br>
--Check for open ports
</br>
 **We try: a for loop to:
 </br>
 **give a range of scan for ports,
 </br>
 **provide a variable to store both our IPv4, and ports once a scan is done,
 </br>
 **set a default timeout to 1sec,
 </br>
 **provide a variable to store result once the socket successfully finds a target port,
 </br>
 **run an if statement to test logic of open/closed,
 </br>
 **close() if else.
 </br>
A very (slow process overall)...
</br>
I provided exception in the code, such as;
</br>
--KeyboardInterrupt - Ctrl + C
</br>
--socket.gaierror - for unresolved hostnames
</br>
--socket.error - for unestablished server connections
</br>
(provided a sys.exit() way out with relevant information displayed.)
