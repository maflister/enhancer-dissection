# Author: Timothy Bailey

# The following section sets site-specific global variables  
# that are set during running "configure"
#
# MAXTIME         - wall time limit for job to run
#

package Globals;

require Exporter;
@ISA = qw(Exporter);
@EXPORT = qw(
         $MAXTIME
         $MINMEMESEQW
         $MINW
         $MAXW
         $CMAX
         $MINSITES
         $MAXSITES
         $MINPSPW
         $MAXPSPW
);

our $MAXTIME = '14400';
our $MINMEMESEQW = 8;
our $MINW = 3;
our $MAXW = 30;
our $CMAX = 100;
our $MINSITES = 2;
our $MAXSITES = 600;
our $MINPSPW = 3;
our $MAXPSPW = 20;
