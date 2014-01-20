#!/bin/sh

# previous saved rules
RULE_FILE="../db/mallory_iptables_backup"

# backup
iptables-save > $RULE_FILE

