#!/bin/sh

# previous saved rules
RULE_FILE="../db/mallory_iptables_backup"

# restore
iptables-restore < $RULE_FILE

# remove rule file
rm -f $RULE_FILE

