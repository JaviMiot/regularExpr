#!/usr/bin/perl

use strict;
use warnings;

my $t = time;
open(my $f,"<./results.csv") or die("no hay archivo");

my $match = 0;
my $nomatch = 0;

while (<$f>){
    chomp;
    if(m/^(\d{4})\-.*?,(.*?),(Ecuador),(\d+),(\d+),.*$/){
        if($5 > $4){
            printf("%s %s (%d) - (%d) %s\n",
             $1, $2,$4,$5,$3
            )
        }
        $match++;
    }else{
        $nomatch++;
    }
}

close($f);

printf("se encontraron: \n - %d matches\n - %d no maches \n tardo %d segundos",
 $match, $nomatch,time() - $t);